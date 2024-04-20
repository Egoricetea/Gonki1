import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor


class CarGame(QWidget):
    def __init__(self):
        super().__init__()
        self.car_speed1 = 5
        self.car_speed2 = 2
        self.car1_y = 50
        self.car2_y = 50

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.movec)
        self.timer.start(50)



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(80, self.car1_y, 30, 50)

        painter.setBrush(QColor(0, 0, 255))
        painter.drawRect(180, self.car2_y, 30, 50)

    def movec(self):
        self.car1_y += self.car_speed1
        self.car2_y += self.car_speed2
        self.repaint()
        if self.car1_y > self.height():
            self.car1_y = -50
        if self.car2_y > self.height():
            self.car2_y = -50




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    game = CarGame()
    window.setCentralWidget(game)
    window.setWindowTitle('Hot cars')
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec_())