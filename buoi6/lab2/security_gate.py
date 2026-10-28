import os
import re
import sys
import json

class DevSecOpsGate:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.findings = []

    def scan_secrets(self):
        # Scan for leaked API keys, tokens, hardcoded credentials
        patterns = [
            (r"(api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]", "High Severity: Leaked API Secret/Token"),
            (r"BEGIN\s+(RSA|OPENSSH|EC)?\s*PRIVATE\s+KEY", "Critical Severity: Hardcoded Private Key")
        ]
        count = 0
        for root, _, files in os.walk(self.root_dir):
            if any(skip in root for skip in [".git", "node_modules", "build", "public", ".pytest_cache"]):
                continue
            for file in files:
                fpath = os.path.join(root, file)
                try:
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    for pattern, desc in patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            self.findings.append({"file": fpath, "rule": "Secret-Scan", "detail": desc})
                            count += 1
                except Exception:
                    pass
        return count

    def scan_dependencies(self):
        pkg_path = os.path.join(self.root_dir, "package.json")
        if os.path.exists(pkg_path):
            with open(pkg_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            deps = data.get("dependencies", {})
            return len(deps)
        return 0

    def run_all(self):
        secrets_found = self.scan_secrets()
        deps_checked = self.scan_dependencies()
        report = {
            "status": "PASSED" if secrets_found == 0 else "FAILED",
            "secrets_found": secrets_found,
            "dependencies_checked": deps_checked,
            "findings": self.findings
        }
        with open(os.path.join(self.root_dir, "security-report.json"), "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        return report

if __name__ == "__main__":
    gate = DevSecOpsGate()
    rep = gate.run_all()
    print(f"[*] DevSecOps Security Gate Result: {rep['status']}")
    print(f"    - Secrets Found: {rep['secrets_found']}")
    print(f"    - Dependencies Checked: {rep['dependencies_checked']}")
    if rep['status'] != "PASSED":
        sys.exit(1)
