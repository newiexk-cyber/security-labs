# Kế hoạch triển khai Buổi 3: Bảo mật mạng máy tính

- **Mục tiêu**: Xây dựng hoàn chỉnh Lab 1 (SecureChat) và Lab 2 (NetRecon) theo tài liệu thực hành môn học.
- **Tiêu chuẩn chất lượng**: Không dùng placeholder/stub, 100% chức năng chạy thật, unit test đầy đủ, báo cáo chi tiết kèm ảnh minh chứng.

---

## Các bước triển khai

### Bước 1: Khởi tạo cấu trúc dự án Buổi 3
- Tạo các thư mục: uoi3/lab1/certs, uoi3/lab1/tests, uoi3/lab2/modules, uoi3/lab2/templates, uoi3/lab2/static, uoi3/lab2/tests, uoi3/images.

### Bước 2: Triển khai Lab 1 - SecureChat
1. Cấu hình OpenSSL: uoi3/lab1/openssl.cnf.
2. Tạo script tạo chứng chỉ tự động: uoi3/lab1/make-certs.bat và uoi3/lab1/make_certs.py (sử dụng OpenSSL tạo CA, server cert, client cert).
3. Triển khai uoi3/lab1/message_encryption.py (AES-256-CBC, PKCS7).
4. Triển khai uoi3/lab1/connection_manager.py (quản lý socket và encryption key có lock).
5. Triển khai uoi3/lab1/room_manager.py (quản lý room và broadcast có lock).
6. Triển khai uoi3/lab1/server.py (SSL/TLS server socket, client cert auth, chat broadcast).
7. Triển khai uoi3/lab1/client.py (SSL/TLS client, AES encryption, multithreaded receive/send).
8. Viết unit test uoi3/lab1/tests/test_secure_chat.py. Chạy pytest đảm bảo kiểm thử vượt qua.

### Bước 3: Triển khai Lab 2 - NetRecon
1. Triển khai uoi3/lab2/modules/filter_utils.py (Whitelist/Blacklist).
2. Triển khai uoi3/lab2/modules/port_scanner.py (Asyncio port scanner với semaphore).
3. Triển khai uoi3/lab2/modules/service_detector.py (Nmap wrapper).
4. Triển khai uoi3/lab2/modules/banner_grabber.py (Socket banner grabber).
5. Triển khai uoi3/lab2/modules/network_mapper.py (ARP table mapper).
6. Triển khai uoi3/lab2/modules/vuln_checker.py (CVE mapping database).
7. Triển khai uoi3/lab2/modules/email_sender.py (SMTP SSL email dispatcher).
8. Triển khai uoi3/lab2/cli.py (Click CLI command).
9. Triển khai uoi3/lab2/app.py và các template HTML/CSS trong 	emplates/ và static/.
10. Tạo file cấu hình uoi3/lab2/requirements.txt và uoi3/lab2/.env.
11. Viết unit test uoi3/lab2/tests/test_netrecon.py. Chạy pytest đảm bảo kiểm thử vượt qua.

### Bước 4: Thực thi kiểm thử và thu thập minh chứng thực tế
1. Chạy sinh cặp chứng chỉ x509 cho CA, Server, Client.
2. Khởi chạy thử nghiệm SecureChat (Server + Client gửi tin nhắn mã hóa).
3. Khởi chạy NetRecon CLI và Web Flask, quét cổng localhost và kiểm tra kết quả.
4. Chụp/ghi lại ảnh minh chứng thực tế lưu vào uoi3/images/.

### Bước 5: Viết tài liệu báo cáo và hoàn thiện commit
1. Viết báo cáo chi tiết uoi3/README.md.
2. Viết tài liệu con uoi3/lab1/README.md và uoi3/lab2/README.md.
3. Cập nhật mục lục README.md gốc của repository.
4. Thực hiện commit chuẩn sinh viên và đồng bộ lên GitHub.
