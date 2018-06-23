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


        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(300, 200, 200, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(300, 300)
        self.btn.clicked.connect(self.download)


        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel(self.style().objectName(), self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50, 200)
        comboBox.activated[str].connect(self.style_choice)


        self.show()


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)



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
