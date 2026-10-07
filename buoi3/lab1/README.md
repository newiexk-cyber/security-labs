# Lab 1: SecureChat - Lập trình Socket an toàn với SSL/TLS và Mã hóa AES

- **Sinh viên thực hiện**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

---

## 1. Mục tiêu và Kiến trúc

Lab 1 tập trung xây dựng ứng dụng chat thời gian thực qua giao thức mạng với các tiêu chuẩn bảo mật cao cấp:
- **Xác thực chứng chỉ hai chiều (Mutual TLS / mTLS)**: Cả Server và Client đều sở hữu chứng chỉ X.509 được cấp bởi Certificate Authority (CA) nội bộ và kiểm tra chéo tính hợp lệ trước khi bắt tay thiết lập phiên.
- **Mã hóa kênh truyền TLS 1.2+**: Bảo vệ toàn bộ dữ liệu trao đổi trước các cuộc tấn công nghe lén (Sniffing) và tấn công xen giữa (Man-in-the-Middle - MITM).
- **Mã hóa nội dung tin nhắn đầu-cuối (End-to-End Encryption)**: Tin nhắn được mã hóa bằng thuật toán đối xứng **AES-256-CBC** kết hợp cơ chế đệm **PKCS#7** và Vector khởi tạo (IV) ngẫu nhiên 16 bytes.
- **Quản lý phiên đa luồng & Phòng chat**: Server điều phối luồng socket độc lập cho từng client, hỗ trợ phòng chat (`general`) và giải mã / tái mã hóa an toàn theo từng khóa phiên riêng biệt của từng người nhận.

---

## 2. Cấu trúc thư mục Lab 1

```text
buoi3/lab1/
├── certs/                      # Thư mục chứng chỉ số X.509
│   ├── ca/                     # CA nội bộ (ca.crt, ca.key)
│   ├── server/                 # Server cert & private key (server.crt, server.key)
│   └── client/                 # Client cert & private key (client.crt, client.key)
├── tests/
│   └── test_secure_chat.py     # Unit test & Integration test mTLS
├── openssl.cnf                 # Cấu hình OpenSSL sinh CA
├── make-certs.bat              # Script tự động tạo toàn bộ chứng chỉ và khóa RSA
├── message_encryption.py       # Module mã hóa AES-256-CBC + PKCS7
├── connection_manager.py       # Quản lý phiên kết nối và khóa AES của client
├── room_manager.py             # Quản lý danh sách phòng và điều phối broadcast
├── server.py                   # Secure Socket TLS Server đa luồng
├── client.py                   # Secure Socket TLS Client đa luồng
└── requirements.txt            # Thư viện phụ thuộc
```

---

## 3. Hướng dẫn sinh chứng chỉ số

Sử dụng tập lệnh `make-certs.bat` để tự động hóa toàn bộ quy trình:
```powershell
.\make-certs.bat
```
Quy trình thực hiện:
1. Tạo khóa bí mật Root CA (RSA-2048) và chứng chỉ tự ký `ca.crt` với thời hạn 10 năm (3650 ngày).
2. Tạo cặp khóa Server, tạo Certificate Signing Request (CSR) và ký cấp `server.crt` bởi Root CA.
3. Tạo cặp khóa Client, tạo CSR và ký cấp `client.crt` bởi Root CA.

---

## 4. Hướng dẫn khởi chạy và kiểm thử

### Khởi chạy Server
```powershell
python server.py
```
Server sẽ lắng nghe tại `127.0.0.1:8443`, yêu cầu xác thực chứng chỉ client (`ssl.CERT_REQUIRED`) và kích hoạt TLS 1.2 trở lên.

### Khởi chạy Client
Mở terminal riêng biệt và chạy:
```powershell
python client.py
```
- Nhập Username của bạn (ví dụ: `Nguyen_Nhat_Lam`).
- Client tự động tạo khóa AES-256 ngẫu nhiên, kết nối TLS đến server, xác thực chứng chỉ `ca.crt` và gửi khóa an toàn cho server.
- Có thể mở đồng thời 2-3 client để thử nghiệm chat broadcast trong phòng `general`.

### Chạy kiểm thử tự động
```powershell
pytest tests/test_secure_chat.py -v
```
