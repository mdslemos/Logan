from loguru import logger
import random
import time
from datetime import datetime

usernames = ["Joaquim", "Bruno", "Carla", "admin", "Joana", "Pedro", "Ana", "Maria", "Tiago", "Rui"]
ip_addresses = ["192.168.1.1", "10.0.0.2", "172.16.0.3", "203.0.113.4", "198.51.100.5", "198.168.1.98", "172.16.0.12"]
malware_types = ["Trojan", "Ransomware", "Worm", "Spyware", "Adware"]
actions = ["Successful Login", "File Access", "Port Scan Detected", "Failed Login", "Malware Detected"]
weights = [0.50, 0.20, 0.15, 0.10, 0.05]

def setup_logger(log_file_path, log_file_name=None):
    if log_file_name is None:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file_name = f"{log_file_path}/log_{current_time}.log"
    if logger._core.handlers:
        logger.remove(0)
    logger.add(log_file_name, format="{time:DD-MM-YYYY HH:mm:ss:SSS} | {level} | {module} | {message}", level="INFO")
    return log_file_name

def generate_log():
    action = random.choices(actions, weights=weights, k=1)[0]
    username = random.choice(usernames)
    ip = random.choice(ip_addresses)

    if action == "Successful Login":
        logger.info(f"Successful login for user '{username}' from IP {ip}")
    elif action == "File Access":
        log_file = f"/var/log/{random.choice(['auth', 'syslog', 'secure'])}.log"
        logger.warning(f"File access: User '{username}' accessed {log_file}")
    elif action == "Port Scan Detected":
        logger.warning(f"Port scan detected from IP {ip} targeting sensitive ports")
    elif action == "Failed Login":
        logger.error(f"Failed login attempt for user '{username}' from IP {ip}")
    elif action == "Malware Detected":
        malware = random.choice(malware_types)
        logger.critical(f"Malware detected! Type: {malware}, User: '{username}', IP: {ip}")

def simulate_soc_logs(event_count, log_file_path, log_file_name=None):
    log_file_name = setup_logger(log_file_path, log_file_name)  # Set up the logger when generating logs
    for i in range(event_count):
        generate_log()
        delay = random.uniform(1, 5)  # Generate a random delay between 1 and 5 seconds
        time.sleep(delay)  # Simulate some delay between log events
    return log_file_name