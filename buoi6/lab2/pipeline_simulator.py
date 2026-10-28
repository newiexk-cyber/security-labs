import os
import sys
import shutil
import subprocess
import json

class ComplexPipelineSimulator:
    def __init__(self, project_dir="."):
        self.project_dir = os.path.abspath(project_dir)

    def run_build_job(self):
        print("[*] Stage: BUILD -> Running 'build-job'...")
        cmd = ["node", "build_site.js"]
        res = subprocess.run(cmd, cwd=self.project_dir, capture_output=True, text=True)
        build_dir = os.path.join(self.project_dir, "build")
        if res.returncode == 0 and os.path.exists(build_dir):
            print(f"   [SUCCESS] Build artifacts created at: {build_dir}")
            return True
        print(f"   [FAILED] Build failed: {res.stderr}")
        return False

    def run_security_gate_job(self):
        print("[*] Stage: SECURITY -> Running 'security-gate'...")
        from security_gate import DevSecOpsGate
        gate = DevSecOpsGate(self.project_dir)
        report = gate.run_all()
        if report["status"] == "PASSED":
            print(f"   [SUCCESS] Security Gate passed: 0 secrets leaked, {report['dependencies_checked']} deps checked.")
            return True
        print(f"   [FAILED] Security Gate failed: {len(report['findings'])} issues found.")
        return False

    def run_pages_deploy_job(self):
        print("[*] Stage: DEPLOY -> Running 'pages'...")
        build_dir = os.path.join(self.project_dir, "build")
        public_dir = os.path.join(self.project_dir, "public")
        os.makedirs(public_dir, exist_ok=True)
        for item in os.listdir(build_dir):
            s = os.path.join(build_dir, item)
            d = os.path.join(public_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        index_file = os.path.join(public_dir, "index.html")
        if os.path.exists(index_file):
            print(f"   [SUCCESS] GitLab Pages deployed at: {public_dir}")
            return True
        return False

    def run_full_pipeline(self):
        print("==================================================")
        print(" Running Complex Docusaurus DevSecOps Pipeline")
        print(" Target: GitLab Pages & Security Gates")
        print("==================================================")
        if not self.run_build_job():
            return False
        if not self.run_security_gate_job():
            return False
        if not self.run_pages_deploy_job():
            return False
        print("==================================================")
        print(" PIPELINE SUCCEEDED: GitLab Pages Ready to Access!")
        print(" URL: https://NguyenNhatLam.gitlab.io/my-pipeline-tutorial-project/")
        print("==================================================")
        return True

if __name__ == "__main__":
    sim = ComplexPipelineSimulator()
    sim.run_full_pipeline()
