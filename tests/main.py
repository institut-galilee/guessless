# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class application(QWidget):

    def __init__(self):
        super(application, self).__init__()
        self.app_initialization()

    def app_initialization(self):
        self.setFixedSize(640, 480)
        self.move(300, 150)
        self.setWindowTitle("Guessless")

        self.titre_label = QLabel("PyCamera")
        self.titre_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.titre_label.setAlignment(Qt.AlignCenter)
        self.titre_label.setStyleSheet("QLabel {color: <hite;}")

        self.guess_btn = QPushButton("Guess !")
        self.guess_btn.clicked.connect(self.guess)
        self.guess_btn.resize(50, 30)
        self.quit_btn = QPushButton("Quit :(")
        self.quit_btn.clicked.connect(self.close)

        self.btn_layout = QHBoxLayout()
        self.layout = QGridLayout()

        self.layout.addWidget(self.titre_label, 0, 0)
        self.titre_label.adjustSize()

        self.btn_layout.addWidget(self.guess_btn)
        self.btn_layout.addWidget(self.quit_btn)
        self.layout.addLayout(self.btn_layout, 1, 0)
        self.setLayout(self.layout)
        self.show()

    def guess(self):
        print("Detection !")

    def quit():
        return 1

def main():

    # Initialization
    app = QApplication(sys.argv)
    window = application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
