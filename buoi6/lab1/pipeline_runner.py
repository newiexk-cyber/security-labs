import os
import sys
import yaml
import time
from concurrent.futures import ThreadPoolExecutor

class PipelineRunner:
    def __init__(self, config_path=".gitlab-ci.yml"):
        self.config_path = config_path
        self.config = self.load_config()
        self.env = {
            "GITLAB_USER_LOGIN": os.getenv("GITLAB_USER_LOGIN", "NguyenNhatLam"),
            "CI_COMMIT_BRANCH": os.getenv("CI_COMMIT_BRANCH", "main")
        }

    def load_config(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def execute_script_command(self, cmd):
        # Substitutes environment variables
        for k, v in self.env.items():
            cmd = cmd.replace(f"${k}", v).replace(f"${{{k}}}", v)
        if cmd.startswith("echo "):
            print(f"      [OUTPUT] {cmd[5:].strip('"')}")
            return True, cmd[5:].strip('"')
        elif cmd.startswith("sleep "):
            duration = float(cmd.split()[1])
            # Cap sleep to 1s in test runner for speed
            actual_sleep = min(duration, 0.5)
            time.sleep(actual_sleep)
            return True, f"slept {duration}s"
        return True, cmd

    def run_job(self, job_name, job_data):
        print(f"   -> Starting Job: {job_name} (Stage: {job_data.get('stage')})")
        start_time = time.time()
        for cmd in job_data.get("script", []):
            success, out = self.execute_script_command(cmd)
            if not success:
                print(f"      [ERROR] Command failed: {cmd}")
                return False
        elapsed = time.time() - start_time
        print(f"   [DONE] Job '{job_name}' completed in {elapsed:.2f}s")
        return True

    def run_pipeline(self):
        stages = self.config.get("stages", ["build", "test", "deploy"])
        print(f"==================================================")
        print(f" Running GitLab CI/CD Pipeline: {len(stages)} Stages")
        print(f" Triggered by: {self.env['GITLAB_USER_LOGIN']} | Branch: {self.env['CI_COMMIT_BRANCH']}")
        print(f"==================================================")

        for stage in stages:
            print(f"\n[*] STAGE: {stage.upper()}")
            stage_jobs = {
                name: data for name, data in self.config.items()
                if isinstance(data, dict) and data.get("stage") == stage
            }
            if not stage_jobs:
                continue

            with ThreadPoolExecutor(max_workers=max(1, len(stage_jobs))) as executor:
                futures = {
                    executor.submit(self.run_job, name, data): name
                    for name, data in stage_jobs.items()
                }
                for f in futures:
                    job_name = futures[f]
                    if not f.result():
                        print(f"Stage '{stage}' failed at job '{job_name}'!")
                        return False

        print(f"\n==================================================")
        print(f" PIPELINE SUCCEEDED: All stages passed!")
        print(f"==================================================")
        return True

if __name__ == "__main__":
    runner = PipelineRunner()
    runner.run_pipeline()
