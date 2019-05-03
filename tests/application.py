# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys

class Application(QWidget):

    def __init__(self):
        super(Application, self).__init__()
        self.init_app()

    def init_app(self):
        #self.showFullScreen()
        self.setFixedSize(640, 480)
        self.move(300, 150)
        self.setWindowTitle("Guessless")

        self.titre_label = QLabel("Apple")
        self.titre_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.titre_label.setAlignment(Qt.AlignCenter)
        self.titre_label.setStyleSheet("QLabel {color: white; font-size: 40px;}")

        self.score_label = QLabel("67%")
        self.score_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("QLabel {color: white; font-size: 25px;}")

        self.description_label = QLabel("An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit ! An apple is a fruit !")
        self.description_label.setWordWrap(True);
        self.description_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("QLabel {color: white;}")

        self.horizontalGroupBox = QGroupBox()
        self.layout = QHBoxLayout()

        self.vGroupBox = QGroupBox()
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.titre_label)
        self.layout2.addWidget(self.score_label)
        self.layout2.addWidget(self.description_label, 1)
        self.layout2.addStretch(1)

        self.bt_guess = QPushButton("Guess !")
        self.layout.addWidget(self.bt_guess, 3)

        self.bt_quit = QPushButton("Quit")
        self.bt_quit.clicked.connect(self.close_all_things)
        self.layout.addWidget(self.bt_quit)

        self.horizontalGroupBox.setLayout(self.layout)
        self.vGroupBox.setLayout(self.layout2)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.vGroupBox)
        self.mainLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.mainLayout)

        self.show()

    def guess(self):
        print("Detection !")

    def close_all_things(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
