# Logical Backup Tool for iOS Forensics

![2024-06-16_162459](https://github.com/DRCRecoveryData/Logical-Backup-Tool/assets/85211068/0b3471fc-b5b4-4a8a-8fe8-6885daea36ab)

## Overview
This tool provides a graphical interface (GUI) application built with PyQt6 and Python, designed to facilitate logical backups of iOS devices. It supports various commands to backup, list files, retrieve backup information, set encryption, and list connected devices using `pymobiledevice3`.

## Features
- **Backup**: Create full backups of iOS devices to a specified directory and compress them into ZIP archives.
- **List Files**: List files contained within a specified backup directory.
- **Backup Info**: Print information about a specified backup directory.
- **Encryption**: Set encryption state for backups with optional password protection.
- **List Devices**: List iOS devices currently connected via USB.

## Requirements
- **Python**: Version 3.6 or higher
- **Dependencies**:
  - PyQt6
  - py7zr
  - colorama

Install dependencies using pip:
```bash
pip install PyQt6 py7zr colorama
```

## Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/DRCRecoveryData/Logical-Backup-Tool.git
   cd Logical-Backup-Tool
   ```

2. **Run the application**:
   ```bash
   python logicalbackuptool-gui.py
   ```
   This will launch the GUI application where you can perform various operations.

3. **Select an option** from the dropdown menu (`backup`, `list`, `info`, `encryption`, `list-devices`).

4. **Specify the Backup Directory**:
   - Click on **Browse** to select the directory where backups should be stored.

5. **Click Apply** to execute the selected command.

6. **Monitor Progress**:
   - The progress of operations (e.g., backup) will be displayed in the progress bar and log area.
   - Upon completion, a popup will notify you of the backup status.

## Notes
- Ensure `pymobiledevice3` is installed and accessible in your system's PATH for proper functionality of commands.
- This tool supports logical backups; for physical extractions, refer to dedicated forensic tools.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## Download
```https://drive.google.com/file/d/1JWmwYxoVidjMTdjvxplWtQJ_bYzlD444/view?usp=sharing```

Password: 123

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
