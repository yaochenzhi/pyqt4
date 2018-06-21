import sys
import time
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("Hello PyQt4!")
        # self.setWindowIcon(QtGui.QIcon(''))

        extractAction = QtGui.QAction("&GET TO THE CHOPPATH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App!")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):

        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)

        # btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        # btn.resize(100, 100)
        btn.move(50,50)
        
        self.show()

    def close_application(self):
        print("Closing application ...")
        self.setWindowTitle("Closing application")
        time.sleep(2)
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    # GUI2 = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
