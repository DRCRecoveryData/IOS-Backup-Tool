# IOS Backup Tool for IOS Forensics

![222](https://github.com/DRCRecoveryData/IOS-Backup-Tool/assets/85211068/f40f8112-eccc-428a-8ce7-1c6c5c7b4df8)

![Build Status](https://img.shields.io/github/actions/workflow/status/DRCRecoveryData/IOS-Backup-Tool/build.yml)
![License](https://img.shields.io/github/license/DRCRecoveryData/IOS-Backup-Tool)
![Version](https://img.shields.io/github/v/release/DRCRecoveryData/IOS-Backup-Tool)

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)
- [Contact](#contact)

## Overview

This tool provides a graphical interface (GUI) application built with PyQt6 and Python, designed to facilitate logical backups of iOS devices. It supports various commands to backup, list files, and restore data.

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

## Installation

To install the IOS Backup Tool:

1. Download the latest release from the [releases page](https://github.com/DRCRecoveryData/IOS-Backup-Tool/releases).
2. Extract the contents to a directory.
3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DRCRecoveryData/IOS-Backup-Tool.git
    cd IOS-Backup-Tool
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

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

For issues or suggestions, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [Python Programming Language](https://www.python.org/)
- [PyQt6 Library](https://pypi.org/project/PyQt6/)

## Contact

For support or questions, please contact us at [hanaloginstruments@gmail.com](mailto:hanaloginstruments@gmail.com)
