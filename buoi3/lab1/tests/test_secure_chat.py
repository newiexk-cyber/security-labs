import pytest
import os
import sys
import socket
import ssl
import threading
import time
import binascii

# Them thu muc lab1 vao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from message_encryption import MessageEncryption
from connection_manager import ConnectionManager
from room_manager import RoomManager

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SERVER_CERT = os.path.join(BASE_DIR, 'certs', 'server', 'server.crt')
SERVER_KEY = os.path.join(BASE_DIR, 'certs', 'server', 'server.key')
CA_CERT = os.path.join(BASE_DIR, 'certs', 'ca', 'ca.crt')
CLIENT_CERT = os.path.join(BASE_DIR, 'certs', 'client', 'client.crt')
CLIENT_KEY = os.path.join(BASE_DIR, 'certs', 'client', 'client.key')

def test_message_encryption_roundtrip():
    key = os.urandom(32)
    crypto = MessageEncryption(key)
    plaintext = "Hello, Secure Socket World! Tiếng Việt: An toàn bảo mật mạng."
    ciphertext = crypto.encrypt(plaintext)
    assert ciphertext != plaintext.encode()
    assert len(ciphertext) > 16  # IV (16) + ciphertext
    decrypted = crypto.decrypt(ciphertext)
    assert decrypted == plaintext

def test_message_encryption_random_iv():
    crypto = MessageEncryption()
    msg = "Same message test"
    ct1 = crypto.encrypt(msg)
    ct2 = crypto.encrypt(msg)
    # IVs must be different even for identical plaintexts
    assert ct1 != ct2
    assert crypto.decrypt(ct1) == msg
    assert crypto.decrypt(ct2) == msg

def test_connection_manager():
    cm = ConnectionManager()
    dummy_sock = object()
    cm.add_client(dummy_sock, "alice", b"01234567890123456789012345678901")
    client_info = cm.get_client(dummy_sock)
    assert client_info is not None
    assert client_info['username'] == "alice"
    assert client_info['encryption_key'] == b"01234567890123456789012345678901"

    cm.remove_client(dummy_sock)
    assert cm.get_client(dummy_sock) is None

def test_room_manager():
    rm = RoomManager()
    sock1 = object()
    sock2 = object()
    rm.create_room("general")
    assert "general" in rm.rooms

    rm.join_room("general", sock1)
    rm.join_room("general", sock2)
    assert sock1 in rm.rooms["general"]
    assert sock2 in rm.rooms["general"]

    rm.leave_room("general", sock1)
    assert sock1 not in rm.rooms["general"]
    assert sock2 in rm.rooms["general"]

def test_ssl_tls_mutual_auth_communication():
    # Test mTLS connection and encrypted message flow
    if not (os.path.exists(SERVER_CERT) and os.path.exists(CLIENT_CERT)):
        pytest.skip("Certificates not generated yet")

    test_port = 8444
    server_ready = threading.Event()
    received_msgs = []

    def run_server():
        ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ctx.load_cert_chain(certfile=SERVER_CERT, keyfile=SERVER_KEY)
        ctx.load_verify_locations(cafile=CA_CERT)
        ctx.verify_mode = ssl.CERT_REQUIRED
        ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

        srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv_sock.bind(('127.0.0.1', test_port))
        srv_sock.listen(1)
        server_ready.set()

        conn, addr = srv_sock.accept()
        sconn = ctx.wrap_socket(conn, server_side=True)

        data = sconn.recv(1024).decode()
        username, key_hex = data.split(':', 1)
        aes_key = bytes.fromhex(key_hex)
        crypto = MessageEncryption(aes_key)

        enc_msg = sconn.recv(4096)
        plain = crypto.decrypt(enc_msg)
        received_msgs.append((username, plain))

        sconn.close()
        srv_sock.close()

    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    server_ready.wait(timeout=3)

    # Client connection
    client_ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CA_CERT)
    client_ctx.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
    client_ctx.check_hostname = False
    client_ctx.verify_mode = ssl.CERT_REQUIRED

    client_key = os.urandom(32)
    client_crypto = MessageEncryption(client_key)

    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock = client_ctx.wrap_socket(raw_sock, server_hostname='127.0.0.1')
    ssock.connect(('127.0.0.1', test_port))

    # Handshake application data
    ssock.send(f"nhatlam:{binascii.hexlify(client_key).decode()}".encode())
    time.sleep(0.1)

    # Send encrypted message
    enc_test_msg = client_crypto.encrypt("Bảo mật mạng bài 3 thành công!")
    ssock.send(enc_test_msg)

    t.join(timeout=3)
    ssock.close()

    assert len(received_msgs) == 1
    assert received_msgs[0][0] == "nhatlam"
    assert received_msgs[0][1] == "Bảo mật mạng bài 3 thành công!"
