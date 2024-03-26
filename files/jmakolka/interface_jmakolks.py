# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Happy_Jmakolka(object):
    def setupUi(self, Happy_Jmakolka):
        Happy_Jmakolka.setObjectName("Happy_Jmakolka")
        Happy_Jmakolka.resize(1920, 1080)
        Happy_Jmakolka.setStyleSheet("QWidget{\n"
"background: url(files/jmakolka/jmakolka_background.jpg);\n"
"}\n"
"QToolButton{\n"
"background: rgb(255, 255, 127);\n"
"border: 2px solid rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"QFrame{\n"
"background: rgb(0, 85, 255);\n"
"border: 2px solid green;\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"}\n"
"QLabel{\n"
"background: rgb(0, 0, 0, 0);\n"
"border: 2px solid rgb(0, 0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 2px;\n"
"}\n"
"#frame_7{\n"
"background-color: rgb(85, 170, 0);\n"
"}\n"
"#frame_8{\n"
"background-color: rgb(85, 170, 0);\n"
"}\n"
"#frame_9{\n"
"background-color: rgb(85, 170, 0);\n"
"}\n"
"#frame_10{\n"
"background-color: rgb(85, 170, 0);\n"
"}")
        self.frame_16 = QtWidgets.QFrame(Happy_Jmakolka)
        self.frame_16.setGeometry(QtCore.QRect(500, 850, 151, 141))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.input_1 = QtWidgets.QLabel(self.frame_16)
        self.input_1.setGeometry(QtCore.QRect(20, 10, 120, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.input_1.setFont(font)
        self.input_1.setObjectName("label_2")
        self.toolButton_2 = QtWidgets.QToolButton(Happy_Jmakolka)
        self.toolButton_2.setGeometry(QtCore.QRect(2010, 930, 181, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("#toolButton{\n"
"background: rgb(255, 255, 127)\n"
"}")
        self.toolButton_2.setObjectName("toolButton_2")
        self.image_3 = QtWidgets.QFrame(Happy_Jmakolka)
        self.image_3.setGeometry(QtCore.QRect(1070, 190, 410, 640))
        self.image_3.setStyleSheet("background:url(files/jmakolka/fish_main.jpg)")
        self.image_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_3.setObjectName("frame_5")
        self.image_1 = QtWidgets.QFrame(Happy_Jmakolka)
        self.image_1.setGeometry(QtCore.QRect(170, 190, 410, 640))
        self.image_1.setStyleSheet("background:url(files/jmakolka/grandfather_main.jpg)")
        self.image_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_1.setObjectName("frame_12")
        self.frame_15 = QtWidgets.QFrame(Happy_Jmakolka)
        self.frame_15.setGeometry(QtCore.QRect(740, 850, 151, 141))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.input_2 = QtWidgets.QLabel(self.frame_15)
        self.input_2.setGeometry(QtCore.QRect(20, 10, 120, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.input_2.setFont(font)
        self.input_2.setObjectName("label_6")
        self.image_2 = QtWidgets.QFrame(Happy_Jmakolka)
        self.image_2.setGeometry(QtCore.QRect(620, 190, 410, 640))
        self.image_2.setStyleSheet("background:url(files/jmakolka/grandmother_main.jpg)")
        self.image_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_2.setObjectName("frame_11")
        self.frame_14 = QtWidgets.QFrame(Happy_Jmakolka)
        self.frame_14.setGeometry(QtCore.QRect(980, 850, 151, 141))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.input_3 = QtWidgets.QLabel(self.frame_14)
        self.input_3.setGeometry(QtCore.QRect(20, 10, 120, 131))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.input_3.setFont(font)
        self.input_3.setObjectName("label_7")
        self.nums_2 = QtWidgets.QLabel(Happy_Jmakolka)
        self.nums_2.setGeometry(QtCore.QRect(1760, 470, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.nums_2.setFont(font)
        self.nums_2.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(Happy_Jmakolka)
        self.frame_3.setGeometry(QtCore.QRect(1520, 620, 231, 211))
        self.frame_3.setStyleSheet("background:url(files/jmakolka/kolobok_icon.jpg)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.image_5 = QtWidgets.QLabel(Happy_Jmakolka)
        self.image_5.setGeometry(QtCore.QRect(1520, 400, 231, 211))
        self.image_5.setStyleSheet("""border: 2px solid green;
border-radius: 10px;
padding: 2px;""")
        self.image_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_5.setObjectName("frame_2")
        self.nums_1 = QtWidgets.QLabel(Happy_Jmakolka)
        self.nums_1.setGeometry(QtCore.QRect(1760, 250, 281, 110))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.nums_1.setFont(font)
        self.nums_1.setStyleSheet("")
        self.nums_1.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Happy_Jmakolka)
        self.label_4.setGeometry(QtCore.QRect(1760, 670, 281, 110))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.image_4 = QtWidgets.QLabel(Happy_Jmakolka)
        self.image_4.setGeometry(QtCore.QRect(1520, 180, 231, 211))
        self.image_4.setStyleSheet("""border: 2px solid green;
border-radius: 10px;
padding: 2px;""")
        self.image_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_4.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(Happy_Jmakolka)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 201, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("#toolButton{\n"
"background: rgb(255, 255, 127)\n"
"}")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_3 = QtWidgets.QPushButton(Happy_Jmakolka)
        self.pushButton_3.setGeometry(QtCore.QRect(1560, 870, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background: rgb(255, 255, 127)")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Happy_Jmakolka)
        QtCore.QMetaObject.connectSlotsByName(Happy_Jmakolka)

    def retranslateUi(self, Happy_Jmakolka):
        _translate = QtCore.QCoreApplication.translate
        Happy_Jmakolka.setWindowTitle(_translate("Happy_Jmakolka", "Form"))
        self.input_1.setText(_translate("Happy_Jmakolka", "-"))
        self.toolButton_2.setText(_translate("Happy_Jmakolka", "НАЗАД"))
        self.input_2.setText(_translate("Happy_Jmakolka", "-"))
        self.input_3.setText(_translate("Happy_Jmakolka", "-"))
        self.nums_2.setText(_translate("Happy_Jmakolka", "412"))
        self.nums_1.setText(_translate("Happy_Jmakolka", "134"))
        self.label_4.setText(_translate("Happy_Jmakolka", "314"))
        self.toolButton.setText(_translate("Happy_Jmakolka", "НАЗАД"))
        self.pushButton_3.setText(_translate("Happy_Jmakolka", "НАЧАТЬ"))
