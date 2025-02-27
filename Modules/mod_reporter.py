def generate_overall_report(log_counts, output_file, first_entry_time, last_entry_time, critical_events, error_events, log_file_name):
    """Generate an overall report of the log analysis."""
    report_lines = []
    report_lines.append("Log Analysis Report")
    report_lines.append("===================")
    report_lines.append("")
    report_lines.append(f"Log File: {log_file_name}")
    report_lines.append("")
    report_lines.append("Summary:")
    report_lines.append("--------")
    total_logs = sum(log_counts.values())
    report_lines.append(f"Total Logs: {total_logs}")
    report_lines.append(f"First Entry Time: {first_entry_time}")
    report_lines.append(f"Last Entry Time: {last_entry_time}")
    report_lines.append("")
    report_lines.append("Detailed Log Counts:")
    report_lines.append("--------------------")
    for level, count in log_counts.items():
        report_lines.append(f"{level}: {count}")
    report_lines.append("")
    report_lines.append("Critical Events:")
    report_lines.append("----------------")
    for event in critical_events:
        report_lines.append(event)
    report_lines.append("")
    report_lines.append("Error Events:")
    report_lines.append("-------------")
    for event in error_events:
        report_lines.append(event)

    report_content = "\n".join(report_lines)
    with open(output_file, "w") as file:
        file.write(report_content)

    print(f"Report generated and saved to {output_file}")
    return report_content

def generate_failed_login_report(log_entries, output_file, log_file_name):
    """Generate a report of failed login attempts."""
    ip_counts = {}
    for entry in log_entries:
        if "failed login" in entry.lower():
            ip = entry.split(" ")[-1].strip()  # Assuming the IP is the last element in the log entry
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

    # Sort the IP addresses by the number of failed login attempts in descending order
    sorted_ip_counts = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

    report_lines = []
    report_lines.append("Failed Login Attempts Report")
    report_lines.append("============================")
    report_lines.append("")
    report_lines.append(f"Log File: {log_file_name}")
    report_lines.append("")
    report_lines.append(f"{'IP Address':<20} | {'Number of Failed Attempts':<25}")
    report_lines.append("-" * 47)
    for ip, count in sorted_ip_counts:
        report_lines.append(f"{ip:<20} | {count:<25}")

    report_content = "\n".join(report_lines)
    with open(output_file, "w") as file:
        file.write(report_content)

    print(f"Failed login report generated and saved to {output_file}")
    return report_content

def generate_malware_report(log_entries, output_file, first_entry_time, last_entry_time, log_file_name):
    """Generate a report of malware detections."""
    malware_dict = {}
    for entry in log_entries:
        if "malware detected" in entry.lower():
            parts = entry.split(" | ")
            malware_info = parts[-1].split(", ")
            malware_type = malware_info[0].split(": ")[1]
            ip = malware_info[-1].split(": ")[1]
            if malware_type not in malware_dict:
                malware_dict[malware_type] = []
            malware_dict[malware_type].append(ip)

    report_lines = []
    report_lines.append("Malware Detection Report")
    report_lines.append("========================")
    report_lines.append("")
    report_lines.append(f"Log File: {log_file_name}")
    report_lines.append("")
    report_lines.append(f"First Entry Time: {first_entry_time}")
    report_lines.append(f"Last Entry Time: {last_entry_time}")
    report_lines.append("")
    for malware_type, ips in malware_dict.items():
        report_lines.append(f"Malware Type: {malware_type} (Total IPs: {len(ips)})")
        report_lines.append("------------------------")
        for ip in ips:
            report_lines.append(ip)
        report_lines.append("")

    report_content = "\n".join(report_lines)
    with open(output_file, "w") as file:
        file.write(report_content)

    print(f"Malware report generated and saved to {output_file}")
    return report_content

if __name__ == "__main__":
    sample_log_counts = {
        "INFO": 50,
        "WARNING": 30,
        "ERROR": 10,
        "CRITICAL": 2
    }
    sample_first_entry_time = "2025-02-26 22:28:19"
    sample_last_entry_time = "2025-02-26 23:28:19"
    sample_critical_events = ["Critical event 1", "Critical event 2"]
    sample_error_events = ["Error event 1", "Error event 2", "Error event 3"]
    sample_log_file_name = "sample_log_file.log"
    report = generate_overall_report(sample_log_counts, "log_analysis_report.txt", sample_first_entry_time, sample_last_entry_time, sample_critical_events, sample_error_events, sample_log_file_name)
    print(report)

    sample_log_entries = [
        "2025-02-26 22:28:19 | INFO | User login successful | 192.168.1.1",
        "2025-02-26 22:30:19 | ERROR | Failed login attempt | 192.168.1.2",
        "2025-02-26 22:32:19 | ERROR | Failed login attempt | 192.168.1.2",
        "2025-02-26 22:34:19 | ERROR | Failed login attempt | 192.168.1.3",
        "2025-02-26 23:32:20:887 | CRITICAL | mod_generator | Malware detected! Type: Adware, User: 'Ana', IP: 172.16.0.3",
        "2025-02-26 23:32:20:887 | CRITICAL | mod_generator | Malware detected! Type: Spyware, User: 'Bruno', IP: 192.168.1.4"
    ]
    failed_login_report = generate_failed_login_report(sample_log_entries, "failed_login_report.txt", sample_log_file_name)
    print(failed_login_report)

    malware_report = generate_malware_report(sample_log_entries, "malware_report.txt", sample_first_entry_time, sample_last_entry_time, sample_log_file_name)
    print(malware_report)