# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'man_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet("background: url(files/main_window/mainmenu_background.jpg)\n"
"")
        self.btn_ris = QtWidgets.QPushButton(Form)
        self.btn_ris.setGeometry(QtCore.QRect(1210, 310, 700, 111))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_ris.setFont(font)
        self.btn_ris.setStyleSheet("background: rgba(85, 255, 127, 0.7);\n"
"border-radius:25px;")
        self.btn_ris.setObjectName("pushButton_2")
        self.btn_jmak = QtWidgets.QPushButton(Form)
        self.btn_jmak.setGeometry(QtCore.QRect(740, 885, 700, 90))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_jmak.setFont(font)
        self.btn_jmak.setStyleSheet("background: rgba(0, 170, 255, 0.7);\n"
"border-radius:25px")
        self.btn_jmak.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(710, 100, 700, 141))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgba(0, 0, 0, 0)\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_ris.setText(_translate("Form", "ВЕСЕЛАЯ РИСОВАЛКА"))
        self.btn_jmak.setText(_translate("Form", "ВЕСЕЛАЯ ЖМАКОЛКА"))
        self.label.setText(_translate("Form", "ГЛАВНОЕ МЕНЮ"))
