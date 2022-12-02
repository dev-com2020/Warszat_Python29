import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja!")

        button = QPushButton("Naciśnij mnie!")
        button.setCheckable(True)
        button.clicked.connect(self.clicked_connect)
        button.clicked.connect(self.toggled)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def clicked_connect(self):
        print("Kliknięte!")

    def toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
