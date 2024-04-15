from PyQt5 import QtCore, QtGui, QtWidgets
import random
import serial
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url('files/perepoloh/sky_background.png') no-repeat center fixed;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vinni = QtWidgets.QFrame(self.centralwidget)
        self.vinni.setGeometry(QtCore.QRect(10, 260, 101, 250))
        self.vinni.setStyleSheet("background-image: url('files/perepoloh/vinnipuh.jpg');\n"
                                 "border: 0px solid;")
        self.vinni.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vinni.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vinni.setObjectName("vinni")
        self.bees = QtWidgets.QFrame(self.centralwidget)
        self.bees.setGeometry(QtCore.QRect(1110, 300, 120, 91))
        self.bees.setStyleSheet("background-image: url('files/perepoloh/bees.jpg');\n"
                                "border: 0px solid;")
        self.bees.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bees.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bees.setObjectName("bees")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class FlappyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print('l')
        self.arduino = serial.Serial('COM4', 9600)  #% замените 'COM3' на имя порта вашего Arduino
        # self.arduino = 50
        print(self.arduino)
        self.score = 0
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(600, 10, 100, 20))
        self.score_label.setObjectName("score_label")
        self.score_label.setStyleSheet("color: white; font-size: 14pt;")

        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(550, 10, 40, 20))
        self.pause_button.setObjectName("pause_button")
        self.pause_button.setText("Pause")

        self.window_lower_bound = 0
        self.window_upper_bound = self.height() - 250

        # Timers
        self.bees_spawn_timer = QtCore.QTimer(self)
        self.bees_move_timer = QtCore.QTimer(self)
        self.score_timer = QtCore.QTimer(self)
        self.arduino_data_timer = QtCore.QTimer(self)

        # Initialize events
        self.init_events()

    def init_events(self):
        print('k')
        self.pause_button.clicked.connect(self.toggle_game_pause)
        print('h')
        self.bees_spawn_timer.timeout.connect(self.spawn_bees)
        self.bees_spawn_timer.start(50)

        self.bees_move_timer.timeout.connect(self.move_bees)
        self.bees_move_timer.start(50)

        self.score_timer.timeout.connect(self.update_score)
        self.score_timer.start(1000)

        self.arduino_data_timer.timeout.connect(self.read_arduino_data)
        self.arduino_data_timer.start(100)


    def spawn_bees(self):
        bees_x, _, _, _ = self.bees.geometry().getRect()
        if bees_x < -120 or bees_x > 1280:
            bees_y = random.randint(self.window_lower_bound, self.window_upper_bound - 91)
            self.bees.setGeometry(QtCore.QRect(1280, bees_y, 120, 91))


    def move_bees(self):
        bees_x, bees_y, _, _ = self.bees.geometry().getRect()
        bees_x -= 5

        if bees_x < -120:
            bees_x = 1280

        self.bees.setGeometry(QtCore.QRect(bees_x, bees_y, 120, 91))
        self.check_collision()

    def update_score(self):
        self.score += 1
        self.score_label.setText(f"Очки: {self.score}")

    def read_arduino_data(self):
        if self.arduino.in_waiting > 0:
        # if True:
            try:
                distance = int(self.arduino.readline().decode().strip())
                # distance = 50
                self.move_vinni(distance)
            except ValueError:
                pass

    #def move_vinni(self, distance):
    #    distance = max(min(distance, 30), 1)
     #   ratio = (distance - 1) / (30 - 1)
     #   new_y = self.window_upper_bound - (self.window_upper_bound - self.window_lower_bound) * ratio
     #   self.vinni.setGeometry(QtCore.QRect(10, new_y, 101, 250))
      #  self.check_collision()

    def move_vinni(self, distance):
        print('k')
        distance = max(min(distance, 30), 1)
        x = np.array([1, 15, 30])
        y = np.array([self.window_upper_bound, self.window_lower_bound + 125, self.window_lower_bound])
        new_y = np.interp(distance, x, y)
        print('000')
        self.vinni.setGeometry(QtCore.QRect(10, int(new_y), 101, 250))
        self.check_collision()
        print('200')


    def check_collision(self):
        print(888)
        vinni_rect = self.vinni.geometry()
        bees_rect = self.bees.geometry()
        print(888)

        if vinni_rect.intersects(bees_rect) or self.is_vinni_out_of_bounds():
            self.game_over()

    def is_vinni_out_of_bounds(self):
        _, vinni_y, _, _ = self.vinni.geometry().getRect()
        return vinni_y <= self.window_lower_bound or vinni_y >= self.window_upper_bound

    def game_over(self):
        self.bees_spawn_timer.stop()
        self.bees_move_timer.stop()
        self.score_timer.stop()
        self.arduino_data_timer.stop()

        self.game_over_label = QtWidgets.QLabel(self.centralwidget)
        self.game_over_label.setGeometry(QtCore.QRect(540, 300, 300, 100))
        self.game_over_label.setStyleSheet("color: white; font-size: 14pt;")
        self.game_over_label.setText(f"Молодец! Игра завершена!\nОчки: {self.score}")
        self.game_over_label.show()

        self.out_but = QtWidgets.QPushButton()
        self.out_but.setGeometry(540, 300, 600, 100)
        self.out_but.setText('в меню')
        self.out_but.clicked.connect(self.out)

    def out(self):
        self.hide()

    def toggle_game_pause(self):
        if self.bees_spawn_timer.isActive():
            self.bees_spawn_timer.stop()
            self.bees_move_timer.stop()
            self.score_timer.stop()
            self.arduino_data_timer.stop()
            self.pause_button.setText("Resume")
        else:
            self.bees_spawn_timer.start()
            self.bees_move_timer.start()
            self.score_timer.start()
            self.arduino_data_timer.start()
            self.pause_button.setText("Pause")

        self.out_but = QtWidgets.QPushButton()
        self.out_but.setGeometry(540, 300, 600, 100)
        self.out_but.setText('в меню')
        self.out_but.clicked.connect(self.out)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = FlappyMainWindow()

    main_window.show()
    result = app.exec_()
    main_window.arduino.close()  # закрытие соединения с Arduino
    sys.exit(result)
