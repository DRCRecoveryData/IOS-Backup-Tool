# IOS Backup Tool for IOS Forensics

![222](https://github.com/DRCRecoveryData/IOS-Backup-Tool/assets/85211068/f40f8112-eccc-428a-8ce7-1c6c5c7b4df8)


## Overview
This tool provides a graphical interface (GUI) application built with PyQt6 and Python, designed to facilitate logical backups of iOS devices. It supports various commands to backup, list files, retrieve backup information, set encryption, and list connected devices using `pymobiledevice3`.

## Features
- **Backup**: Create full backups of iOS devices to a specified directory and compress them into ZIP archives.
- **List Devices**: List iOS devices currently connected via USB.

## Requirements
- **Python**: Version 3.6 or higher
- **Dependencies**:
  - PyQt6
  - py7zr
  - pymobiledevice3

Install dependencies using pip:
```bash
pip install PyQt6 py7zr pymobiledevice3
```

## Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/DRCRecoveryData/Logical-Backup-Tool.git
   cd Logical-Backup-Tool
   ```

2. **Run the application**:
   ```bash
   python iosbackuptool-gui.py
   ```
   This will launch the GUI application where you can perform various operations.

3. **Select an option** from the dropdown menu (`backup`, `list-devices`).

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
