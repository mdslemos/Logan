import csv
import json
from loguru import logger

def read_csv_file(csv_file):
    log_data = []
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                log_data.append(','.join(row))
    except FileNotFoundError:
        logger.error(f"File not found: {csv_file}")
    except Exception as e:
        logger.error(f"An error occurred while reading the CSV file: {e}")
    return log_data

def read_json_file(json_file):
    log_data = []
    try:
        with open(json_file, "r") as file:
            json_reader = json.load(file)
            for log_entry in json_reader:
                log_data.append(f"{log_entry['timestamp']} | {log_entry['level']} | {log_entry['module']} | {log_entry['message']}")
    except FileNotFoundError:
        logger.error(f"File not found: {json_file}")
    except Exception as e:
        logger.error(f"An error occurred while reading the JSON file: {e}")
    return log_data

def convert_to_csv(log_file_path, csv_file_path):
    with open(log_file_path, 'r') as log_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header row to the CSV file
        csv_writer.writerow(["timestamp", "level", "module", "message"])
        for line in log_file:
            # Parse the log line here (this is a simplified example)
            log_parts = line.strip().split(" | ")
            csv_writer.writerow(log_parts)

def convert_to_json(log_file_path, json_file_path):
    logs = []
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            log_parts = line.strip().split(" | ")
            log_entry = {
                "timestamp": log_parts[0],
                "level": log_parts[1],
                "module": log_parts[2],
                "message": log_parts[3]
            }
            logs.append(log_entry)
    with open(json_file_path, 'w') as json_file:
        json.dump(logs, json_file, indent=4)