import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0.846591, x2:0.494, y2:0.289364, stop:0 rgba(0, 210, 255, 255), stop:1 rgba(50, 106, 215, 255));")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 270, 150, 150))
        self.pushButton.setStyleSheet("border-radius: 75px;\n"
"background-color: rgb(198, 255, 212);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "NLO"))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)

    def keyPressEvent(self, event):
        try:
            if event.key() == QtCore.Qt.Key_Left:
                self.pushButton.move((self.pushButton.x() - 20) % 1000, (self.pushButton.y()))
            elif event.key() == QtCore.Qt.Key_Up:
                self.pushButton.move((self.pushButton.x()) % 1000, (self.pushButton.y() - 20) % 800)
            elif event.key() == QtCore.Qt.Key_Down:
                self.pushButton.move((self.pushButton.x()) % 1000, (self.pushButton.y() + 20) % 800)
            elif event.key() == QtCore.Qt.Key_Right:
                self.pushButton.move((self.pushButton.x() + 20) % 1000, (self.pushButton.y()) % 800)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
