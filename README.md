# Logan: The Log Analyzer

Logan is a tool for generating, analyzing, converting, and reporting on log files.

## Installation and Running

1. Clone the repository:
   ```bash
   git clone https://github.com/mdslemos/logan.git
   cd logan
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. To run the program, use the following command:
   ```bash
   python main.py
   ```

## Usage

Logan allows you to perform 4 types of actions:

1. Generate log files

In this module, the user can define the number of events to be generated in the log file. 

Each event is described by the following fields: timestamp, level of importance, module that generated the entry and message.

The log files are writen to a fixed location: /Outputs/Logs

2. Analyze log files

This module performs some analysis function on a given log file. This can be used to verify the validity of the file and get some information as: time period covered by the log file, total number of events in the log file and their distribution by level of importance.

The results of the analysis are printed in the terminal.

3. Convert log files into CSV and/or JSON formats

With this module, the user may choose an existent log file and convert it to CSV and/or JSON, allowing the import of data to other platforms.

Each converted file is written to the location Output/CSV or Output/JSON, accordingly.

4. Generate reports from the log files

This module allows the user to choose a log file and generate three types of reports from it:

- Overall report;
- Malware report;
- Failed login attempts report.

Each report is printed in the terminal and written in a .txt file located in Output/Reports.

## Output folder

The output folder already has some sample files to be explored, in case the user doesn't want to generate new log files.