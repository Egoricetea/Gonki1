import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import Qt, QTimer,QRect
from PyQt5.QtGui import QPainter, QPixmap
import random
from random import randint


class CarGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Гонки")
        self.setGeometry(480, 255, 800, 500)

        self.car_speed1 = 20
        self.car_speed5 = randint(21, 28)
        self.car_speed6 = randint(21, 28)

        self.car_speed2 = randint(2 ,4)
        self.car_speed3 = randint(2, 4)
        self.car_speed4 = randint(2, 4)

        self.player_speed = 6
        self.road_moove = 15
        self.car1_y = randint(-100 ,70)
        self.car5_y = randint(-500, 70)
        self.car6_y = randint(-200, 70)

        self.car2_y = randint(-700,20)
        self.car3_y = randint(-500, 60)
        self.car4_y = randint(-200, 35)

        self.player_x = 535
        self.points=0

        self.rpice1_y = 0
        self.rpice2_y = -496
        self.road_image = QPixmap("sprites/road3.png")

        self.sprite1 = random.choice(
            [QPixmap("sprites/car1.png"),QPixmap("sprites/car2.png"),QPixmap("sprites/car3.png"),QPixmap("sprites/car4.png")
             ,QPixmap("sprites/car5.png"),QPixmap("sprites/car6.png")])
        self.sprite2 = random.choice(
            [QPixmap("sprites/car1.png"),QPixmap("sprites/car2.png"),QPixmap("sprites/car3.png"),QPixmap("sprites/car4.png")
             ,QPixmap("sprites/car5.png"),QPixmap("sprites/car6.png")])
        self.sprite3 = random.choice(
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

        painter.drawPixmap(95, self.car1_y, self.sprite1)
        painter.drawPixmap(205, self.car5_y, self.sprite2)
        painter.drawPixmap(310, self.car6_y, self.sprite3)

        painter.drawPixmap(535, self.car2_y, QPixmap("sprites/pl_car1.png"))
        painter.drawPixmap(640, self.car3_y, QPixmap("sprites/pl_car1.png"))
        painter.drawPixmap(430, self.car4_y, QPixmap("sprites/pl_car1.png"))

        painter.drawPixmap(self.player_x, 340, self.player_image)

    def movec(self):
        self.car1_y += self.car_speed1
        self.car5_y += self.car_speed5
        self.car6_y += self.car_speed6

        self.car2_y += self.car_speed2
        self.car3_y += self.car_speed3
        self.car4_y += self.car_speed4


        self.rpice1_y += self.road_moove
        self.rpice2_y += self.road_moove

        if self.rpice1_y >= self.height():
            self.rpice1_y = self.rpice2_y-496
        if self.rpice2_y >= self.height():
            self.rpice2_y = self.rpice1_y-496



        if self.car1_y > self.height():
            self.car1_y = randint(-1200,-800)
            self.sprite1 = random.choice(
                [QPixmap("sprites/car1.png"), QPixmap("sprites/car2.png"), QPixmap("sprites/car3.png"),
                 QPixmap("sprites/car4.png")
                    , QPixmap("sprites/car5.png"), QPixmap("sprites/car6.png")])
            self.points+=100
            print(self.points)

        if self.car2_y > self.height():
            self.car2_y = randint(-500,-100)
            self.points += 100
            print(self.points)

        if self.car3_y > self.height():
            self.car3_y = randint(-700,-50)
            self.points += 100
            print(self.points)

        if self.car4_y > self.height():
            self.car4_y = randint(-400,-70)
            self.points += 100
            print(self.points)

        if self.car5_y > self.height():
            self.car5_y = randint(-1200,-800)
            self.sprite2 = random.choice(
                [QPixmap("sprites/car1.png"), QPixmap("sprites/car2.png"), QPixmap("sprites/car3.png"),
                 QPixmap("sprites/car4.png")
                    , QPixmap("sprites/car5.png"), QPixmap("sprites/car6.png")])
            self.points += 100
            print(self.points)

        if self.car6_y > self.height():
            self.car6_y = randint(-1200,-800)
            self.sprite3 = random.choice(
                [QPixmap("sprites/car1.png"), QPixmap("sprites/car2.png"), QPixmap("sprites/car3.png"),
                 QPixmap("sprites/car4.png")
                    , QPixmap("sprites/car5.png"), QPixmap("sprites/car6.png")])
            self.points += 100
            print(self.points)

        if self.check_collision():
            self.timer.stop()
            QMessageBox.information(self, "Провал", "Вы потерпели крах)")
            self.close()
        self.repaint()

    def check_collision(self):
        player_rect = QRect(self.player_x, 340, 60, 98)
        car1_rect = QRect(95, self.car1_y, 60, 98)
        car2_rect = QRect(535, self.car2_y, 60, 98)
        car3_rect = QRect(640, self.car3_y, 60, 98)
        car4_rect = QRect(430, self.car4_y, 60, 98)
        car5_rect = QRect(205, self.car5_y, 60, 98)
        car6_rect = QRect(310, self.car6_y, 60, 98)

        if player_rect.intersects(car1_rect) or player_rect.intersects(car2_rect) or player_rect.intersects(car3_rect) or player_rect.intersects(car4_rect)\
                or player_rect.intersects(car5_rect) or player_rect.intersects(car6_rect):
            return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

        elif event.key() == Qt.Key_Left:
            self.player_x -= self.player_speed
        elif event.key() == Qt.Key_Right:
            self.player_x += self.player_speed


        elif event.key() == Qt.Key_Up:
            if self.car_speed1 <28:
                self.car_speed1+=1
                self.car_speed2+=1
                self.car_speed3+=1
                self.car_speed4+=1
                self.car_speed5+=1
                self.car_speed6+=1
                self.road_moove+=1
        elif event.key() == Qt.Key_Down:
            if self.car_speed1 >20:
                self.car_speed1-=1
                self.car_speed2-=1
                self.car_speed3-=1
                self.car_speed4-=1
                self.car_speed5-=1
                self.car_speed6-=1
                self.road_moove-=1
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CarGame()
    mainWindow.show()
    sys.exit(app.exec_())
