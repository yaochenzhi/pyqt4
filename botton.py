import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("Hello PyQt4!")
        # self.setWindowIcon(QtGui.QIcon(''))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        btn.resize(100, 100)
        btn.move(50,50)
        
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    # GUI2 = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()

