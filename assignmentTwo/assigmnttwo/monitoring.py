import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0
LOG_FILE = "system_health.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"CPU usage is high: {cpu_usage}%"
        logging.warning(message)
        print(message)

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        message = f"Memory usage is high: {memory_usage}%"
        logging.warning(message)
        print(message)

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        message = f"Disk space usage is high: {disk_usage}%"
        logging.warning(message)
        print(message)

def check_top_processes():
    processes = [(p.pid, p.name(), p.cpu_percent(interval=1)) for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    high_cpu_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    if high_cpu_processes:
        message = "Top CPU consuming processes:\n" + "\n".join([f"PID: {pid}, Name: {name}, CPU: {cpu}%" for pid, name, cpu in high_cpu_processes])
        logging.info(message)
        print(message)

    high_memory_processes = sorted(processes, key=lambda x: x[2] / psutil.virtual_memory().total * 100, reverse=True)[:5]
    if high_memory_processes:
        message = "Top memory consuming processes:\n" + "\n".join([f"PID: {pid}, Name: {name}, Memory: {cpu / psutil.virtual_memory().total * 100}%" for pid, name, cpu in high_memory_processes])
        logging.info(message)
        print(message)

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_top_processes()
