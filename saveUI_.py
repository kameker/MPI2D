import sys

from PyQt5 import QtWidgets
from saveUI import Ui_SaveWindow


class ExampleApp(QtWidgets.QMainWindow, Ui_SaveWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_button.clicked.connect(self.save_file)

    def save_file(self):
        with open("name.txt", "w") as file:
            if self.name.text():
                file.write(self.name.text())


def sf():
    app2 = QtWidgets.QApplication(sys.argv)
    window2 = ExampleApp()
    window2.show()
    app2.exec_()
