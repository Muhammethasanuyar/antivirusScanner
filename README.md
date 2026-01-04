# Antivirus Scanner

A lightweight, educational antivirus scanner written in Python. This tool performs file scanning using SHA-256 signature matching and heuristic analysis to detect potential threats.

## Features

- **Signature-based Detection**: Identifies known threats by comparing file hashes (SHA-256) against a local database (`signatures.json`).
- **Heuristic Analysis**: Detects suspicious files based on behavioral patterns and attributes:
    - **Double Extensions**: Flags files like `document.pdf.exe`.
    - **Suspicious Extensions**: Alerts on potentially dangerous file types (e.g., `.bat`, `.scr`, `.vbs`).
    - **Suspicious Strings**: Scans file content for keywords often associated with malware (e.g., `powershell`, `/bin/sh`).
- **Detailed Reporting**: Generates a comprehensive JSON report containing scan statistics, detected threats, and suspicious files with reasons.
- **CLI Interface**: Simple command-line interface for easy integration and usage.

## Installation

No external dependencies are required. The project uses the Python standard library.

1.  Clone the repository:
    ```bash
    git clone git@github.com:Muhammethasanuyar/antivirusScanner.git
    cd antivirusScanner
    ```

2.  Ensure you have Python 3.x installed.

## Usage

Run the scanner from the root directory of the project using the following command:

```bash
python -m src.app --path <directory_to_scan> --out <output_report_path> [options]
```

### Arguments

- `--path`: (Required) The directory path to scan.
- `--out`: (Required) The path where the JSON report will be saved.
- `--signatures`: (Optional) Path to the signature database file. Defaults to `data/signatures.json`.

### Example

To scan the `samples` directory and save the report to `output/report.json`:

```bash
python -m src.app --path samples --out output/report.json
```

## Project Structure

```
.
├── data/
│   └── signatures.json    # Database of known malware SHA-256 hashes
├── src/
│   ├── app.py             # Main entry point and CLI handler
│   ├── scanner.py         # Core scanning logic (file traversal, orchestration)
│   ├── hasher.py          # SHA-256 hash calculation utility
│   ├── signatures.py      # Signature loading and matching logic
│   ├── rules.py           # Heuristic analysis rules
│   └── report.py          # JSON report generation
├── samples/               # Directory for testing with sample files
├── output/                # Directory for scan reports
└── README.md              # Project documentation
```

## Output Format

The generated JSON report includes:
- **Scan Information**: Path scanned, timestamp (implied).
- **Statistics**: Total files scanned, number of clean files, detections.
- **Detections**: A list of detected or suspicious files with:
    - File path
    - SHA-256 hash
    - Status (`DETECTED` or `SUSPICIOUS`)
    - Threat score
    - specific reasons for detection

## Disclaimer

**Educational Use Only**: This tool is designed for educational purposes to demonstrate the concepts of file scanning and malware detection. It is **not** a substitute for commercial antivirus software and does not provide real-time protection or remediation/removal capabilities. Use with caution when handling real malware samples.
