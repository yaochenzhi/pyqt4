import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("Hello PyQt4!")
        # self.setWindowIcon(QtGui.QIcon(''))
        self.show()


app = QtGui.QApplication(sys.argv)
GUI = Window()
# GUI2 = Window()
sys.exit(app.exec_())