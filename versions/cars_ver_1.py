import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor


class CarGame(QWidget):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    game = CarGame()
    window.setCentralWidget(game)
    window.setWindowTitle('Hot Cars')
    window.resize(450, 700)
    window.show()
    sys.exit(app.exec_())