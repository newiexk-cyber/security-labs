import unittest
import os
import sys
import json
import yaml

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pipeline_simulator import ComplexPipelineSimulator
from security_gate import DevSecOpsGate

class TestDocusaurusPipeline(unittest.TestCase):
    def setUp(self):
        self.project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.sim = ComplexPipelineSimulator(self.project_dir)

    def test_gitlab_ci_configuration(self):
        ci_path = os.path.join(self.project_dir, ".gitlab-ci.yml")
        self.assertTrue(os.path.exists(ci_path))
        with open(ci_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        self.assertIn("stages", config)
        self.assertIn("build", config["stages"])
        self.assertIn("deploy", config["stages"])
        self.assertIn("build-job", config)
        self.assertIn("pages", config)
        self.assertEqual(config["pages"]["stage"], "deploy")

    def test_docusaurus_config_url(self):
        cfg_path = os.path.join(self.project_dir, "docusaurus.config.js")
        with open(cfg_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("NguyenNhatLam.gitlab.io", content)
        self.assertIn("/my-pipeline-tutorial-project/", content)

    def test_security_gate_scan(self):
        gate = DevSecOpsGate(self.project_dir)
        report = gate.run_all()
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["secrets_found"], 0)
        self.assertGreater(report["dependencies_checked"], 0)

    def test_full_pipeline_build_and_deploy(self):
        success = self.sim.run_full_pipeline()
        self.assertTrue(success)
        public_index = os.path.join(self.project_dir, "public", "index.html")
        self.assertTrue(os.path.exists(public_index))

if __name__ == '__main__':
    unittest.main()
