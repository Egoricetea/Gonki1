import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import Qt, QTimer,QRect
from PyQt5.QtGui import QPainter, QPixmap
import random


class CarGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hot Cars")
        self.setGeometry(960, 510, 300, 500)

        self.car_speed1 = 5
        self.car_speed2 = 2
        self.player_speed = 5
        self.car1_y = 50
        self.car2_y = 50
        self.player_x = 165

        self.rpice1_y = 0
        self.rpice2_y = -500
        self.road_image = QPixmap("sprites/road2.png")

        self.sprite1 = random.choice(
            [QPixmap("sprites/car1.png"),QPixmap("sprites/car2.png"),QPixmap("sprites/car3.png"),QPixmap("sprites/car4.png")
             ,QPixmap("sprites/car5.png"),QPixmap("sprites/car6.png")])
        self.car2_images = [
            QPixmap("sprites/pl_car1.png")]


        self.player_image = QPixmap("sprites/pl_car1.png")


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.movec)
        self.timer.start(50)



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        painter.drawPixmap(0, self.rpice1_y, self.width(), self.height(), self.road_image)
        painter.drawPixmap(0, self.rpice2_y, self.width(), self.height(), self.road_image)

        painter.drawPixmap(75, self.car1_y, self.sprite1)
        painter.drawPixmap(165, self.car2_y, QPixmap("sprites/pl_car1.png"))

        painter.drawPixmap(self.player_x, 400, self.player_image)

    def movec(self):
        self.car1_y += self.car_speed1
        self.car2_y += self.car_speed2


        self.rpice1_y += self.car_speed1
        self.rpice2_y += self.car_speed1

        if self.rpice1_y >= self.height():
            self.rpice1_y = self.rpice2_y-500
        if self.rpice2_y >= self.height():
            self.rpice2_y = self.rpice1_y-500



        if self.car1_y > self.height():
            self.car1_y = -100
            self.sprite1 = random.choice(
                [QPixmap("sprites/car1.png"), QPixmap("sprites/car2.png"), QPixmap("sprites/car3.png"),
                 QPixmap("sprites/car4.png")
                    , QPixmap("sprites/car5.png"), QPixmap("sprites/car6.png")])

        if self.car2_y > self.height():
            self.car2_y = -100

        if self.check_collision():
            self.timer.stop()
            QMessageBox.information(self, "Провал", "Вы потерпели крах)")
            self.close()
        self.repaint()

    def check_collision(self):
        player_rect = QRect(self.player_x, 400, 60, 98)
        car1_rect = QRect(75, self.car1_y, 60, 98)
        car2_rect = QRect(165, self.car2_y, 60, 98)

        if player_rect.intersects(car1_rect) or player_rect.intersects(car2_rect):
            return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        elif event.key() == Qt.Key_A:
            self.player_x -= self.player_speed
        elif event.key() == Qt.Key_D:
            self.player_x += self.player_speed


        elif event.key() == Qt.Key_W:
            if self.car_speed1 <12:
                self.car_speed1+=1
                self.car_speed2+=1
        elif event.key() == Qt.Key_S:
            if self.car_speed1 >5:
                self.car_speed1-=1
                self.car_speed2-=1
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CarGame()
    mainWindow.show()
    sys.exit(app.exec_())
