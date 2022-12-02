import sys
from random import choice

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja!")
        self.label = QLabel("Kliknij w okno!")
        self.setCentralWidget(self.label)
        self.setContextMenuPolicy()
        self.customContextMenuRequested.connect(self.on_context_menu)

    # def mouseMoveEvent(self, e):
    #     if e.button() == Qt.MouseButton.LeftButton:
    #         self.label.setText("mouseMoveEvent LEFT")
    #     elif e.button() == Qt.MouseButton.MiddleButton:
    #         self.label.setText("mouseMoveEvent MIDDLE")
    #     elif e.button() == Qt.MouseButton.RightButton:
    #         self.label.setText("mouseMoveEvent RIGHT")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseMoveEvent LEFT")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseMoveEvent MIDDLE")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseMoveEvent RIGHT")

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseRelaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
