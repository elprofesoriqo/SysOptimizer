import psutil

def optimize_memory():
    """
    Zamyka procesy zużywające nadmiar pamięci RAM.
    """
    high_memory_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        if proc.info['memory_info'].rss > 500 * 1024 * 1024:  # Procesy używające >500MB RAM
            proc.terminate()
            high_memory_processes.append(proc.info)
    return high_memory_processes

def optimize_cpu():
    """
    Zamyka procesy zużywające nadmiar CPU.
    """
    high_cpu_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if proc.info['cpu_percent'] > 80:  # Procesy używające >80% CPU
            proc.terminate()
            high_cpu_processes.append(proc.info)
    return high_cpu_processes


import subprocess
import json

def monitor_processes():
    try:
        subprocess.run(["modules/sys_monitor.exe"], check=True)
        with open("processes.json", "r") as file:
            result = json.load(file)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
