#!/usr/bin/env python3
import sys
import time
from PyQt5 import QtCore, QtWidgets


class ConfWorker(QtCore.QObject):
    updated_button = QtCore.pyqtSignal(list)
    updated_label = QtCore.pyqtSignal(str)
    updated_error = QtCore.pyqtSignal(str)
    request_signal = QtCore.pyqtSignal()
    customer = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(ConfWorker, self).__init__(parent)
        self.customer.connect(self.getcustomer)

    @QtCore.pyqtSlot()
    def doWork(self):
        #self.request_signal.emit()
        print("ok")

    @QtCore.pyqtSlot(str)
    def getcustomer(self, text):
        self.configure(text)

    def configure(self, customer_name):
        self.updated_button.emit(["In progress...", False])
        self.updated_label.emit(customer_name)
        time.sleep(5) # During this time you should be able to see color change etc.
        #myaction.myaction(customer_name)# TAKES ~20 SECONDS TO FINISH
        self.updated_button.emit(["Start", True])

class ConfGUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ConfGUI, self).__init__()

        # create a QThread and start the thread that handles
        thread = QtCore.QThread(self)
        thread.start()

        # create the worker without a parent so you can move
        self.worker = ConfWorker()
        # the worker moves to another thread
        self.worker.moveToThread(thread)

        self.worker.updated_button.connect(self.updateButton)
        self.worker.updated_label.connect(self.updateLabel)
        self.worker.updated_error.connect(self.updateError)
        self.worker.request_signal.connect(self.sendCustomer)

        self.targetBtn = QtWidgets.QPushButton('Start Configuration', self)
        self.targetBtn.setStyleSheet("QPushButton { background-color: green; color: white }"
                        "QPushButton:disabled { background-color: red; color: white }")
        self.targetBtn.clicked.connect(self.worker.doWork)
        self.targetBtn.setFixedSize(200, 50)

        self.customerlist = QtWidgets.QComboBox(self)
        self.customerlist.addItems(["testcustomer1", "testcustomer2", "testcustomer3"])
        self.customerlist.setFixedSize(200, 50)

        self.label = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 30pt; font-family: Courier; color: green;')
        self.label.setFixedSize(400,50)

        self.error_label = QtWidgets.QLabel(self, alignment=QtCore.Qt.AlignCenter)
        self.error_label.setStyleSheet('font-size: 30pt; font-family: Courier; color: red;')
        self.error_label.setFixedSize(400,50)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.customerlist, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.error_label, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.targetBtn, alignment=QtCore.Qt.AlignCenter)
        self.setFixedSize(400, 550)

    @QtCore.pyqtSlot()
    def sendCustomer(self):
        self.worker.customer.emit(self.customerlist.currentText())

    @QtCore.pyqtSlot(list)
    def updateButton(self, button_list):
        self.targetBtn.setText(button_list[0])
        self.targetBtn.setEnabled(button_list[1])

    @QtCore.pyqtSlot(str)
    def updateLabel(self, label_text):
        self.label.setText(label_text)

    @QtCore.pyqtSlot(str)
    def updateError(self, error_text):
        self.error_label.setText(error_text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = ConfGUI()
    ex.show()
    sys.exit(app.exec_())
