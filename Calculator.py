from math import *

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Calculator.ui', None)
        self.ui.show()

        self.ui.btn_0.clicked.connect(partial(self.func_number_x, 0))
        self.ui.btn_1.clicked.connect(partial(self.func_number_x, 1))
        self.ui.btn_2.clicked.connect(partial(self.func_number_x, 2))
        self.ui.btn_3.clicked.connect(partial(self.func_number_x, 3))
        self.ui.btn_4.clicked.connect(partial(self.func_number_x, 4))
        self.ui.btn_5.clicked.connect(partial(self.func_number_x, 5))
        self.ui.btn_6.clicked.connect(partial(self.func_number_x, 6))
        self.ui.btn_7.clicked.connect(partial(self.func_number_x, 7))
        self.ui.btn_8.clicked.connect(partial(self.func_number_x, 8))
        self.ui.btn_9.clicked.connect(partial(self.func_number_x, 9))

        self.ui.btn_sum.clicked.connect(partial(self.input_num1, '+'))
        self.ui.btn_sub.clicked.connect(partial(self.input_num1, '-'))
        self.ui.btn_multiply.clicked.connect(partial(self.input_num1, '*'))
        self.ui.btn_division.clicked.connect(partial(self.input_num1, '/'))

        self.ui.btn_equal.clicked.connect(self.equal)

        self.ui.btn_reset.clicked.connect(self.reset)
        
        self.ui.btn_symmetry.clicked.connect(self.symmetry)

        self.ui.btn_point.clicked.connect(self.decimal_point)

        self.ui.btn_percent.clicked.connect(self.percent)

        self.ui.btn_sin.clicked.connect(partial(self.function_x, 'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.function_x, 'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.function_x, 'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.function_x, 'cot'))
        self.ui.btn_log.clicked.connect(partial(self.function_x, 'log'))
        self.ui.btn_sqrt.clicked.connect(partial(self.function_x, 'sqrt'))

    def func_number_x(self, x):
        self.ui.textbox.setText(self.ui.textbox.text() + str(x))

    def input_num1(self, op):
        try:
            if self.ui.textbox.text() != '':
                self.num1 = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.operator = op
        except:
            self.ui.textbox.setText('Error')

    def equal(self):
        try:
            if self.ui.textbox.text() != '':
                self.num2 = float(self.ui.textbox.text())

                if self.operator == '+':
                    result = self.num1 + self.num2
                elif self.operator == '-':
                    result = self.num1 - self.num2
                elif self.operator == '*':
                    result = self.num1 * self.num2
                elif self.operator == '/':
                    result = self.num1 / self.num2
                
                self.ui.textbox.setText(str(result))
        except:
            self.ui.textbox.setText('Error')

    def reset(self):
        self.ui.textbox.setText('')

    def symmetry(self):
        if '-' in self.ui.textbox.text():
            negative = float(self.ui.textbox.text()) * -1
            self.ui.textbox.setText(str(negative))
        else:
            self.ui.textbox.setText('-' + self.ui.textbox.text())

    def decimal_point(self):
        if '.' not in self.ui.textbox.text() and self.ui.textbox.text() != '':
            self.ui.textbox.setText(self.ui.textbox.text() + '.')

    def percent(self):
        try:
            if self.ui.textbox.text() != '':
                cent = float(self.ui.textbox.text()) / 100
                self.ui.textbox.setText(str(cent))
        except:
            self.ui.textbox.setText('Error')       

    def function_x(self, t):
        try:
            if self.ui.textbox.text() != '':
                text = radians(float(self.ui.textbox.text()))

                if t == 'sin':
                    result = sin(text)
                elif t == 'cos':
                    result = cos(text)
                elif t == 'tan':
                    result = tan(text)
                elif t == 'cot':
                    result = cos(text) / sin(text)
                elif t == 'log':
                    result = log(float(self.ui.textbox.text()))
                elif t == 'sqrt':
                    result = sqrt(float(self.ui.textbox.text()))
                
                result = round(result, 6)
                self.ui.textbox.setText(str(result))
        except:
            self.ui.textbox.setText('Error')

app = QApplication()
window = Calculator()

app.exec()