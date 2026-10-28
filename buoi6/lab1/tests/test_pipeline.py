import unittest
import os
import sys

# Ensure lab1 directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pipeline_runner import PipelineRunner

class TestGitLabCIPipeline(unittest.TestCase):
    def setUp(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', '.gitlab-ci.yml')
        self.runner = PipelineRunner(config_path)

    def test_stages_defined(self):
        stages = self.runner.config.get("stages", [])
        self.assertEqual(stages, ["build", "test", "deploy"])

    def test_jobs_exist(self):
        expected_jobs = ["build-job", "test-job1", "test-job2", "deploy-prod"]
        for job in expected_jobs:
            self.assertIn(job, self.runner.config)
            self.assertIn("stage", self.runner.config[job])
            self.assertIn("script", self.runner.config[job])

    def test_job_stages_mapping(self):
        self.assertEqual(self.runner.config["build-job"]["stage"], "build")
        self.assertEqual(self.runner.config["test-job1"]["stage"], "test")
        self.assertEqual(self.runner.config["test-job2"]["stage"], "test")
        self.assertEqual(self.runner.config["deploy-prod"]["stage"], "deploy")

    def test_environment_configuration(self):
        deploy_job = self.runner.config["deploy-prod"]
        self.assertEqual(deploy_job.get("environment"), "production")

    def test_pipeline_execution_simulation(self):
        success = self.runner.run_pipeline()
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
