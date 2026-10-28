# Lab 1: Thực hành CI/CD cơ bản với GitLab

- **Sinh viên**: Nguyễn Nhật Lâm
- **MSSV**: 2387700036
- **Môn học**: Lập trình an toàn (Bảo mật ứng dụng)

## 1. Giới thiệu
Triển khai pipeline GitLab CI/CD cơ bản gồm 3 giai đoạn (Stages):
- **build**: Thực thi `build-job` chào mừng người dùng (`$GITLAB_USER_LOGIN`).
- **test**: Thực thi song song `test-job1` và `test-job2` (mô phỏng kiểm thử có độ trễ).
- **deploy**: Thực thi `deploy-prod` triển khai tự động lên môi trường `production`.

## 2. Cấu trúc thư mục
```text
lab1/
├── .gitlab-ci.yml      # Cấu hình pipeline CI/CD GitLab
├── pipeline_runner.py  # Script mô phỏng và chạy kiểm thử pipeline cục bộ
├── requirements.txt    # Thư viện phụ thuộc (pyyaml)
└── tests/
    └── test_pipeline.py # Unit tests kiểm tra tính toàn vẹn của CI config
```

## 3. Cách chạy kiểm thử
```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Chạy kiểm thử tự động
python -m unittest discover tests

# Chạy mô phỏng pipeline
python pipeline_runner.py
```
