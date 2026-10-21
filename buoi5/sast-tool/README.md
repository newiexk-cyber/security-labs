# SAST-Tool: Static Analysis Security Testing

## 1. Giới thiệu
Công cụ phân tích mã nguồn tĩnh (SAST) cho Python, phát hiện các mẫu mã nguy hiểm, đánh giá chất lượng mã nguồn bằng linter và xuất báo cáo chuẩn SARIF.

## 2. Cấu trúc thư mục
```text
sast-tool/
├── requirements.txt
├── examples/
│   ├── vulnerable_01.py
│   └── vulnerable_02.py
├── rules/
│   └── default_rules.json
├── sast_tool/
│   ├── __init__.py
│   ├── ast_analyzer.py
│   ├── code_quality_checker.py
│   ├── main.py
│   ├── sarif_reporter.py
│   ├── security_rule_engine.py
│   └── vuln_pattern_matcher.py
└── tests/
    ├── __init__.py
    ├── test_ast_analyzer.py
    ├── test_code_quality_checker.py
    ├── test_sarif_reporter.py
    ├── test_security_rule_engine.py
    └── test_vuln_pattern_matcher.py
```

## 3. Cài đặt và thực thi
```bash
# Cài đặt thư viện
pip install -r requirements.txt

# Chạy kiểm thử tự động
python -m unittest discover tests

# Quét mã nguồn và xuất báo cáo SARIF
python -m sast_tool.main examples/vulnerable_01.py
python -m sast_tool.main examples/vulnerable_02.py
```
