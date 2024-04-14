import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl
from flappy import FlappyMainWindow
from jmakolka_last import JmakolkaMainWindow
from risovalka import RisovalkaMainWindow
from Evolution import EvolutionMainRun, WINDOW
import subprocess


class Main_Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/main_window/new_menu.ui', self)

        # Создание плейлиста и добавление музыкальной заставки
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("files/main_window/cook.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        # Создание объекта проигрывателя и добавление плейлиста
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)

        # Воспроизведение музыки при запуске приложения
        self.player.play()

        self.perepoloh.clicked.connect(self.open_pchel)
        self.jmakolka.clicked.connect(self.open_jmak)
        self.risovalka.clicked.connect(self.open_ris)
        self.more_games.clicked.connect(self.all_games)
        self.all_games_window = None

    def all_games(self):
        if not self.all_games_window:
            self.all_games = All_Games()
        self.hide()
        self.all_games.show()

    '''def open_vadimky(self):
        EvolutionMainRun(WINDOW)'''

    def open_jmak(self):
        self.jm = JmakolkaMainWindow()
        self.jm.show()
        # self.hide1()

    def open_ris(self):
        self.risov = RisovalkaMainWindow()
        self.risov.show()
        # elf.hide()

    def open_pchel(self):
        self.bird = FlappyMainWindow()
        self.bird.show()

class All_Games(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/main_window/all_games.ui', self)
        self.back.clicked.connect(self.back_to_menu)
        self.menu_window = None
        self.perepoloh.clicked.connect(self.open_pchel)
        self.jmakolka.clicked.connect(self.open_jmak)
        self.risovalka.clicked.connect(self.open_ris)
        self.evolution.clicked.connect(open_vadimky) # self.open_vadimk
        self.photo_hunt.clicked.connect(self.open_photo)

    def back_to_menu(self):
        if not self.menu_window:
            self.menu = Main_Menu()
        self.hide()
        self.menu.show()

    def open_jmak(self):
        self.jm = JmakolkaMainWindow()
        self.jm.show()
        # self.hide1()

    def open_ris(self):
        self.risov = RisovalkaMainWindow()
        self.risov.show()
        # elf.hide()

    def open_pchel(self):
        self.bird = FlappyMainWindow()
        self.bird.show()

    def open_photo(self):
        subprocess.run(["python", "files/photo_hunt/duck_hunt.py"])

def open_vadimky():
    EvolutionMainRun(WINDOW)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Menu()
    ex.show()
    sys.exit(app.exec_())



'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
# from files.main_window.main_menu_new import Ui_Form
from files.main_window.main_menu_interface import Ui_MainWindow
from jmakolka_last import My_Smth
from PyQt5.QtCore import QUrl, QRect
from PyQt5 import QtGui
from risovalka import MainWindow
from flappy import MainWindow as Birdcl
import vadimok_2048


class My(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Основное меню')

        self.vadimki_btn = QtWidgets.QPushButton(self)
        self.vadimki_btn.setGeometry(450, 450, 261, 51)
        self.vadimki_btn.setStyleSheet("background: rgb(255, 170, 0);")
        self.vadimki_btn.setText('2048 Вадимок')
        self.vadimki_btn.clicked.connect(self.open_vadimky)

        # Создание плейлиста и добавление музыкальной заставки
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("files/main_window/cook.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        # Создание объекта проигрывателя и добавление плейлиста
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)

        # Воспроизведение музыки при запуске приложения
        self.player.play()

        self.btn_jmak.clicked.connect(self.open_jmak)
        self.btn_ris.clicked.connect(self.open_ris)
        self.btn_perepol.clicked.connect(self.open_pchel)

    def open_vadimky(self):
        vadimok_2048.main(vadimok_2048.WINDOW)

    def open_jmak(self):
        self.jm = My_Smth()
        self.jm.show()
        # self.hide1()

    def open_ris(self):
        self.risov = MainWindow()
        self.risov.show()
        # elf.hide()

    def open_pchel(self):
        self.bird = Birdcl()
        self.bird.show()


app = QApplication(sys.argv)
ex = My()
ex.show()
sys.exit(app.exec_())
'''