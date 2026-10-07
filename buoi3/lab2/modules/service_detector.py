import subprocess
import logging
import os
import shutil
from datetime import datetime

logging.basicConfig(filename='netrecon.log', level=logging.INFO)

def log(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"[{now}] {msg}")

def get_nmap_bin():
    found = shutil.which("nmap")
    if found:
        return found
    candidates = [
        os.path.expanduser(r"~\nmap_bin\nmap-7.92\nmap.exe"),
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        r"C:\Program Files\Nmap\nmap.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "nmap"

def detect_service(ip, ports):
    ports_str = ','.join(str(p) for p in ports)
    nmap_bin = get_nmap_bin()
    cmd = [nmap_bin, "-sV", "-p", ports_str, ip]
    log(f"Running service detection on {ip}:{ports_str}")
    try:
        result = subprocess.check_output(cmd).decode(errors='ignore')
        log(result)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode(errors='ignore') if e.output else str(e)}"
    except Exception as e:
        return f"Error: {e}"
