# Đặc tả thiết kế Buổi 3: Bảo mật mạng máy tính

- **Sinh viên**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)
- **Mục tiêu**: Xây dựng ứng dụng chat bảo mật qua Socket SSL/TLS (SecureChat) và bộ công cụ trinh sát mạng (NetRecon).

---

## 1. Tổng quan yêu cầu

### Lab 1: SecureChat (Lập trình Socket an toàn & mã hóa đầu-cuối)
1. **Hạ tầng chứng chỉ SSL/TLS**:
   - Tự tạo Root CA nội bộ (ca.crt, ca.key).
   - Cấp chứng chỉ cho Server (server.crt, server.key) và Client (client.crt, client.key) được ký bởi Root CA.
   - Bắt buộc xác thực hai chiều (Mutual TLS / mTLS) với ssl.CERT_REQUIRED.
2. **Mã hóa tin nhắn (MessageEncryption)**:
   - Thuật toán đối xứng AES-256-CBC, sử dụng PKCS#7 padding (thư viện cryptography).
   - Khóa AES ngẫu nhiên 256-bit được tạo riêng cho từng phiên client (os.urandom(32)).
   - IV ngẫu nhiên 16 bytes gắn kèm vào đầu mỗi gói tin mã hóa.
3. **Quản lý kết nối & phòng chat**:
   - ConnectionManager: Quản lý danh sách socket, tên người dùng, khóa giải mã AES tương ứng, đồng bộ thread-safe với 	hreading.Lock.
   - RoomManager: Hỗ trợ tạo phòng, tham gia (join_room), rời phòng (leave_room), gửi tin nhắn theo phòng (roadcast_room).
4. **Server & Client Socket đa luồng**:
   - server.py: Server socket đa luồng, hỗ trợ TLSv1.2 trở lên, giải mã tin nhắn nhận được và mã hóa lại theo từng khóa riêng của client trong phòng để gửi tiếp.
   - client.py: Khởi tạo kết nối TLS, xác thực chứng chỉ server, gửi khóa AES cho server, chạy luồng nhận tin nhắn ngầm và giao diện console nhập tin nhắn.

### Lab 2: NetRecon (Bộ công cụ trinh sát mạng & phát hiện lỗ hổng)
1. **Các module chức năng**:
   - modules/port_scanner.py: Quét cổng bất đồng bộ bằng syncio và socket, kiểm soát tải với syncio.Semaphore(rate_limit).
   - modules/service_detector.py: Gọi lệnh Nmap (
map -sV -p ...) để nhận diện dịch vụ và phiên bản ứng dụng trên các cổng mở.
   - modules/banner_grabber.py: Kết nối socket và đọc chuỗi banner dịch vụ trả về.
   - modules/network_mapper.py: Đọc bảng ARP hệ thống (rp -a) để phát hiện các thiết bị trong mạng cục bộ.
   - modules/vuln_checker.py: Ánh xạ danh sách cổng quét được với cơ sở dữ liệu mã định danh CVE nguy hiểm phổ biến.
   - modules/filter_utils.py: Lọc danh sách IP theo Whitelist và Blacklist.
   - modules/email_sender.py: Gửi báo cáo kết quả quét tự động qua giao thức SMTP SSL (Gmail).
2. **Giao diện dòng lệnh (CLI)**:
   - cli.py: Sử dụng thư viện click cung cấp các tham số --target, --ports, --rate-limit, --mode (scan, service, banner, map, vuln, all).
3. **Giao diện Web (Flask + HTMX)**:
   - pp.py: Web server Flask, các route / và /scan (POST).
   - 	emplates/index.html, 	emplates/layout.html, 	emplates/result.html: Form nhập liệu và trả kết quả động qua HTMX.
   - static/style.css: Giao diện terminal tối hiện đại.

---

## 2. Kiểm thử & Đảm bảo chất lượng (TDD)
- **Kiểm thử Lab 1**: Unit test cho mã hóa/giải mã AES-CBC PKCS7, kiểm tra ConnectionManager và RoomManager. Kiểm tra kết nối TLS thực tế giữa client và server.
- **Kiểm thử Lab 2**: Unit test cho bộ lọc IP ilter_utils, uln_checker, 
etwork_mapper, kiểm tra quét cổng CLI và Web UI thực tế.
