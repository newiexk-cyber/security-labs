# Lab 2: NetRecon - Bộ công cụ trinh sát mạng & Phát hiện lỗ hổng

- **Sinh viên thực hiện**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

---

## 1. Giới thiệu tổng quan

**NetRecon** (Network Reconnaissance Toolkit) là bộ công cụ thực hành khám phá hệ thống mạng, phục vụ công tác đánh giá an ninh phòng thủ (Defensive Security). Công cụ bao gồm cả giao diện dòng lệnh (CLI) và giao diện trực quan trên nền tảng Web (Flask + HTMX).

Các tính năng chính:
- **Port Scanner (`port_scanner.py`)**: Quét cổng TCP bất đồng bộ bằng `asyncio`, kiểm soát tốc độ quét với cơ chế giới hạn tải `Semaphore(rate_limit)`.
- **Service Detection (`service_detector.py`)**: Tích hợp công cụ chuẩn công nghiệp **Nmap** (`nmap -sV`) để phân tích và nhận diện chính xác phần mềm cùng phiên bản đang hoạt động phía sau cổng mở.
- **Banner Grabbing (`banner_grabber.py`)**: Kết nối socket TCP đến dịch vụ mục tiêu và trích xuất chuỗi định danh dịch vụ ban đầu (banner).
- **Network Mapping (`network_mapper.py`)**: Truy vấn bảng ARP (`arp -a`) của hệ thống để vẽ sơ đồ các thiết bị đang hoạt động trong cùng mạng LAN.
- **Vulnerability Checker (`vuln_checker.py`)**: Cơ sở dữ liệu đối chiếu cổng mở với các lỗ hổng bảo mật nghiêm trọng (CVE) đã biết trong thực tế.
- **Target Filtering (`filter_utils.py`)**: Hỗ trợ danh sách Whitelist/Blacklist để bảo đảm phạm vi kiểm thử an toàn.
- **Email Reporting (`email_sender.py`)**: Tự động gửi kết quả quét qua giao thức bảo mật SMTP SSL (cổng 465).

---

## 2. Bảng cơ sở dữ liệu lỗ hổng (Vulnerability Mapping)

| Cổng (Port) | Dịch vụ (Service) | Mã CVE tham chiếu | Mô tả nguy cơ |
| :---: | :---: | :---: | :--- |
| **21** | FTP | `CVE-2015-3306`, `CVE-2001-0261` | Lỗ hổng chèn lệnh từ xa ProFTPD mod_copy, rò rỉ buffer |
| **22** | SSH | `CVE-2018-15473` | Lỗ hổng rò rỉ danh sách người dùng OpenSSH qua User Enumeration |
| **23** | Telnet | `CVE-2011-4862` | Lỗ hổng tràn bộ đệm giao thức Telnet mã hóa kém |
| **80** | HTTP | `CVE-2021-41773` | Lỗ hổng duyệt đường dẫn (Path Traversal) trên Apache HTTP Server 2.4.49 |
| **443** | HTTPS | `CVE-2021-3449` | Lỗ hổng từ chối dịch vụ (DoS) OpenSSL renegotiation crash |

---

## 3. Hướng dẫn sử dụng

### 3.1. Sử dụng qua giao diện dòng lệnh (CLI)

```powershell
# Quét toàn bộ thông tin trên máy localhost (cổng 80, 443, 8443)
python cli.py --target 127.0.0.1 --ports 80,443,8443 --mode all

# Chỉ quét cổng mở bất đồng bộ
python cli.py --target 127.0.0.1 --ports 22,80,443 --mode scan

# Chỉ kiểm tra phiên bản dịch vụ qua Nmap
python cli.py --target 127.0.0.1 --ports 80,443 --mode service
```

### 3.2. Sử dụng qua giao diện Web (Flask)

1. Khởi động Web Server:
```powershell
python app.py
```
2. Mở trình duyệt tại địa chỉ: `http://localhost:5000/`.
3. Nhập IP mục tiêu (ví dụ `127.0.0.1`), danh sách cổng (ví dụ `80,443,8443`), chọn chế độ và nhập email nhận kết quả.
4. Bấm **Scan** để xem kết quả trả về động qua HTMX.

### 3.3. Chạy kiểm thử tự động
```powershell
pytest tests/test_netrecon.py -v
```
