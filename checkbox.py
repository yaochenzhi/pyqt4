import os
import sys
import time
from PyQt4 import QtGui, QtCore


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
        btn.resize(btn.minimumSizeHint())
        btn.move(425,0)

        extractAction = QtGui.QAction(QtGui.QIcon(os.path.join(BASE_DIR,'python.png')), 'Flee the Scence', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)


        self.checkBox = QtGui.QCheckBox("Enlarge Window", self)
        self.checkBox.move(300, 0)
        # self.checkBox.toggle()
        self.checkBox.stateChanged.connect(self.enlarge_window)


        self.show()

    def enlarge_window(self):
        if self.checkBox.isChecked():
            print("Checked")
            self.setGeometry(500,500,1000,500)
        else:
            print("Uncheked")
            self.setGeometry(500,500,1000,100)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Extract!",
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting ")
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
