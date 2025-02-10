import sys
import os
import tempfile
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QComboBox, QProgressBar, QPlainTextEdit, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal
import subprocess
import re

# Function to strip ANSI escape codes
def strip_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

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

        self.log_updated.emit(f"Starting backup to {self.backup_directory}...")

        process = subprocess.Popen(['pymobiledevice3', 'backup2', 'backup', '--full', self.backup_directory],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True, encoding='utf-8')

        for line in process.stdout:
            self.log_updated.emit(strip_ansi_escape_codes(line.strip()))

        process.communicate()
        if process.returncode != 0:
            self.log_updated.emit("Error executing backup command.")
        else:
            self.log_updated.emit("Backup completed successfully.")
            self.backup_finished.emit(f"Backup completed and saved to {self.backup_directory}.")

    def list_connected_devices(self):
        self.log_updated.emit("Listing connected devices...")
        try:
            process = subprocess.Popen(['pymobiledevice3', 'usbmux', 'list'],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)

            for line in process.stdout:
                self.log_updated.emit(strip_ansi_escape_codes(line.strip()))

            _, stderr = process.communicate()
            if process.returncode != 0:
                self.log_updated.emit(f"Error listing connected devices: {stderr}")
        except subprocess.CalledProcessError as e:
            self.log_updated.emit(f"Error listing connected devices: {e}")

class LogicalBackupApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logical Backup Tool")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.command_label = QLabel("Options:")
        self.command_combo = QComboBox()
        self.command_combo.addItem("Select Options")
        self.command_combo.addItem("backup")
        self.command_combo.addItem("list-devices")
        
        self.execute_button = QPushButton("Apply", self)
        self.execute_button.setObjectName("blueButton")
        self.execute_button.clicked.connect(self.execute_command)

        self.backup_label = QLabel("Backup Directory:")
        self.backup_path_edit = QLineEdit()
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setObjectName("browseButton")
        self.browse_button.clicked.connect(self.browse_backup_directory)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        self.log_box = QPlainTextEdit()
        self.log_box.setReadOnly(True)

        layout.addWidget(self.command_label)
        layout.addWidget(self.command_combo)
        layout.addWidget(self.backup_label)
        layout.addWidget(self.backup_path_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.execute_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.log_box)

        self.setLayout(layout)

        self.setStyleSheet("""
        QPushButton#blueButton, #browseButton {
            background-color: #3498db;
            border: none;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 4px;
        }
        QPushButton#blueButton:hover, #browseButton:hover {
            background-color: #2980b9;
        }
        """)

        self.worker = None

    def browse_backup_directory(self):
        backup_directory = QFileDialog.getExistingDirectory(self, "Select Backup Directory")
        if backup_directory:
            self.backup_path_edit.setText(backup_directory)

    def execute_command(self):
        command = self.command_combo.currentText()
        backup_directory = self.backup_path_edit.text()

        if command == "Select Options":
            self.show_message("Error", "Please select an option.")
            return

        if command == "backup" and not backup_directory:
            self.show_message("Error", "Please select a backup directory.")
            return

        self.worker = LogicalBackupWorker(command, backup_directory)
        self.worker.log_updated.connect(self.update_log)
        self.worker.progress_updated.connect(self.update_progress)
        self.worker.backup_finished.connect(self.show_backup_completed_popup)
        self.worker.start()

    def update_log(self, message):
        self.log_box.appendPlainText(message)

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

    def show_backup_completed_popup(self, message):
        QMessageBox.information(self, "Backup Completed", message)

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogicalBackupApp()
    window.show()
    sys.exit(app.exec())
