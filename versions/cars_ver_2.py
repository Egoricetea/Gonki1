import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor


class CarGame(QWidget):
    def __init__(self):
        super().__init__()



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(80, 50, 30, 50)

        painter.setBrush(QColor(0, 0, 255))
        painter.drawRect(180, 50, 30, 50)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    game = CarGame()
    window.setCentralWidget(game)
    window.setWindowTitle('Hot Cars'')
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec_())
    