# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
import wiki

class application(QWidget):

    def __init__(self):
        super(application, self).__init__()
        self.app_initialization()
        self.detection_initialization()

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
        self.quit_btn.clicked.connect(self.app.quit())

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
        self.detect()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            print("Fuck you !")

    def detection_initialization(self):
        min_score = 0.5
        IM_WIDTH = 640
        IM_HEIGHT = 480

        sys.path.append('..')
        from utils import label_map_util
        MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'
        CWD_PATH = os.getcwd()
        PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
        PATH_TO_LABELS = os.path.join(CWD_PATH,'data','mscoco_label_map.pbtxt')
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
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    def detect(self):
        # Capture image & expand it
        camera = PiCamera()
        camera.resolution = (IM_WIDTH,IM_HEIGHT)
        camera.framerate = 10
        camera.capture("image.png")
        image = cv2.imread("image.png")
        image_expanded = np.expand_dims(image, axis=0)

        # Detection
        (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})
        print(str(classes[0][0]) + " : " + wiki.search(classes[0][0]))

    def close_all(self):
        camera.close()
        cv2.destroyAllWindows()


def main():

    # Initialization
    app = QApplication(sys.argv)
    window = application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
