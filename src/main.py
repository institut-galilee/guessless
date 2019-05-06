# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys
import os
import wiki
import sound
import random
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse

class Master(QObject):
    initialization = pyqtSignal()
    detection = pyqtSignal()
    sound_start = pyqtSignal()
    sound_guess = pyqtSignal()
    sound_bye = pyqtSignal()
    sound_stop = pyqtSignal()
    sound_begin = pyqtSignal()

    def __init__(self):
        super().__init__()

class Detection(QObject):
    title = pyqtSignal(str)
    score = pyqtSignal(str)
    description = pyqtSignal(str)
    guess = pyqtSignal(bool)
    loading = pyqtSignal(int)
    widgets = pyqtSignal(str)
    action = pyqtSignal(str)
    sound = pyqtSignal(str)
    sound_action = pyqtSignal(str)

    camera = None
    IM_WIDTH = 640
    IM_HEIGHT = 480
    image_tensor = None
    detection_boxes = None
    detection_scores = None
    detection_classes = None
    num_detections = None
    sess = None
    category_index = None

    def __init__(self):
        super().__init__()

    def init_detection(self):
        self.sound_action("start")
        self.action.emit("initialization")
        sys.path.append('..')
        from utils import label_map_util
        MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
        CWD_PATH = os.getcwd()
        PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
        PATH_TO_LABELS = os.path.join(CWD_PATH, 'data', 'mscoco_label_map.pbtxt')
        NUM_CLASSES = 90
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(categories)
        detection_graph = tf.Graph()

        # Load Tensorflow into memory
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            self.sess = tf.Session(graph=detection_graph)

        # Ressources
        self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        self.camera = PiCamera()
        self.camera.resolution = (self.IM_WIDTH, self.IM_HEIGHT)
        self.camera.framerate = 10

        self.action.emit("init_complete")
        self.sound_action("stop")

    def detect(self):
        self.action.emit("guess")
        self.sound_action("start")

        # Capture an image & expand it
        self.camera.capture("image.png")
        self.image = cv2.imread("image.png")
        self.image_expanded = np.expand_dims(self.image, axis=0)

        # Detection
        (boxes, scores, classes, num) = self.sess.run(
        [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
        feed_dict={self.image_tensor: self.image_expanded})

        objects = []
        for index, value in enumerate(classes[0]):
            object_dict = {}
            if scores[0, index] > 0.2:
                objects.append([(self.category_index.get(value)).get('name'), scores[0, index]])

        print(objects)

        word = [None, None]
        top = 0
        for i in range(len(objects)):
            if objects[i][1] > top:
                word = objects[i]

        print(word[0])

        if (word[0] != None):
            desc = wiki.search(str(word[0]))
            splited = desc.split(".");
            self.description.emit(splited[0] + ".")
            self.title.emit(word[0].capitalize())
            self.score.emit(str(int(word[1] * 100)))
            self.guess.emit(True)
            self.widgets.emit("show")
            self.action.emit("guess_complete")
            sound.textToSound(word[0])
        else:
            self.action.emit("guess_nothing")
            sound.textToSound("Nothing")

        self.sound_action("stop")

    def close_all(self):
        """
        self.camera.close()
        cv2.destroyAllWindows()
        """
        print("See you later !")

class Sound(QObject):

    def __init__(self):
        super().__init__()

    def stop(self):
        self.stop = True

    def launch(self):
        self.stop = False

    def start(self):
        while (self.stop != True):
            sound.start()

    def guess(self):
        while (self.stop != True):
            sound.pulsation

    def bye(self):
        while (self.stop != True):
            sound.bye()

class Application(QWidget):

    stop = False

    def __init__(self):
        super(Application, self).__init__()
        self.init_app()
        self.init_detection()
        self.master.sound_start.emit()

    def init_app(self):
        # Main window
        self.showFullScreen()
        self.setWindowTitle("Guessless")
        self.setStyleSheet("background-color: black;")

        self.titre_label = QLabel()
        self.titre_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.titre_label.setAlignment(Qt.AlignCenter)
        self.titre_label.setStyleSheet("QLabel {color: white; font-size: 40px; font-family: Carlito}")

        self.score_label = QLabel()
        self.score_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("QLabel {color: white; font-size: 25px; font-family: Carlito}")

        self.description_label = QLabel()
        self.description_label.setWordWrap(True);
        self.description_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("QLabel {color: white; font-family: Carlito; font-size: 14px}")

        self.bt_sound = QPushButton()
        self.bt_sound.setStyleSheet("background-color: white; font-size: 18px; font-style: bold; color: black")
        self.bt_sound.setFixedSize(40, 40)
        self.bt_sound.setIcon(QIcon('speaker.png'))
        self.bt_sound.setIconSize(QSize(24,24))
        self.bt_sound.clicked.connect(self.read_description)

        self.horizontalGroupBox = QGroupBox()
        self.layout = QHBoxLayout()

        self.vGroupBox = QGroupBox()
        self.soundGroupBox = QGroupBox()

        self.layout2 = QVBoxLayout()
        self.layout3 = QHBoxLayout()

        self.layout2.addWidget(self.titre_label)
        self.layout2.addWidget(self.score_label)
        self.layout2.addWidget(self.description_label, 1)
        self.layout3.addStretch(3)
        self.layout3.addWidget(self.bt_sound)
        self.bt_sound.hide()

        self.bt_guess = QPushButton("Guess !")
        self.bt_guess.setStyleSheet("background-color: indigo; font-size: 24px; font-style: bold; font-family: Carlito")
        self.bt_guess.setFixedHeight(60)
        self.bt_guess.clicked.connect(self.guess)
        self.layout.addWidget(self.bt_guess, 2)

        self.bt_quit = QPushButton("Shutdown")
        self.bt_quit.setStyleSheet("background-color: white; font-size: 16px; font-style: bold; color: black")
        self.bt_quit.setFixedHeight(60)
        self.bt_quit.clicked.connect(self.bye)
        self.layout.addWidget(self.bt_quit)

        self.horizontalGroupBox.setLayout(self.layout)
        self.vGroupBox.setLayout(self.layout2)
        self.soundGroupBox.setLayout(self.layout3)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.vGroupBox)
        self.mainLayout.addWidget(self.soundGroupBox)
        self.mainLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.mainLayout)

        self.show()

    def init_detection(self):
        # Create Thread, Master and Worker
        self.thread = QThread()
        self.thread.start()

        self.thread2 = QThread()
        self.thread2.start()

        self.worker = Detection()
        self.worker.moveToThread(self.thread)

        self.worker.title.connect(self.changeTitle)
        self.worker.score.connect(self.changeScore)
        self.worker.description.connect(self.changeDescription)
        self.worker.guess.connect(self.updateGuess)
        self.worker.loading.connect(self.loading)
        self.worker.widgets.connect(self.actionWidgets)
        self.worker.action.connect(self.action)
        self.worker.sound.connect(self.read_description)
        self.worker.sound_action.connect(self.sound_action)

        self.workerSound = Sound()
        self.workerSound.moveToThread(self.thread2)

        self.master = Master()
        self.master.initialization.connect(self.worker.init_detection)
        self.master.detection.connect(self.worker.detect)
        self.master.sound_start.connect(self.workerSound.start)
        self.master.sound_guess.connect(self.workerSound.guess)
        self.master.sound_bye.connect(self.workerSound.bye)
        self.master.sound_stop.connect(self.workerSound.stop)
        self.master.sound_begin.connect(self.workerSound.launch)

        # Tensorflow's initialization
        self.master.initialization.emit()

    def actionWidgets(self, action):
        if (action == "show"):
            self.bt_guess.show()
            self.bt_quit.show()
            self.titre_label.show()
            self.description_label.show()
            self.score_label.show()
            self.bt_sound.show()
        elif (action == "hide"):
            self.bt_guess.hide()
            self.bt_quit.hide()
            self.titre_label.hide()
            self.description_label.hide()
            self.score_label.hide()

    def read_description(self):
        sound.textToSound(self.description_label.text())

    def action(self, action):
        self.actionWidgets("hide")

        if (action == "guess"):
            self.bt_sound.hide()
            self.bt_quit.hide()
            self.titre_label.setText("Recognising ...")
            self.titre_label.show()
            self.score_label.setText(self.thinking())
            self.score_label.show()
            self.loading(1)
            self.description_label.show()
            self.bt_quit.show()

        if (action == "guess_complete"):
            self.actionWidgets("show")
            self.bt_quit.setText("Shutdown")

        elif (action == "initialization"):
            self.titre_label.setText("Initialization ...")
            self.titre_label.show()
            self.loading(2)
            self.description_label.show()

        elif (action == "init_complete"):
            self.actionWidgets("show")
            self.score_label.hide()
            self.bt_sound.hide()
            self.bt_guess.setEnabled(True)
            self.description_label.setText("Please push the button GUESS and magic will happen :)")
            self.titre_label.setText("Ready !")

        elif (action == "guess_nothing"):
            self.actionWidgets("show")
            self.score_label.hide()
            self.bt_sound.hide()
            self.description_label.setText("Try with other objects !")
            self.titre_label.setText("Nothing")
            self.updateGuess(True)

    def changeTitle(self, text):
        self.titre_label.setText(text)

    def sound_action(self, action):
        if (action == "start"):
            self.master.sound_begin.emit()
        elif (action == "stop"):
            self.master.sound_stop.emit()

    def thinking(self):
        message = "I'm thinking, give me some space !"
        rand = random.randint(0, 5)
        if (rand == 1):
            message = "I'm guessing, it's almost done !"
        if (rand == 2):
            message = "Those hands are awesome !"
        if (rand == 3):
            message = "I'm happy to help you :) !"
        if (rand == 4):
            message = "1, 2, 3, I'm guessing, 4, 5, 6, I'm still guessing !"
        if (rand == 5):
            message = "Don't tell me ... I will find it myself !"
        return message

    def loading(self, mode):
        if (mode == 1):
            self.movie = QMovie("loading.gif")
        elif (mode == 2):
            self.movie = QMovie("loading2.gif")

        self.movie.setScaledSize(QSize(400, 400))
        self.description_label.setMovie(self.movie)
        self.movie.start()

    def changeScore(self, score):
        self.score_label.setText(score + "%")

    def changeDescription(self, text):
        self.description_label.setText(text)

    def updateGuess(self, mode):
        self.bt_guess.setEnabled(mode)

    def guess(self):
        print("Detection !")
        self.master.detection.emit()
        self.master.sound_guess.emit()

    def close_all_things(self):
        self.worker.close_all()
        self.close()
        self.thread.quit()
        self.thread.wait(1)

    def bye(self):
        bt_text = self.bt_quit.text()
        if (bt_text == "Shutdown"):
            self.close_all_things()
            sound.Quit()
            os.system("shutdown now -h")

def main():
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
