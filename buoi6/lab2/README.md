# Lab 2: Tạo pipeline CI/CD phức tạp với Docusaurus và DevSecOps

- **Sinh viên**: Nguyễn Nhật Lâm
- **MSSV**: 2387700036
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

## 1. Giới thiệu
Triển khai pipeline CI/CD phức tạp với ứng dụng tài liệu Docusaurus, tích hợp chốt kiểm tra bảo mật (DevSecOps Security Gate) và triển khai tự động lên GitLab Pages:
- **Stage 1 (Build)**: Sử dụng Docker container `node` biên dịch trang tĩnh Docusaurus sang thư mục `build/` và lưu dưới dạng artifacts.
- **Stage 2 (Security)**: Chốt kiểm tra an toàn tự động (quét lộ mật khẩu/API key, phân tích lỗ hổng thư viện phụ thuộc).
- **Stage 3 (Deploy)**: Job `pages` di chuyển artifact `build/` sang `public/` để phục vụ trực tuyến tại URL GitLab Pages.

## 2. Cấu trúc thư mục
```text
lab2/
├── .gitlab-ci.yml          # Cấu hình pipeline đa giai đoạn (build, security, deploy)
├── build_site.js           # Kịch bản biên dịch trang Docusaurus tĩnh
├── docusaurus.config.js    # Cấu hình dự án Docusaurus (URL, baseUrl, theme)
├── package.json            # Khai báo phụ thuộc và scripts npm
├── pipeline_simulator.py   # Trình chạy mô phỏng quy trình CI/CD hoàn chỉnh
├── security_gate.py        # Chốt kiểm tra bảo mật DevSecOps (Secret & SCA)
└── tests/
    └── test_docusaurus_pipeline.py # Unit tests kiểm tra toàn bộ pipeline
```

## 3. Cách chạy kiểm thử
```bash
# Chạy kiểm thử tự động toàn diện
python -m unittest discover tests

# Chạy mô phỏng toàn bộ pipeline
python pipeline_simulator.py
```
