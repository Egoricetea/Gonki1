import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor


class CarGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.car_speed1 = 5
        self.car_speed2 = 2
        self.player_speed = 30

        self.car1_y = 50
        self.car2_y = 50
        self.player_x = 130

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

        painter.setBrush(QColor(0, 255, 0))
        painter.drawRect(self.player_x, 50, 30, 50)

    def movec(self):
        self.car1_y += self.car_speed1
        self.car2_y += self.car_speed2
        self.repaint()
        if self.car1_y > self.height():
            self.car1_y = -50
        if self.car2_y > self.height():
            self.car2_y = -50

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_A:
            self.player_x -= self.player_speed
            self.repaint()
        elif event.key() == Qt.Key_D:
            self.player_x += self.player_speed
            self.repaint()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CarGame()
    mainWindow.show()
    sys.exit(app.exec_())
