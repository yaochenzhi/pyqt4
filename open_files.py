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

        # EDITOR
        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open the editor")
        openEditor.triggered.connect(self.editor)

        # OPEN FILE
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_open)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)

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


        # FONT WIDGET
        fontChoice = QtGui.QAction(QtGui.QIcon(os.path.join(BASE_DIR,'python.png')), 'Flee the Scence', self)
        fontChoice.triggered.connect(self.font_choice)
        # self.addToolBar("Font")
        # self.toolbar = self.addToolBar("Font")
        self.toolbar.addAction(fontChoice)


        # COLOR PICKER WIDGET
        color = QtGui.QColor(0, 0, 0)
        print(color.name())

        fontColor =QtGui.QAction("Font bg color", self)
        fontColor.triggered.connect(self.color_picker)

        self.toolbar.addAction(fontColor)


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


        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)


        self.show()


    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

        self.editor()
        with file:
            text = file.read()
            self.textEditor.setText(text)

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" %color.name())

    def editor(self):
        self.textEditor = QtGui.QTextEdit()
        self.setCentralWidget(self.textEditor)



    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


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
