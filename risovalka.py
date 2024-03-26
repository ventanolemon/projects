import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt, QPoint, QTimer, QRect
from PyQt5.QtGui import QPainter, QPen, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame, QGridLayout, QToolButton, QHBoxLayout, QSizePolicy, QPushButton
from PyQt5 import QtGui


class RisovalkaMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_width = 640
        self.video_height = 440

        self.setWindowTitle('Happy_Risovalka')
        self.setGeometry(0, 0, 1920, 1080)

        # Set background image
        self.frame_12 = QFrame(self)
        self.frame_12.setGeometry(QRect(0, 0, 1920, 1080))
        self.frame_12.setStyleSheet(
            "background: url(files/risovalka/background_img.jpg);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        '''
        background_image = QImage('/fon.bmp')
        background_image = background_image.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)'''

        self.back_button = QPushButton(self)
        self.back_button.setGeometry(1650, 900, 251, 101)
        self.back_button.setText('В главное меню')
        self.back_button.setStyleSheet('background:rgb(255, 255, 127)')
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back_button.setFont(font)
        self.back_button.clicked.connect(self.back_menu)
        self.back_button.hide()

        self.drawing_widget = DrawingWidget()
        self.drawing_widget.setGeometry(0, 0, 1300, 700)

        layout = QVBoxLayout()
        layout.addWidget(self.drawing_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Add right frame with tool buttons
        frame = QFrame()
        frame.setFixedHeight(150)
        frame_layout = QHBoxLayout()
        frame.setLayout(frame_layout)

        self.pen = QPen(Qt.blue, 8, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        # Apply styles
        button_size = 100
        button_radius = button_size // 2

        button_style = f"""
            width: {button_size}px;
            height: {button_size}px;
            border-radius: {button_radius}px;
        """

        green_button = QToolButton()
        green_button.setStyleSheet("background-color: rgb(0, 255, 0);" + button_style)
        green_button.setFixedSize(100, 100)
        green_button.clicked.connect(lambda: self.drawing_widget.set_pen_color(Qt.green))
        frame_layout.addWidget(green_button)

        blue_button = QToolButton()
        blue_button.setStyleSheet("background-color: blue;" + button_style)
        blue_button.setFixedSize(100, 100)
        blue_button.clicked.connect(lambda: self.drawing_widget.set_pen_color(Qt.blue))
        frame_layout.addWidget(blue_button)

        red_button = QToolButton()
        red_button.setStyleSheet("background-color: red;" + button_style)
        red_button.setFixedSize(100, 100)
        red_button.clicked.connect(lambda: self.drawing_widget.set_pen_color(Qt.red))
        frame_layout.addWidget(red_button)

        yellow_button = QToolButton()
        yellow_button.setStyleSheet("background-color: yellow;" + button_style)
        yellow_button.setFixedSize(100, 100)
        yellow_button.clicked.connect(lambda: self.drawing_widget.set_pen_color(Qt.yellow))
        frame_layout.addWidget(yellow_button)

        # кнопка для очистки экрана
        clear_button = QToolButton()
        clear_button.setStyleSheet("background-color: white;" + button_style)
        clear_button.setFixedSize(100, 100)
        clear_button.clicked.connect(self.drawing_widget.clear_screen)
        clear_button.move(750, 900)
        frame_layout.addWidget(clear_button)


        layout.addWidget(frame)

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.capture_frame)
        self.timer.start(1000//60)  # Update at 30 fps

    def back_menu(self):
        print('lll')
        self.hide()

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        green_ball_center = self.detect_green_ball(frame)

        if green_ball_center is not None:
            x, y = green_ball_center

            # x = int(x * self.drawing_widget.width() / self.video_width)
            y = int(y * self.drawing_widget.height() / self.video_height)

            x = int((self.video_width - x) * self.drawing_widget.width() / self.video_width)
            # y = int(self.video_height - y * self.drawing_widget.height() / self.video_height)

            self.drawing_widget.add_point((x, y))

    def detect_green_ball(self, frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([21, 17, 50])
        upper_green = np.array([42, 153, 142])
        mask = cv2.inRange(hsv_frame, lower_green, upper_green)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return None

        max_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(max_contour) < 500:
            return None

        ((x, y), radius) = cv2.minEnclosingCircle(max_contour)
        center = (int(x), int(y))

        return center


class DrawingWidget(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(0, 0, 1920, 1080)
        self.lines = []
        self.current_line = []
        self.pen = QPen(Qt.blue, 80, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.points = []
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.background_image = QImage('bukva_O.jpg')
        # Apply styles
        self.setStyleSheet("""
            border: 5px solid rgb(0, 0, 0);
            border-radius: 100px;
            padding: 15px;
            background: rgb(255, 255, 255);
        """)

    def add_point(self, point):
        self.current_line.append(QPoint(*point))
        self.update()

    def set_pen_color(self, color):
        if self.current_line:
            self.lines.append((self.pen.color(), self.current_line))
            self.current_line = []
        self.pen.setColor(color)

    def clear_screen(self):
        """функция для очистки экрана"""
        self.lines.clear()
        self.current_line.clear()
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        widget_center = self.rect().center()
        image_center = self.background_image.rect().center()
        offset_x = widget_center.x() - image_center.x()
        offset_y = widget_center.y() - image_center.y()
        painter.drawImage(offset_x, offset_y, self.background_image)
        for color, line in self.lines:
            painter.setPen(QPen(color, 80, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            if len(line) > 1:
                for i in range(len(line) - 1):
                    painter.drawLine(line[i], line[i + 1])
        painter.setPen(self.pen)

        if len(self.current_line) > 1:
            for i in range(len(self.current_line) - 1):
                painter.drawLine(self.current_line[i], self.current_line[i + 1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RisovalkaMainWindow()
    window.show()
    sys.exit(app.exec_())
