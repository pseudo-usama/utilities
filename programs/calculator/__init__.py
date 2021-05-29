import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from .main_window import Ui_MainWindow


class Calculator:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.do_some_initialization()

        MainWindow.show()
        sys.exit(app.exec_())

    def do_some_initialization(self):
        self.equation_txtEdit = self.ui.equation_txtEdit
        self.ans_lbl = self.ui.eq_answer_lbl

        self.equation_txtEdit.textChanged.connect(self.evaluate)

    def set_ans(self, text):
        self.ans_lbl.setText(text)
    def get_eq(self):
        return self.equation_txtEdit.toPlainText()

    def evaluate(self):
        eq = self.get_eq()

        if eq == '':
            self.set_ans('')            
            return

        try:
            ans = str(eval(eq))
            self.set_ans(ans)
        except Exception as e:
            self.set_ans(str(e))


def start():
    Calculator()


if __name__ == '__main__':
    Calculator()
