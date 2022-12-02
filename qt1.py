import sys
from random import choice

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.button_is_checked = True

        self.setWindowTitle("Moja aplikacja!")

        self.button = QPushButton("Naciśnij mnie!")
        self.button.clicked.connect(self.clicked_connect)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        # self.button.setCheckable(True)
        # self.button.released.connect(self.clicked_connect)
        # self.button.setChecked(self.button_is_checked)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def clicked_connect(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("Setting title:   %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        
        # self.button_is_checked = self.button.isChecked()
        # self.button.setText("Już zostałem wciśnięty!")
        # self.button.setEnabled(False)
        # print(self.button_is_checked)
        
    def the_window_title_changed(self,window_title):
        print("Window title changed   %s" % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
