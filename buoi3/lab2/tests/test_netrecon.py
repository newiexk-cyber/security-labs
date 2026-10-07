import pytest
import os
import sys
import asyncio

# Them thu muc lab2 vao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.filter_utils import filter_targets
from modules.vuln_checker import check_vulns, VULN_PORTS
from modules.port_scanner import async_scan_ports
from modules.service_detector import detect_service
from modules.network_mapper import map_network
from app import app

def test_filter_targets():
    ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "8.8.8.8"]
    whitelist = ["192.168.1.1", "10.0.0.1"]
    blacklist = ["10.0.0.1"]

    filtered = filter_targets(ip_list, whitelist=whitelist)
    assert set(filtered) == {"192.168.1.1", "10.0.0.1"}

    filtered = filter_targets(ip_list, whitelist=whitelist, blacklist=blacklist)
    assert filtered == ["192.168.1.1"]

    assert filter_targets(ip_list) == ip_list

def test_vuln_checker():
    ports = [21, 22, 80, 8080, 9999]
    vulns = check_vulns(ports)
    assert 21 in vulns
    assert "FTP" in vulns[21]
    assert 22 in vulns
    assert "SSH" in vulns[22]
    assert 80 in vulns
    assert "HTTP" in vulns[80]
    assert 8080 not in vulns
    assert 9999 not in vulns

def test_async_port_scanner():
    res = asyncio.run(async_scan_ports("127.0.0.1", [65432], rate_limit=10))
    assert isinstance(res, list)

def test_service_detector():
    res = detect_service("127.0.0.1", [80])
    assert "Nmap" in res or "closed" in res or "open" in res

def test_network_mapper():
    res = map_network()
    assert "Interface" in res or "Internet Address" in res

def test_flask_routes():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"NetRecon" in resp.data

    post_resp = client.post('/scan', data={
        'target': '127.0.0.1',
        'ports': '80,443',
        'mode': 'vuln',
        'email': 'test@example.com'
    })
    assert post_resp.status_code == 200
    assert b"Vulnerability Check" in post_resp.data
