import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from files.jmakolka.interface_jmakolks import Ui_Happy_Jmakolka
from PyQt5.QtCore import Qt, QTimer
import random
import csv
from files.jmakolka.tale_adder_interface import Ui_Form_TaleAdder


class TaleAdder(QtWidgets.QWidget, Ui_Form_TaleAdder):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)
        self.name_of_tale = ''
        self.icontale = ''
        self.winskreen = ''
        self.hero_1 = ''
        self.hero_2 = ''
        self.hero_3 = ''
        self.activation()

    def activation(self):
        self.icontaleadder.clicked.connect(self.icontale_add)
        self.winskrennadder.clicked.connect(self.winskreen_add)
        self.heroadder_1.clicked.connect(self.hero_1_add)
        self.heroadder_2.clicked.connect(self.hero_2_add)
        self.heroadder_3.clicked.connect(self.hero_3_add)
        self.add_tale_button.clicked.connect(self.add_tale)

    def icontale_add(self):
        self.icontale = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.taleicon_txt.setText(self.icontale.split('/')[-1])

    def winskreen_add(self):
        self.winskreen = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.winskreen_txt.setText(self.winskreen.split('/')[-1])

    def hero_1_add(self):
        self.hero_1 = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.hero_txt_1.setText(self.hero_1.split('/')[-1])

    def hero_2_add(self):
        self.hero_2 = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.hero_txt_2.setText(self.hero_2.split('/')[-1])

    def hero_3_add(self):
        self.hero_3 = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.hero_txt_3.setText(self.hero_3.split('/')[-1])

    def add_tale(self):
        print(f'{self.name_tale};{self.winskreen};{self.icontale};{self.hero_1};{self.hero_2};{self.hero_3}')
        self.name_of_tale = self.name_tale.text()
        if self.name_of_tale and self.icontale and self.winskreen and self.hero_1 and self.hero_2 and self.hero_3:
            with open('files/jmakolka/jmakolka.csv', 'w', encoding='utf-8') as f:
                # [name;url_mainpict;url_avatar;url_firstperson;url_secondperson;url_thirdperson]
                f.write(f'{self.name_of_tale};{self.winskreen};{self.icontale};{self.hero_1};{self.hero_2};{self.hero_3}')
                f.close()
        self.close()


class JmakolkaMainWindow(QMainWindow, Ui_Happy_Jmakolka):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buff = ""
        self.timer = QTimer(self)
        self.setWindowTitle('Жмаколка')

        self.gener()
        self.pobed_screen()

        self.obh = ["134", "412", "314"]
        self.pushButton_3.clicked.connect(self.run)

        self.reb_but = QtWidgets.QPushButton(self)
        self.reb_but.setGeometry(1510, 850, 280, 101)
        self.reb_but.setText('Начать заново')
        self.reb_but.setStyleSheet('background:rgb(255, 255, 127)')
        self.reb_but.clicked.connect(self.reboot)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.reb_but.setFont(font)
        self.toolButton.clicked.connect(self.back)
        self.reb_but.hide()
        self.pushButton_3.hide()

        self.add_tale_button = QtWidgets.QPushButton(self)
        self.add_tale_button.setGeometry(1520, 10, 231, 150)
        self.add_tale_button.setStyleSheet("background: white")
        self.add_tale_button.setText('Добавить сказку')
        self.add_tale_button.clicked.connect(self.add_tale)

    def gener(self):
        with open('files/jmakolka/jmakolka.csv', encoding='UTF-8') as f:
            # options = [name; url_mainpict; url_avatar; url_firstperson; url_secondperson; url_thirdperson]
            options = csv.reader(f, delimiter=';')
            options = [tuple(i) for i in options]
            main_tale = random.choice(options)
            options.remove(main_tale)

            self.fon_pob = (main_tale[0], main_tale[1])

            other_tales = random.choices(options, k=1)

            # combination = [''.join(random.choices(['1', '2', '3', '4'], k=3)) for _ in range(2)]
            combination = [''.join(random.choices(['1', '3', '4'], k=3)) for _ in range(2)]
            self.pob_comb = random.choice(combination)
            combination.remove(self.pob_comb)

            combinations = [(self.pob_comb, main_tale[2]), (combination[0], other_tales[0][2])]
            random.shuffle(combinations)

            self.peris_main = main_tale[3:]

            self.image_1.setStyleSheet(f'background:url({self.peris_main[0]})')
            self.image_2.setStyleSheet(f'background:url({self.peris_main[1]})')
            self.image_3.setStyleSheet(f'background:url({self.peris_main[2]})')

            self.nums_1.setText(combinations[0][0])
            # fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            # print(fname)
            avatar_1 = QPixmap(combinations[0][1])
            self.image_4.setPixmap(avatar_1)

            self.nums_2.setText(combinations[1][0])
            avatar_2 = QPixmap(combinations[1][1])
            self.image_5.setPixmap(avatar_2)

            # self.label_4.setText(combinations[1][1])

    def add_tale(self):
        self.adder = TaleAdder()
        self.adder.show()

    def keyPressEvent(self, event):
        symbol = "-"
        if event.key() == Qt.Key_1:
            symbol = "1"
        elif event.key() == Qt.Key_2:
            symbol = "2"
        elif event.key() == Qt.Key_3:
            symbol = "3"
        elif event.key() == Qt.Key_4:
            symbol = "4"
        
        if self.input_1.text() == "-":
            self.buff += symbol
            self.input_1.setText(symbol)
        elif self.input_2.text() == "-":
            self.buff += symbol
            self.input_2.setText(symbol)
        elif self.input_3.text() == "-":
            self.buff += symbol
            self.input_3.setText(symbol)

            if self.buff == self.pob_comb:
                for _ in range(3):
                    self.frame_16.setStyleSheet('background: rgb(0, 255, 0)')
                    self.frame_15.setStyleSheet('background: rgb(0, 255, 0)')
                    self.frame_14.setStyleSheet('background: rgb(0, 255, 0)')
                self.dark_fon.show()
            else:
                for _ in range(3):
                    self.frame_16.setStyleSheet('background: rgb(255, 0, 0)')
                    self.frame_15.setStyleSheet('background: rgb(255, 0, 0)')
                    self.frame_14.setStyleSheet('background: rgb(255, 0, 0)')
                self.reb_but.show()
            self.buff = ""

    def pobed_screen(self):
        self.dark_fon = QtWidgets.QFrame(self)
        self.dark_fon.setGeometry(0, 0, 1920, 1080)
        self.dark_fon.setStyleSheet('background: rgba(0, 0, 0, 0.5)')

        skazk_pict = QtWidgets.QFrame(self.dark_fon)
        skazk_pict.setGeometry(340, 90, 1280, 799)
        skazk_pict.setStyleSheet(f'background: url({self.fon_pob[1]})')

        skazka_podpis_fr = QtWidgets.QFrame(self.dark_fon)
        skazka_podpis_fr.setGeometry(670, 910, 601, 81)
        skazka_podpis_fr.setStyleSheet('background:rgb(255, 255, 127)')

        skazka_podpis = QtWidgets.QLabel(skazka_podpis_fr)
        skazka_podpis.setGeometry(60, 10, 511, 75)
        skazka_podpis.setText(f'{self.fon_pob[0]}')
        font = QtGui.QFont()
        font.setPointSize(24)
        skazka_podpis.setFont(font)

        reboot_button = QtWidgets.QPushButton(self.dark_fon)
        reboot_button.setGeometry(1640, 570, 251, 101)
        reboot_button.setText('Начать заново')
        font = QtGui.QFont()
        font.setPointSize(20)
        reboot_button.setFont(font)
        reboot_button.setStyleSheet('background:rgb(255, 255, 127)')
        reboot_button.clicked.connect(self.reboot)

        back_button = QtWidgets.QPushButton(self.dark_fon)
        back_button.setGeometry(1640, 410, 251, 101)
        back_button.setText('В главное меню')
        font = QtGui.QFont()
        font.setPointSize(20)
        back_button.setFont(font)
        back_button.setStyleSheet('background:rgb(255, 255, 127)')
        back_button.clicked.connect(self.back)

        self.dark_fon.hide()

    def reboot(self):
        self.frame_16.setStyleSheet('background: rgb(0, 0, 255)')
        self.frame_15.setStyleSheet('background: rgb(0, 0, 255)')
        self.frame_14.setStyleSheet('background: rgb(0, 0, 255)')

        self.input_1.setText('-')
        self.input_2.setText('-')
        self.input_3.setText('-')

        self.dark_fon.hide()
        self.reb_but.hide()
        self.gener()
        self.pobed_screen()

    def back(self):
        self.hide()

    def run(self):
        self.pushButton_3.hide()
        a = list(open('jm.txt').read().split())
        self.input_1.setText(a[0])
        self.input_2.setText(a[1])
        self.input_3.setText(a[2])
        if ''.join(a) in self.obh:
            self.dark_fon.show()
        else:
            self.frame_16.setStyleSheet('background: rgb(255, 0, 0)')
            self.frame_15.setStyleSheet('background: rgb(255, 0, 0)')
            self.frame_14.setStyleSheet('background: rgb(255, 0, 0)')
            self.reb_but.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = JmakolkaMainWindow()
    ex.show()
    sys.exit(app.exec_())

