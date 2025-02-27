import os
import json
import csv
from loguru import logger
from collections import defaultdict

ALLOWED_EXTENSIONS = {".log", ".csv", ".json"}
BASE_DIRECTORY = "/home/kali/M05_Project/Logan/Log_Samples"

def analyze_log_file(log_file_path):
    if not is_valid_file(log_file_path):
        return None, None, None

    log_counts = {}
    error_events = []
    critical_events = []

    with open(log_file_path, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 4:
                timestamp, level, module, message = parts
                if level not in log_counts:
                    log_counts[level] = 0
                log_counts[level] += 1
                if level == "ERROR":
                    error_events.append(line)
                elif level == "CRITICAL":
                    critical_events.append(line)
    
    return log_counts, error_events, critical_events 

def read_log_file(log_file):
    if not is_valid_file(log_file):
        return []

    log_data = []
    try:
        with open(log_file, "r") as file:
            log_data = file.readlines()
    except FileNotFoundError:
        logger.error(f"File not found: {log_file}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return log_data

def read_csv_file(csv_file):
    if not is_valid_file(csv_file):
        return []

    log_data = []
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                log_data.append(" | ".join(row))
    except FileNotFoundError:
        logger.error(f"File not found: {csv_file}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return log_data

def read_json_file(json_file):
    if not is_valid_file(json_file):
        return []

    log_data = []
    try:
        with open(json_file, "r") as file:
            log_entries = json.load(file)
            for entry in log_entries:
                log_data.append(f"{entry['timestamp']} | {entry['level']} | {entry['module']} | {entry['message']}")
    except FileNotFoundError:
        logger.error(f"File not found: {json_file}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return log_data

def is_valid_file(file_path):
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return False

    if not os.path.isfile(file_path):
        logger.error(f"Not a file: {file_path}")
        return False

    _, ext = os.path.splitext(file_path)
    if ext.lower() not in ALLOWED_EXTENSIONS:
        logger.error(f"Invalid file extension: {ext}")
        return False

    if os.path.getsize(file_path) == 0:
        logger.error(f"File is empty: {file_path}")
        return False

    try:
        with open(file_path, "r") as file:
            file.read()
    except Exception as e:
        logger.error(f"Cannot read file: {file_path}, error: {e}")
        return False

    return True