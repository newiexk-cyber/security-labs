import subprocess
import tempfile
import os

class VirtualSandbox:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()

    def run_isolated(self, command):
        result = subprocess.run(command, cwd=self.temp_dir, capture_output=True, shell=True)
        return result.stdout.decode('utf-8', errors='ignore'), result.stderr.decode('utf-8', errors='ignore')
