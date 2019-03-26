# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
import sys

class application(QWidget):

    def __init__(self):
        super(application, self).__init__()
        self.init_app()
        self.init_detection()
        self.init_complete()

    def init_app(self):
        self.showFullScreen()
        self.setFixedSize(640, 480)
        self.move(300, 150)
        self.setWindowTitle("Guessless")

        self.titre_label = QLabel("Initialization ...")
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
        self.layout.addLayout(self.btn_layout, 0, 0)
        self.setLayout(self.layout)
        self.show()

    def guess(self):
        print("Detection !")
        print(slef.detect())

    def init_complete(self):
        self.titre_label.setText("Initialization complete !")

    def init_detection(self):
        self.min_score = 0.5
        self.IM_WIDTH = 640
        self.IM_HEIGHT = 480

        sys.path.append('..')
        from utils import label_map_util
        self.MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
        self.CWD_PATH = os.getcwd()
        self.PATH_TO_CKPT = os.path.join(self.CWD_PATH, self.MODEL_NAME, 'frozen_inference_graph.pb')
        self.PATH_TO_LABELS = os.path.join(self.CWD_PATH, 'data', 'mscoco_label_map.pbtxt')
        self.NUM_CLASSES = 90
        self.label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        self.categories = label_map_util.convert_label_map_to_categories(self.label_map, max_num_classes=self.NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(self.categories)
        self.detection_graph = tf.Graph()

        # Load Tensorflow into memory
        with self.detection_graph.as_default():
            self.od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                self.serialized_graph = fid.read()
                self.od_graph_def.ParseFromString(self.serialized_graph)
                tf.import_graph_def(self.od_graph_def, name='')
            self.sess = tf.Session(graph=self.detection_graph)

        # Ressources
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def close_all():
        camera.close()
        cv2.destroyAllWindows()


    def detect(self):
        # Capture image & expand it
        self.camera = PiCamera()
        self.camera.resolution = (self.IM_WIDTH, self.IM_HEIGHT)
        self.camera.framerate = 10
        self.camera.capture("image.png")
        self.image = cv2.imread("image.png")
        self.image_expanded = np.expand_dims(self.image, axis=0)

        # Detection
        (self.boxes, self.scores, self.classes, self.num) = sess.run(
        [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
        feed_dict={self.image_tensor: self.image_expanded})
        print(str(self.classes[0][0]) + " : " + wiki.search(self.classes[0][0]))
        return str(self.classes[0][0])


def main():

    # Initialization
    app = QApplication(sys.argv)
    window = application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
