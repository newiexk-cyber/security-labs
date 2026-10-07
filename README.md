# Báo cáo thực hành Lập trình an toàn

- **Sinh viên**: Nguyễn Nhật Lâm
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)
- **Repository**: [https://github.com/newiexk-cyber/security-labs](https://github.com/newiexk-cyber/security-labs)

Repository lưu trữ mã nguồn và báo cáo các bài thực hành môn Lập trình an toàn.

---

## Danh sách bài thực hành

### [Buổi 1: Cơ sở lập trình bảo mật và kiểm tra đầu vào](./buoi1/README.md)
- **Lab 1**: Kiểm tra và làm sạch dữ liệu đầu vào (Input Validation & Sanitization).
- **Lab 2**: Cấu hình Git Pre-commit Hook tự động ngăn chặn rò rỉ khóa bí mật.
- **Lab 3**: Xây dựng hệ thống Secure Logger bảo mật nhật ký ứng dụng.

### [Buổi 2: Mật mã ứng dụng và hạ tầng khóa công khai (PKI)](./buoi2/README.md)
- **Lab 1**: Thư viện mật mã SecureCrypto (AES-256-GCM, Argon2id, RSA-2048, CLI & GUI).
- **Lab 2**: Hệ thống chứng thực số Mini Certificate Authority (X.509, Chuỗi chứng chỉ, CRL & OCSP).

### [Buổi 3: Bảo mật mạng máy tính](./buoi3/README.md)
- **Lab 1**: Ứng dụng SecureChat qua Socket SSL/TLS (xác thực mTLS, mã hóa đầu-cuối AES-256-CBC, đa luồng).
- **Lab 2**: Bộ công cụ trinh sát mạng NetRecon (quét cổng bất đồng bộ asyncio, nhận diện dịch vụ Nmap, bản đồ ARP, đối chiếu CVE, CLI & Web Flask).

---

## Cấu trúc thư mục

```text
security-labs/
├── README.md               # Tổng quan môn học và danh mục bài thực hành
├── buoi1/                  # Buổi 1: Input Validation, Git Hook, Secure Logger
│   ├── README.md           # Báo cáo chi tiết Buổi 1 kèm ảnh minh chứng
│   ├── images/             # Ảnh chụp kiểm thử thực tế Buổi 1
│   ├── lab1/               # Lab 1: Flask Input Validator
│   ├── lab2/               # Lab 2: Git Pre-commit Security Hook
│   └── lab3/               # Lab 3: Secure Logger System
├── buoi2/                  # Buổi 2: Mật mã ứng dụng và Mini CA (PKI)
│   ├── README.md           # Báo cáo chi tiết Buổi 2 kèm ảnh minh chứng
│   ├── images/             # Ảnh chụp kiểm thử thực tế Buổi 2
│   ├── lab1/               # Lab 1: Thư viện mật mã SecureCrypto
│   └── lab2/               # Lab 2: Hệ thống chứng thực số Mini CA (PKI)
└── buoi3/                  # Buổi 3: Bảo mật mạng máy tính
    ├── README.md           # Báo cáo chi tiết Buổi 3 kèm ảnh minh chứng
    ├── images/             # Ảnh chụp kiểm thử thực tế Buổi 3
    ├── lab1/               # Lab 1: Ứng dụng chat bảo mật SecureChat (SSL/TLS & AES)
    └── lab2/               # Lab 2: Bộ công cụ trinh sát mạng NetRecon (Nmap & Flask)
```
