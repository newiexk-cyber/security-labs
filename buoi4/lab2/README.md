# Lab 2: JWTSecure - Bộ công cụ kiểm thử bảo mật JWT & OAuth 2.0

- **Sinh viên thực hiện**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

---

## 1. Giới thiệu tổng quan

**JWTSecure** là bộ công cụ toàn diện phục vụ việc xây dựng, kiểm thử và đánh giá độ an toàn của cơ chế xác thực Token (JSON Web Token) và ủy quyền OAuth 2.0:
- **API Gateway (`api_gateway/gateway.py`)**: Cổng API xây dựng trên Flask, bảo vệ endpoint `/protected` bằng cách xác thực JWT Bearer token trong HTTP Authorization header.
- **JWT Cracker (`jwt_cracker/cracker.py`)**: Công cụ kiểm thử độ mạnh của khóa bí mật HMAC-SHA256 (`HS256`) bằng phương pháp brute-force từ điển (wordlist attack) đa luồng (`ThreadPoolExecutor`).
- **JWT Validator (`jwt_validator/validator.py`)**: Kiểm tra toàn diện tính hợp lệ của token, xử lý chi tiết các ngoại lệ `ExpiredSignatureError`, `InvalidSignatureError` và `InvalidTokenError`.
- **OAuth 2.0 Client (`oauth_client/client.py`)**: Mô phỏng client OAuth 2.0 tuân thủ luồng Authorization Code Flow chuẩn (sinh Authorization URL và đổi authorization code lấy access token).
- **Token Manager (`token_manager/manager.py`)**: Quản lý vòng đời cặp token Access Token (thời hạn ngắn) và Refresh Token (thời hạn dài), hỗ trợ cấp mới access token an toàn.
- **Bảo mật mã nguồn**: Tuân thủ tiêu chuẩn quét mã tự động GitSecure, không lưu trữ hardcoded secret thô trong code.

---

## 2. Cấu trúc thư mục

```text
buoi4/lab2/
├── api_gateway/
│   ├── __init__.py
│   └── gateway.py              # Flask API Gateway xác thực JWT
├── jwt_cracker/
│   ├── __init__.py
│   └── cracker.py              # Công cụ brute-force secret JWT
├── jwt_validator/
│   ├── __init__.py
│   └── validator.py            # Kiểm tra chữ ký và hạn dùng token
├── oauth_client/
│   ├── __init__.py
│   └── client.py               # Client OAuth 2.0 chuẩn hóa
├── token_manager/
│   ├── __init__.py
│   └── manager.py              # Quản lý phát hành và refresh token
├── tests/
│   ├── __init__.py
│   ├── test_api_gateway.py
│   ├── test_cracker.py
│   ├── test_oauth_client.py
│   ├── test_token_manager.py
│   └── test_validator.py
├── main.py                     # Demo phát hành token và khởi chạy API Gateway
├── pytest.ini
└── requirements.txt
```

---

## 3. Hướng dẫn khởi chạy và kiểm thử

### 3.1. Chạy kiểm thử tự động (Pytest)
```powershell
pytest tests/
```
Chạy toàn bộ 7 test case kiểm tra API Gateway, JWT Cracker, OAuth Client, Token Manager và Validator.

### 3.2. Khởi chạy API Gateway & Xác thực Token
1. Khởi động server API Gateway:
```powershell
python main.py
```
Chương trình sẽ tự động sinh cặp `Access Token` và `Refresh Token`, đồng thời khởi chạy máy chủ tại `http://127.0.0.1:5000`.

2. Kiểm tra truy cập hợp lệ bằng `curl`:
```powershell
curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:5000/protected
```
Kết quả phản hồi:
```json
{"message": "Access granted", "user": "Nguyen_Nhat_Lam"}
```

3. Kiểm tra trường hợp token không hợp lệ:
```powershell
curl -H "Authorization: Bearer invalid_token" http://127.0.0.1:5000/protected
```
Kết quả phản hồi mã lỗi HTTP 401:
```json
{"message": "Access denied"}
```
