import os
import sys

# Add the Modules directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modules')))

# Import necessary modules from the Modules directory
from mod_generator import generate_log_file
from mod_analyzer import analyze_log_file, is_valid_file
from mod_converter import convert_to_csv, convert_to_json
from mod_reporter import generate_overall_report, generate_failed_login_report, generate_malware_report

def list_log_files(log_file_path):
    """List available log files in the specified directory."""
    log_files = [f for f in os.listdir(log_file_path) if f.startswith("log_") and f.endswith(".log")]
    if not log_files:
        print("")
        print("No log files found.")
        return []
    log_files = sorted(log_files)  # Sort the log files in alphabetical order
    print("")
    print("Available log files:")
    for idx, log_file in enumerate(log_files, start=1):
        print(f"{idx}. {log_file}")
    return log_files

def select_log_file(log_files):
    """Prompt the user to select a log file from the list."""
    while True:
        try:
            file_choice = int(input("Enter the number of the log file: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 1 <= file_choice <= len(log_files):
            selected_log_file = log_files[file_choice - 1]
            print("")
            print(f"Selected log file: {selected_log_file}")
            return selected_log_file
        else:
            print("Invalid choice. Please select a valid option.")

def get_first_and_last_entry_times(log_file_path):
    """Get the first and last entry times from the log file."""
    with open(log_file_path, "r") as file:
        lines = file.readlines()
        if not lines:
            return None, None
        first_entry = lines[0].split(" | ")[0]
        last_entry = lines[-1].split(" | ")[0]
        return first_entry, last_entry

def generate_log_file_menu():
    """Generate a new log file with simulated log events."""
    while True:
        print("")
        print("Generate Log File")
        print("=================")
        print("1. Generate new log file")
        print("2. Return to main menu")
        print("")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            log_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'Logs')
            try:
                event_count = int(input("Enter the number of events to generate: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            log_file_name = generate_log_file(event_count, log_file_path)
            print(f"Generated {event_count} log events in {log_file_name}")
        elif choice == 2:
            return
        else:
            print("Invalid choice. Please select a valid option.")

def analyze_log_file_menu():
    """Analyze a selected log file."""
    while True:
        print("")
        print("Analyze Log File")
        print("================")
        print("1. Choose log file to analyze")
        print("2. Return to main menu")
        print("")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            log_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'Logs')
            log_files = list_log_files(log_file_path)
            if log_files:
                selected_log_file = select_log_file(log_files)
                if selected_log_file:
                    analyze_selected_log_file(log_file_path, selected_log_file)
        elif choice == 2:
            return
        else:
            print("Invalid choice. Please select a valid option.")

def analyze_selected_log_file(log_file_path, selected_log_file):
    """Analyze the selected log file and display the results."""
    log_counts, error_events, critical_events = analyze_log_file(os.path.join(log_file_path, selected_log_file))
    if log_counts is not None:
        print(f"Log analysis complete.")
        if is_valid_file(os.path.join(log_file_path, selected_log_file)):
            print(f"The log file is valid and has no errors.")
        first_entry, last_entry = get_first_and_last_entry_times(os.path.join(log_file_path, selected_log_file))
        if first_entry and last_entry:
            print(f"First entry time: {first_entry}")
            print(f"Last entry time: {last_entry}")
        total_events = sum(log_counts.values())
        print(f"Total events in the log: {total_events}")
        print(f"Distribution of events by level: {log_counts}")
    else:
        print("Invalid log file. Analysis aborted.")

def convert_log_file_menu():
    """Convert a selected log file to CSV, JSON, or both formats."""
    while True:
        print("")
        print("Convert Log File")
        print("================")
        print("1. Convert log file to CSV")
        print("2. Convert log file to JSON")
        print("3. Convert log file to CSV and JSON")
        print("4. Return to main menu")
        print("")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice in [1, 2, 3]:
            log_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'Logs')
            log_files = list_log_files(log_file_path)
            if log_files:
                selected_log_file = select_log_file(log_files)
                if selected_log_file:
                    convert_selected_log_file(log_file_path, selected_log_file, choice)
        elif choice == 4:
            return
        else:
            print("Invalid choice. Please select a valid option.")

def convert_selected_log_file(log_file_path, selected_log_file, choice):
    """Convert the selected log file based on the user's choice."""
    if choice == 1:
        convert_to_format(log_file_path, selected_log_file, 'CSV')
    elif choice == 2:
        convert_to_format(log_file_path, selected_log_file, 'JSON')
    elif choice == 3:
        convert_to_format(log_file_path, selected_log_file, 'CSV')
        convert_to_format(log_file_path, selected_log_file, 'JSON')

def convert_to_format(log_file_path, selected_log_file, format):
    """Convert the selected log file to the specified format."""
    if format == 'CSV':
        csv_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'CSV')
        os.makedirs(csv_file_path, exist_ok=True)
        csv_file = os.path.join(csv_file_path, selected_log_file.replace(".log", ".csv"))
        convert_to_csv(os.path.join(log_file_path, selected_log_file), csv_file)
        print(f"Log data successfully converted to CSV: {csv_file}")
    elif format == 'JSON':
        json_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'JSON')
        os.makedirs(json_file_path, exist_ok=True)
        json_file = os.path.join(json_file_path, selected_log_file.replace(".log", ".json"))
        convert_to_json(os.path.join(log_file_path, selected_log_file), json_file)
        print(f"Log data successfully converted to JSON: {json_file}")

def generate_report_menu():
    """Generate a report based on the user's choice."""
    while True:
        print("")
        print("Generate Report")
        print("===============")
        print("1. Generate overall report")
        print("2. Generate malware report")
        print("3. Generate failed login attempts report")
        print("4. Return to main menu")
        print("")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice in [1, 2, 3]:
            log_file_path = os.path.join(os.path.dirname(__file__), 'Output', 'Logs')
            log_files = list_log_files(log_file_path)
            if log_files:
                selected_log_file = select_log_file(log_files)
                if selected_log_file:
                    generate_selected_report(log_file_path, selected_log_file, choice)
        elif choice == 4:
            return
        else:
            print("Invalid choice. Please select a valid option.")

def generate_selected_report(log_file_path, selected_log_file, choice):
    """Generate the selected report based on the user's choice."""
    log_file_full_path = os.path.join(log_file_path, selected_log_file)
    first_entry, last_entry = get_first_and_last_entry_times(log_file_full_path)
    if choice == 1:
        # Generate overall report
        result = analyze_log_file(log_file_full_path)
        if result is not None:
            log_counts, error_events, critical_events = result  # Extract log_counts, error_events, and critical_events from the result
            report_dir = os.path.join(os.path.dirname(__file__), 'Output', 'Reports')
            os.makedirs(report_dir, exist_ok=True)
            report_file_path = os.path.join(report_dir, selected_log_file.replace(".log", "_overall_report.txt"))
            report = generate_overall_report(log_counts, report_file_path, first_entry, last_entry, critical_events, error_events, selected_log_file)
            print(report)
        else:
            print("Invalid log file. Report generation aborted.")
    elif choice == 2:
        # Generate malware report
        with open(log_file_full_path, "r") as file:
            log_entries = file.readlines()
        report_dir = os.path.join(os.path.dirname(__file__), 'Output', 'Reports')
        os.makedirs(report_dir, exist_ok=True)
        report_file_path = os.path.join(report_dir, selected_log_file.replace(".log", "_malware_report.txt"))
        report = generate_malware_report(log_entries, report_file_path, first_entry, last_entry, selected_log_file)
        print(report)
    elif choice == 3:
        # Generate failed login attempts report
        with open(log_file_full_path, "r") as file:
            log_entries = file.readlines()
        report_dir = os.path.join(os.path.dirname(__file__), 'Output', 'Reports')
        os.makedirs(report_dir, exist_ok=True)
        report_file_path = os.path.join(report_dir, selected_log_file.replace(".log", "_failed_login_report.txt"))
        report = generate_failed_login_report(log_entries, report_file_path, selected_log_file)
        print(report)

def main():
    """Main entry point of the program."""
    print("")
    print("===========================")
    print("| Logan: The Log Analyzer |")
    print("===========================")
    print("")
    print("This tool generates simulated log events for testing log analysis scripts.")
    print("")

def menu():
    """Display the main menu and handle user input."""
    while True:
        print("")
        print("Main Menu")
        print("=========")
        print("1. Generate log file")
        print("2. Analyze log file")
        print("3. Convert log file")
        print("4. Generate report")
        print("5. Exit")
        print("")
        try:
            choice_number = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice_number == 1:
            generate_log_file_menu()
        elif choice_number == 2:
            analyze_log_file_menu()
        elif choice_number == 3:
            convert_log_file_menu()
        elif choice_number == 4:
            generate_report_menu()
        elif choice_number == 5:
            print("")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    menu()