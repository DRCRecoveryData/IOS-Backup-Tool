# 🍏 iOS Logical Backup Tool for Forensics

**A powerful, GUI-based utility for creating logical backups of iOS devices, essential for digital forensics and data recovery.**

<img width="552" height="678" alt="image" src="https://github.com/user-attachments/assets/a6b58339-1574-4353-8d19-ec6dc0439171" />

| Status & License | | |
| :--- | :--- | :--- |
| ![Build Status](https://img.shields.io/github/actions/workflow/status/DRCRecoveryData/IOS-Backup-Tool/build.yml) | ![License](https://img.shields.io/github/license/DRCRecoveryData/IOS-Backup-Tool) | ![Version](https://img.shields.io/github/v/release/DRCRecoveryData/IOS-Backup-Tool) |

---

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Notes for Forensics](#notes-for-forensics)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 💡 Overview

The **iOS Logical Backup Tool** is a dedicated **Graphical User Interface (GUI)** application, built using **PyQt6** and **Python**, designed to streamline the process of acquiring logical backups from iOS devices. Leveraging the power of `pymobiledevice3`, this tool is tailored for professionals in **digital forensics** and **data recovery** who require reliable and reproducible acquisition workflows.

---

## ✨ Features

This tool offers a straightforward, step-by-step interface for critical acquisition tasks:

* **Logical Backup Acquisition**: Create full, standard logical backups of connected iOS devices.
* **Archiving**: Automatically compress generated backups into **ZIP archives** for efficient storage and transfer.
* **Device Management**: Easily **list all currently connected iOS devices** via USB.
* **Intuitive GUI**: A user-friendly interface simplifies the complex command-line processes into a few clicks.

---

## ⚙️ Requirements

### Software Dependencies

Ensure you have the following installed on your system:

* **Python**: Version 3.6 or higher.

### Python Libraries

The tool relies on these essential Python packages:

* **PyQt6**: For the robust Graphical User Interface.
* **py7zr**: For handling compression and archiving of the backup data.
* **pymobiledevice3**: The core library facilitating communication and data acquisition from iOS devices.

Install all required libraries easily via `pip`:
```bash
pip install PyQt6 py7zr pymobiledevice3
````

-----

## ⬇️ Installation

### Method 1: Installing from Source

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/DRCRecoveryData/IOS-Backup-Tool.git](https://github.com/DRCRecoveryData/IOS-Backup-Tool.git)
    cd IOS-Backup-Tool
    ```

2.  **Install Dependencies:**
    It is highly recommended to install dependencies from the provided `requirements.txt` file:

    ```sh
    pip install -r requirements.txt
    ```

### Method 2: Using a Pre-built Release

1.  Download the latest executable release from the [releases page](https://github.com/DRCRecoveryData/IOS-Backup-Tool/releases).
2.  Extract the downloaded archive to your preferred working directory.
3.  Execute the application file directly (e.g., `iosbackuptool.exe` on Windows).

-----

## 🚀 Usage

1.  **Launch the Application:**
    If running from source, execute the main script:

    ```bash
    python iosbackuptool-gui.py
    ```

2.  **Connect Device:** Connect the target iOS device to your computer via USB.

3.  **Select Operation:**

      * Use the dropdown menu to select your desired operation (e.g., `backup`, `list-devices`).

4.  **Specify Output Directory (for Backup):**

      * Click the **Browse** button and select the directory where you want the final backup archive to be saved.

5.  **Execute Command:**

      * Click **Apply** to begin the selected process.

6.  **Monitor Status:**

      * Observe the progress in the log area and the progress bar. A notification popup will confirm successful completion.

-----

## ⚠️ Notes for Forensics

  * **Logical vs. Physical:** This tool performs **logical backups** which extract user-generated data that the operating system allows access to. For a full **physical file system extraction**, you must use specialized tools and techniques (often requiring jailbreaking or hardware exploits).
  * **PATH Variable:** Ensure the necessary components of `pymobiledevice3` are properly installed and accessible via your system's **PATH** environment variable for all commands to function correctly.

-----

## 🤝 Contributing

We welcome contributions from the community\! If you have suggestions for features, bug fixes, or improvements:

1.  **Fork** the repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

For bug reports or questions, please open an **Issue** on GitHub.

-----

## ⚖️ License

This project is distributed under the **MIT License**. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for full details.

-----

## ✉️ Contact

For support, inquiries, or partnership opportunities, please reach out:

  * **Email**: [hanaloginstruments@gmail.com](mailto:hanaloginstruments@gmail.com)
