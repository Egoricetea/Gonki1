import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import Qt, QTimer,QRect
from PyQt5.QtGui import QPainter, QColor, QPixmap


class CarGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hot Cars")
        self.setGeometry(960, 510, 300, 500)

        self.car_speed1 = 5
        self.car_speed2 = 2
        self.player_speed = 24
        self.car1_y = 50
        self.car2_y = 50
        self.player_x = 132


        self.rpice1_y = 0
        self.rpice2_y = -500
        self.road_image = QPixmap("sprites/road2.png")


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.movec)
        self.timer.start(50)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        painter.drawPixmap(0, self.rpice1_y, self.width(), self.height(), self.road_image)
        painter.drawPixmap(0, self.rpice2_y, self.width(), self.height(), self.road_image)

        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(84, self.car1_y, 30, 50)

        painter.setBrush(QColor(0, 0, 255))
        painter.drawRect(180, self.car2_y, 30, 50)

        painter.setBrush(QColor(0, 255, 0))
        painter.drawRect(self.player_x, 400, 30, 50)

    def movec(self):
        self.car1_y += self.car_speed1
        self.car2_y += self.car_speed2


        self.rpice1_y += self.car_speed1
        self.rpice2_y += self.car_speed1
        if self.rpice1_y >= self.height():
            self.rpice1_y = self.rpice2_y-500
        self.repaint()
        if self.rpice2_y >= self.height():
            self.rpice2_y = self.rpice1_y-500
        self.repaint()

        if self.car1_y > self.height():
            self.car1_y = -50
        if self.car2_y > self.height():
            self.car2_y = -50

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        elif event.key() == Qt.Key_A:
            self.player_x -= self.player_speed
            self.repaint()
        elif event.key() == Qt.Key_D:
            self.player_x += self.player_speed
            self.repaint()

        elif event.key() == Qt.Key_W:
            if self.car_speed1 <10:
                self.car_speed1+=1
                self.car_speed2+=1
        elif event.key() == Qt.Key_S:
            if self.car_speed1 >5:
                self.car_speed1-=1
                self.car_speed2-=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CarGame()
    mainWindow.show()
    sys.exit(app.exec_())
