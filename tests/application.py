# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys
import os
import wiki
import random
"""
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
"""

class Master(QObject):
    initialization = pyqtSignal()
    detection = pyqtSignal()

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

    camera = None
    IM_WIDTH = 640
    IM_HEIGHT = 480
    image_tensor = None
    detection_boxes = None
    detection_scores = None
    detection_classes = None
    num_detections = None

    def __init__(self):
        super().__init__()

    def init_detection(self):
        self.action.emit("initialization")
        """
        sys.path.append('..')
        from utils import label_map_util
        MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
        CWD_PATH = os.getcwd()
        PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
        PATH_TO_LABELS = os.path.join(CWD_PATH, 'data', 'mscoco_label_map.pbtxt')
        NUM_CLASSES = 90
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)
        detection_graph = tf.Graph()

        # Load Tensorflow into memory
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            sess = tf.Session(graph=detection_graph)

        # Ressources
        self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        self.camera = PiCamera()
        self.camera.resolution = (self.IM_WIDTH, self.IM_HEIGHT)
        self.camera.framerate = 10
        """

        for i in range(5):
            print("Init ! " + str(i))
            time.sleep(1)

        self.action.emit("initComplete")

    def detect(self):
        self.action.emit("guess")
        """
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
            if self.scores[0, index] > 0:
                object_dict[(self.category_index.get(value)).get('name')] = self.scores[0, index]
                objects.append(object_dict)

        #os.system('echo "' + word + '" | festival --tts')
        print(objects)
        """
        for i in range(5):
            print("Detectetion powa ! " + str(i))
            time.sleep(1)

        word = "Smartphone"

        self.description.emit(wiki.search(word))
        self.title.emit(word)
        self.score.emit("50")
        self.guess.emit(True)
        self.widgets.emit("show")

    def close_all(self):
        """
        self.camera.close()
        cv2.destroyAllWindows()
        """
        print("See you later !")


class Application(QWidget):

    def __init__(self):
        super(Application, self).__init__()
        self.init_app()
        self.init_detection()

    def init_app(self):
        # Main window
        #self.showFullScreen()
        self.setFixedSize(600, 800)
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

        self.horizontalGroupBox = QGroupBox()
        self.layout = QHBoxLayout()

        self.vGroupBox = QGroupBox()
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.titre_label)
        self.layout2.addWidget(self.score_label)
        self.layout2.addWidget(self.description_label, 1)

        self.bt_guess = QPushButton("Guess !")
        self.bt_guess.setStyleSheet("background-color: indigo; font-size: 24px; font-style: bold; font-family: Carlito")
        self.bt_guess.setFixedHeight(60)
        self.bt_guess.clicked.connect(self.guess)
        self.layout.addWidget(self.bt_guess, 3)

        self.bt_quit = QPushButton("Quit")
        self.bt_quit.setStyleSheet("background-color: white; font-size: 18px; font-style: bold; color: black")
        self.bt_quit.setFixedHeight(60)
        self.bt_quit.clicked.connect(self.close_all_things)
        self.layout.addWidget(self.bt_quit)

        self.horizontalGroupBox.setLayout(self.layout)
        self.vGroupBox.setLayout(self.layout2)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.vGroupBox)
        self.mainLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.mainLayout)

        self.show()

    def init_detection(self):
        # Create Thread, Master and Worker
        self.thread = QThread()
        self.thread.start()

        self.worker = Detection()
        self.worker.moveToThread(self.thread)

        self.worker.title.connect(self.changeTitle)
        self.worker.score.connect(self.changeScore)
        self.worker.description.connect(self.changeDescription)
        self.worker.guess.connect(self.updateGuess)
        self.worker.loading.connect(self.loading)
        self.worker.widgets.connect(self.actionWidgets)
        self.worker.action.connect(self.action)

        self.master = Master()
        self.master.initialization.connect(self.worker.init_detection)
        self.master.detection.connect(self.worker.detect)

        # Tensorflow's initialization
        self.master.initialization.emit()

    def actionWidgets(self, action):
        if (action == "show"):
            self.bt_guess.show()
            self.bt_quit.show()
            self.titre_label.show()
            self.description_label.show()
            self.score_label.show()
        elif (action == "hide"):
            self.bt_guess.hide()
            self.bt_quit.hide()
            self.titre_label.hide()
            self.description_label.hide()
            self.score_label.hide()

    def action(self, action):
        self.actionWidgets("hide")

        if (action == "guess"):
            self.titre_label.setText("Recognising ...")
            self.titre_label.show()
            self.score_label.setText(self.thinking())
            self.score_label.show()
            self.loading(1)
            self.description_label.show()
            self.bt_quit.show()

        elif (action == "initialization"):
            self.titre_label.setText("Initialization ...")
            self.titre_label.show()
            self.loading(2)
            self.description_label.show()

        elif (action == "initComplete"):
            self.actionWidgets("show")
            self.score_label.hide()
            self.bt_guess.setEnabled(True)
            self.description_label.setText("Please push the button GUESS and magic will happen :)")
            self.titre_label.setText("Ready !")

    def changeTitle(self, text):
        self.titre_label.setText(text)

    def thinking(self):
        message = "I'm thinking, give me some space !"
        rand = random.randint(0, 4)
        if (rand == 1):
            message = "I'm guessing, it's almost done !"
        if (rand == 2):
            message = "Those hands are awesome !"
        if (rand == 3):
            message = "I'm happy to help you :) !"
        if (rand == 4):
            message = "1, 2, 3, I'm guessing, 4, 5, 6, I'm still guessing !"
        return message

    def loading(self, mode):
        if (mode == 1):
            self.movie = QMovie("loading.gif")
        elif (mode == 2):
            self.movie = QMovie("loading2.gif")

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

    def close_all_things(self):
        self.worker.close_all()
        self.close()
        self.thread.quit()
        self.thread.wait(1)

def main():
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
