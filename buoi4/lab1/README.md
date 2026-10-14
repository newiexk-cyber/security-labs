# Lab 1: Web Vulnerability Scanner - Công cụ kiểm thử lỗ hổng Web

- **Sinh viên thực hiện**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

---

## 1. Giới thiệu tổng quan

**WebVulnScanner** là công cụ kiểm thử bảo mật ứng dụng web tự động, tập trung phát hiện các lỗ hổng nguy hiểm hàng đầu trong danh mục OWASP Top 10:
- **XSS Scanner (`scanners/xss_scanner.py`)**: Tự động chèn các payload tấn công XSS phổ biến (`<script>alert(1)</script>`, `"><svg/onload=alert(1)>`) vào tham số HTTP GET, kiểm tra cơ chế phản hồi để phát hiện Reflected Cross-Site Scripting.
- **SQL Injection Tester (`scanners/sql_injection_tester.py`)**: Phân tích tham số URL để phát hiện các mẫu tấn công SQL Injection kinh điển (`' OR '1'='1`, `'; DROP TABLE users;--`, `UNION SELECT`).
- **CSRF Detector (`scanners/csrf_detector.py`)**: Phân tích cú pháp form HTML thông qua Regex để kiểm tra sự hiện diện của các token chống giả mạo (`csrf_token`, `_csrf`, `csrfmiddlewaretoken`).
- **SSRF Tester (`scanners/ssrf_tester.py`)**: Phát hiện các tham số URL truyền vào địa chỉ IP riêng tư nội bộ (`127.0.0.1`, `localhost`, `10.x.x.x`, `192.168.x.x`, `172.16-31.x.x`) nhằm ngăn chặn tấn công máy chủ gọi ngược vào mạng cục bộ.
- **Report Generator (`report/report_generator.py`)**: Tổng hợp danh sách các lỗ hổng tìm được và chuẩn hóa báo cáo theo các cấp độ rủi ro: `Critical`, `High`, `Medium`, `Low`.

---

## 2. Cấu trúc thư mục

```text
buoi4/lab1/
├── report/
│   ├── __init__.py
│   └── report_generator.py     # Module tổng hợp báo cáo lỗ hổng
├── scanners/
│   ├── __init__.py
│   ├── csrf_detector.py        # Kiểm tra token CSRF trong HTML
│   ├── sql_injection_tester.py # Kiểm tra biến thể SQL Injection
│   ├── ssrf_tester.py          # Kiểm tra tham số gọi IP nội bộ
│   └── xss_scanner.py          # Kiểm tra phản hồi mã độc XSS
├── tests/
│   ├── __init__.py
│   ├── test_csrf.py
│   ├── test_report.py
│   ├── test_sql_injection.py
│   ├── test_ssrf.py
│   └── test_xss.py
├── ui/
│   ├── templates/
│   │   ├── index.html          # Form nhập liệu kiểm thử
│   │   └── result.html         # Giao diện hiển thị báo cáo rủi ro
│   └── app.py                  # Máy chủ Flask Web UI
├── main.py                     # Demo kiểm thử quét qua giao diện dòng lệnh
└── requirements.txt
```

---

## 3. Hướng dẫn khởi chạy và kiểm thử

### 3.1. Chạy kiểm thử tự động (Unit Tests)
```powershell
python -m unittest discover tests
```
Hệ thống sẽ thực thi toàn bộ 9 bài kiểm thử độc lập cho 5 module và trả về trạng thái `OK`.

### 3.2. Chạy kiểm thử qua giao diện dòng lệnh (CLI)
```powershell
python main.py
```
Chương trình sẽ quét thử nghiệm một URL mẫu và in báo cáo phân loại rủi ro ra màn hình console.

### 3.3. Khởi chạy giao diện Web Flask
```powershell
python ui/app.py
```
Mở trình duyệt truy cập `http://localhost:5000/`, nhập URL cần quét và đánh dấu chọn các công cụ kiểm thử (XSS, SQL Injection, CSRF, SSRF) để xem kết quả trực quan.
