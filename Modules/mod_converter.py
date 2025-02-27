import csv
import json
from loguru import logger

def convert_to_csv(log_file_path, csv_file_path):
    """Convert a log file to CSV format."""
    with open(log_file_path, 'r') as log_file, open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header row to the CSV file
        csv_writer.writerow(["timestamp", "level", "module", "message"])
        for line in log_file:
            # Parse the log line here (this is a simplified example)
            log_parts = line.strip().split(" | ")
            csv_writer.writerow(log_parts)

def convert_to_json(log_file_path, json_file_path):
    """Convert a log file to JSON format."""
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