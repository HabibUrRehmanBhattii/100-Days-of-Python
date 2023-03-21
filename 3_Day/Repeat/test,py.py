import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, \
    QAction


class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.grid_layout = None
        self.line_edit = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 250, 200)

        self.grid_layout = QGridLayout()
        self.line_edit = QLineEdit()
        self.grid_layout.addWidget(self.line_edit, 0, 0, 1, 4)

        self.createButton('7', 1, 0)
        self.createButton('8', 1, 1)
        self.createButton('9', 1, 2)
        self.createButton('/', 1, 3)

        self.createButton('4', 2, 0)
        self.createButton('5', 2, 1)
        self.createButton('6', 2, 2)
        self.createButton('*', 2, 3)

        self.createButton('1', 3, 0)
        self.createButton('2', 3, 1)
        self.createButton('3', 3, 2)
        self.createButton('-', 3, 3)

        self.createButton('0', 4, 0)
        self.createButton('.', 4, 1)
        self.createButton('=', 4, 2)
        self.createButton('+', 4, 3)

        self.setLayout(self.grid_layout)

    def createButton(self, text, row, col):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.buttonClicked(text))
        self.grid_layout.addWidget(button, row, col)

    def buttonClicked(self, text):
        if text == '=':
            result = eval(self.line_edit.text())
            self.line_edit.setText(str(result))
        elif text == 'C':
            self.line_edit.setText('')
        else:
            self.line_edit.setText(self.line_edit.text() + text)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.calculator = Calculator()
        self.setCentralWidget(self.calculator)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        exitAct = QAction('Exit', self)
        exitAct.triggered.connect(self.close)
        fileMenu.addAction(exitAct)

        self.setWindowTitle('Main Window')
        self.setGeometry(300, 300, 250, 200)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
