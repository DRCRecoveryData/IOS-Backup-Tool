import sys
import os
import tempfile
import re
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QLineEdit, QFileDialog, QComboBox, QProgressBar, QPlainTextEdit, QMessageBox,
    QGroupBox, QSizePolicy
)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QFont

# Function to strip ANSI escape codes
def strip_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

# --- Worker Thread (Kept original logic) ---
class LogicalBackupWorker(QThread):
    progress_updated = pyqtSignal(int) 
    log_updated = pyqtSignal(str)
    backup_finished = pyqtSignal(str)

    def __init__(self, command, backup_directory=None):
        super().__init__()
        self.command = command
        self.backup_directory = backup_directory

    def run(self):
        try:
            self.execute_command(self.command)
        except Exception as e:
            self.log_updated.emit(f"Error: {e}")

    def execute_command(self, command):
        if command == 'backup':
            self.backup()
        elif command == 'list-devices':
            self.list_connected_devices()

    def backup(self):
        if not self.backup_directory:
            self.log_updated.emit("Backup directory not selected.")
            return

        self.log_updated.emit(f"[INFO] Starting full backup to: {self.backup_directory}...")

        try:
            process = subprocess.Popen(['pymobiledevice3', 'backup2', 'backup', '--full', self.backup_directory],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, 
                                        universal_newlines=True, encoding='utf-8')

            for line in process.stdout:
                self.log_updated.emit(strip_ansi_escape_codes(line.strip()))
                
            process.wait()
            
            if process.returncode != 0:
                self.log_updated.emit("[ERROR] Backup failed. Check log for details.")
            else:
                self.log_updated.emit("[SUCCESS] Backup completed successfully.")
                self.backup_finished.emit(f"Backup completed and saved to:\n\n{self.backup_directory}")
        
        except FileNotFoundError:
            self.log_updated.emit("[CRITICAL] Error: 'pymobiledevice3' command not found. Ensure it is installed and in your system PATH.")
        except Exception as e:
            self.log_updated.emit(f"[CRITICAL] An unexpected error occurred during backup: {e}")


    def list_connected_devices(self):
        self.log_updated.emit("[INFO] Listing connected devices...")
        try:
            process = subprocess.Popen(['pymobiledevice3', 'usbmux', 'list'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        universal_newlines=True)

            stdout, stderr = process.communicate()
            
            for line in stdout.splitlines():
                self.log_updated.emit(strip_ansi_escape_codes(line.strip()))

            if process.returncode != 0:
                self.log_updated.emit(f"[ERROR] Error listing connected devices: {stderr.strip()}")
            else:
                self.log_updated.emit("[SUCCESS] Device listing finished.")
        
        except FileNotFoundError:
             self.log_updated.emit("[CRITICAL] Error: 'pymobiledevice3' command not found. Ensure it is installed and in your system PATH.")
        except subprocess.CalledProcessError as e:
            self.log_updated.emit(f"[CRITICAL] Error listing connected devices: {e}")

# --- Modern GUI App (Text Changes Applied) ---
class LogicalBackupApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IOS Backup Tool") # Changed title
        self.setMinimumSize(550, 600)
        self.worker = None

        self.setup_ui()
        self.apply_modern_stylesheet()
        
        default_dir = os.path.join(os.path.expanduser('~'), '')
        self.backup_path_edit.setText(default_dir)

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # 1. Action Group (Dropdown and Execute Button)
        action_group = QGroupBox("Operation Selection") # Changed GroupBox title
        action_group.setObjectName("ActionGroup")
        action_layout = QVBoxLayout(action_group)
        
        # Command ComboBox
        self.command_combo = QComboBox()
        self.command_combo.addItem("Select an Operation...") # Changed dropdown text
        self.command_combo.addItem("Full Logical Backup", userData='backup') # Changed item text
        self.command_combo.addItem("List Connected Devices", userData='list-devices') # Changed item text
        self.command_combo.setCurrentIndex(0)
        self.command_combo.setMinimumHeight(35)
        action_layout.addWidget(self.command_combo)

        # Execute Button
        self.execute_button = QPushButton("Run Action") # Changed button text
        self.execute_button.setObjectName("AccentButton")
        self.execute_button.clicked.connect(self.execute_command)
        action_layout.addWidget(self.execute_button)
        
        main_layout.addWidget(action_group)
        
        # 2. Backup Directory Group
        backup_group = QGroupBox("Backup Destination Folder") # Changed GroupBox title
        backup_group.setObjectName("BackupGroup")
        backup_layout = QVBoxLayout(backup_group)
        
        # Directory Path Input and Browse Button
        path_h_layout = QHBoxLayout()
        self.backup_path_edit = QLineEdit()
        self.backup_path_edit.setPlaceholderText("Select or enter the path for your backup folder...") # Changed placeholder text
        
        self.browse_button = QPushButton("Browse...")
        self.browse_button.setObjectName("SecondaryButton")
        self.browse_button.clicked.connect(self.browse_backup_directory)
        self.browse_button.setFixedWidth(100)

        path_h_layout.addWidget(self.backup_path_edit)
        path_h_layout.addWidget(self.browse_button)
        backup_layout.addLayout(path_h_layout)

        main_layout.addWidget(backup_group)

        # 3. Progress Bar 
        progress_group = QGroupBox("Current Progress") # Changed GroupBox title
        progress_layout = QVBoxLayout(progress_group)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        progress_layout.addWidget(self.progress_bar)
        main_layout.addWidget(progress_group)

        # 4. Log Output
        log_group = QGroupBox("Real-time Command Output") # Changed GroupBox title
        log_group.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        log_layout = QVBoxLayout(log_group)
        self.log_box = QPlainTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setMinimumHeight(200)
        log_layout.addWidget(self.log_box)
        main_layout.addWidget(log_group)


    def apply_modern_stylesheet(self):
        # Professional Dark Theme (Kept from previous version)
        stylesheet = """
            QWidget {
                background-color: #2e3436; /* Dark slate gray */
                color: #ffffff;
                font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
                font-size: 10pt;
            }
            QGroupBox {
                font-size: 11pt;
                font-weight: bold;
                border: 1px solid #4e5a60;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 20px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                color: #6ab0e5; /* Light blue accent */
            }
            QLineEdit, QComboBox {
                background-color: #3c444a;
                border: 1px solid #5a646c;
                border-radius: 4px;
                padding: 8px;
                color: #ffffff;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #6ab0e5; /* Accent color on focus */
            }
            
            /* Accent Button (Primary Action) */
            QPushButton#AccentButton {
                background-color: #6ab0e5; 
                border: none;
                color: #2e3436; 
                padding: 12px;
                font-size: 11pt;
                font-weight: bold;
                border-radius: 6px;
                min-height: 30px;
            }
            QPushButton#AccentButton:hover {
                background-color: #4c8fd5;
            }
            QPushButton#AccentButton:pressed {
                background-color: #386ba0;
            }

            /* Secondary Button (Browse) */
            QPushButton#SecondaryButton {
                background-color: #4e5a60;
                border: 1px solid #5a646c;
                color: #ffffff;
                padding: 8px;
                font-size: 10pt;
                border-radius: 4px;
            }
            QPushButton#SecondaryButton:hover {
                background-color: #5a646c;
            }
            
            QProgressBar {
                border: 1px solid #5a646c;
                border-radius: 5px;
                text-align: center;
                height: 25px;
                background-color: #3c444a;
            }
            QProgressBar::chunk {
                background-color: #8ae234; /* Success green */
                border-radius: 5px;
            }
            
            QPlainTextEdit {
                background-color: #222527; /* Very dark for log */
                border: 1px solid #4e5a60;
                border-radius: 5px;
                padding: 5px;
                color: #b0e57f; /* Log green/light */
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 9pt;
            }
            QComboBox QAbstractItemView {
                background-color: #3c444a;
                color: #ffffff;
                selection-background-color: #6ab0e5;
            }
        """
        self.setStyleSheet(stylesheet)


    def browse_backup_directory(self):
        current_path = self.backup_path_edit.text()
        if not os.path.isdir(current_path):
             current_path = os.path.expanduser('~')
             
        backup_directory = QFileDialog.getExistingDirectory(
            self, "Select Backup Destination Folder", current_path, # Changed dialog title
            QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontResolveSymlinks
        )
        if backup_directory:
            self.backup_path_edit.setText(backup_directory)

    def execute_command(self):
        if self.worker and self.worker.isRunning():
            self.show_message("Error", "A process is already running. Please wait for it to complete.")
            return
            
        command_index = self.command_combo.currentIndex()
        if command_index == 0:
            self.show_message("Error", "Please select an **Operation**.")
            return

        # Use itemData to get the original command string ('backup' or 'list-devices')
        command = self.command_combo.itemData(command_index)
        backup_directory = self.backup_path_edit.text()
        
        self.log_box.clear()
        self.progress_bar.setValue(0)

        if command == "backup":
            if not backup_directory:
                self.show_message("Error", "Please select a **Backup Destination Folder**.")
                return
            if not os.path.exists(backup_directory):
                try:
                    os.makedirs(backup_directory, exist_ok=True)
                    self.log_box.appendPlainText(f"[INFO] Created directory: {backup_directory}")
                except Exception as e:
                    self.show_message("Error", f"Could not create backup directory: {e}")
                    return

        # Start the worker thread
        self.worker = LogicalBackupWorker(command, backup_directory)
        self.worker.log_updated.connect(self.update_log)
        self.worker.progress_updated.connect(self.update_progress)
        self.worker.backup_finished.connect(self.show_backup_completed_popup)
        self.worker.start()

    def update_log(self, message):
        self.log_box.moveCursor(self.log_box.textCursor().End)
        self.log_box.insertPlainText(message + "\n")
        
    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

    def show_backup_completed_popup(self, message):
        self.progress_bar.setValue(100)
        QMessageBox.information(
            self, 
            "Action Completed 🎉", # Changed popup title
            message
        )

    def show_message(self, title, message):
        if "Error" in title:
            QMessageBox.critical(self, title, message)
        else:
            QMessageBox.information(self, title, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogicalBackupApp()
    window.show()
    sys.exit(app.exec())
