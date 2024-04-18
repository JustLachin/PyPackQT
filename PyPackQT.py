import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QTextEdit
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyInstaller Desktop Uygulaması")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.selectFileButton = QPushButton("Python dosyası seç")
        self.selectFileButton.clicked.connect(self.selectFile)
        layout.addWidget(self.selectFileButton)

        self.logLabel = QLabel("Log Kaydı")
        layout.addWidget(self.logLabel)

        self.logTextEdit = QTextEdit()
        layout.addWidget(self.logTextEdit)

        self.startButton = QPushButton("Paketlemeyi Başlat")
        self.startButton.clicked.connect(self.startPackaging)
        layout.addWidget(self.startButton)

        self.setLayout(layout)

        self.selectedFilePath = None

    def selectFile(self):
        self.selectedFilePath, _ = QFileDialog.getOpenFileName(self, "Python dosyasını seç", "", "Python Files (*.py)")
        if self.selectedFilePath:
            self.logTextEdit.append(f"Seçilen dosya: {self.selectedFilePath}")

    def startPackaging(self):
        if not self.selectedFilePath:
            self.logTextEdit.append("Lütfen bir dosya seçin.")
            return

        pyinstaller_path = os.path.join(os.path.dirname(__file__), "pyinstaller", "bin", "pyinstaller.exe")
        self.logTextEdit.append("Paketleme işlemi başlatılıyor...")
        process = subprocess.Popen([pyinstaller_path, "--onefile", self.selectedFilePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            self.logTextEdit.append(stdout.decode())
        if stderr:
            self.logTextEdit.append(stderr.decode())
        self.logTextEdit.append("Paketleme işlemi tamamlandı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
