# Forensic File Integrity Monitor

## 🛡️ Project Overview
This project is a security utility designed for **Forensic File Integrity Monitoring (FIM)**. It automates the detection of unauthorized file modifications by tracking SHA-256 cryptographic hashes over time. This tool is built to provide a reliable audit trail for sensitive files, ensuring data integrity for cybersecurity investigations.

## 🚀 Key Features
* **Continuous Monitoring Loop**: Features an interactive main loop that allows for repetitive file checking without restarting the application.
* **SHA-256 Hash Verification**: Calculates high-security cryptographic hashes to detect even single-bit changes in file content.
* **JSON Forensic Logging**: Automatically records timestamps, filenames, and hash values into a structured JSON log for long-term auditability.
* **Historical Comparison**: Retrieves and displays all previous hash values for a specific file, allowing users to visually identify exactly when a file was tampered with.
* **Robust Input Validation**: Built-in error handling manages invalid file paths and incorrect user inputs to ensure system stability.

## 🛠️ Technical Stack
* **Language**: Python 3.x.
* **Modules**:
    * `hashlib`: For SHA-256 hash generation.
    * `json`: For persistent data storage and log management.
    * `datetime`: For accurate forensic timestamping.

## 📂 Usage
1. Run the script: `python file_monitor.py`.
2. Enter the full path of the file you wish to monitor.
3. The system will display the current hash and compare it against historical records.
4. Enter `e` or `exit` to safely terminate the session.# Forensic-File-Integrity-Monitor
