# DAST-Tool: Dynamic Analysis Security Testing

## 1. Giới thiệu
Nền tảng kiểm thử và phân tích động (DAST) trong môi trường runtime:
- Giám sát CPU, bộ nhớ, danh sách file mở của tiến trình (`psutil`).
- Phát hiện rò rỉ bộ nhớ (memory leaks) và tràn bộ nhớ (overflow).
- Thống kê lưu lượng mạng theo card mạng thời gian thực.
- Nhận diện các lệnh hệ thống nguy hiểm (`os.system`, `eval`, `exec`).
- Thực thi mã cô lập trong Virtual Sandbox an toàn.
- Cung cấp RESTful API giám sát qua Flask.

## 2. Cấu trúc thư mục
```text
dast-tool/
├── requirements.txt
├── __init__.py
├── memory_analyzer.py
├── network_traffic_analyzer.py
├── runtime_monitor.py
├── security_behavior_checker.py
├── virtual_sandbox.py
├── main.py
├── app.py
└── tests/
    ├── __init__.py
    ├── test_memory_analyzer.py
    ├── test_network_traffic_analyzer.py
    ├── test_runtime_monitor.py
    ├── test_security_behavior_checker.py
    └── test_virtual_sandbox.py
```

## 3. Cài đặt và thực thi
```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Chạy kiểm thử tự động
python -m unittest discover -s tests

# Chạy demo kiểm thử động
python main.py

# Khởi chạy Flask API Server
python app.py
```
