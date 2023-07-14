from PyQt5.QtWidgets import QMainWindow, QDialog
from gui.InterfaceBasic import Ui_MainWindowBasic
from gui.InterfaceScientific import Ui_MainWindowScientific
from calculator import Calculator
from gui.About import Ui_About
import math


class ChangeMode():
    def __init__(self):
        ChangeMode.basic = AppControllerBasic()
        ChangeMode.scientific = AppControllerScientific()

class AppControllerBasic(QMainWindow, Ui_MainWindowBasic): 
    def __init__(self): 
        super().__init__() 
        super().setupUi(self)

        self.clear = False
        self.lineEdit.setText("0")

        # Calculator
        self.calculator = Calculator()

        # Connecting the signal 
        self.pushButton_c.clicked.connect(self.clear_c)
        self.pushButton_0.clicked.connect(self.inputDigit_0)
        self.pushButton_1.clicked.connect(self.inputDigit_1)
        self.pushButton_2.clicked.connect(self.inputDigit_2)
        self.pushButton_3.clicked.connect(self.inputDigit_3)
        self.pushButton_4.clicked.connect(self.inputDigit_4)
        self.pushButton_5.clicked.connect(self.inputDigit_5)
        self.pushButton_6.clicked.connect(self.inputDigit_6)
        self.pushButton_7.clicked.connect(self.inputDigit_7)
        self.pushButton_8.clicked.connect(self.inputDigit_8)
        self.pushButton_9.clicked.connect(self.inputDigit_9)
        self.pushButton_sum.clicked.connect(self.selectOp_sum)
        self.pushButton_prod.clicked.connect(self.selectOp_prod)
        self.pushButton_div.clicked.connect(self.selectOp_div)
        self.pushButton_sub.clicked.connect(self.selectOp_sub)
        self.pushButton_per.clicked.connect(self.selectOp_per)
        self.pushButton_eq.clicked.connect(self.selectOp_eq)
        self.pushButton_dot.clicked.connect(self.inputDigit_dot)
        self.pushButton_sig.clicked.connect(self.selectOp_sig)
        self.actionScientific.triggered.connect(self.SwitchMode)
        self.actionLicence.triggered.connect(self.about)

    def about(self):
        Dialog = QDialog()
        ui = Ui_About()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def SwitchMode(self):
        ChangeMode.basic.hide()
        ChangeMode.scientific.show()

    def clear_c(self):
        self.lineEdit.clear()
        self.lineEdit.setText("0")

    def inputDigit_0(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "0")

    def inputDigit_1(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "1")

    def inputDigit_2(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "2")

    def inputDigit_3(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "3")

    def inputDigit_4(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "4")

    def inputDigit_5(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "5")

    def inputDigit_6(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "6")

    def inputDigit_7(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "7")

    def inputDigit_8(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "8")

    def inputDigit_9(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "9")
    
    def selectOp_sum(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("+")
        self.clear = True

    def selectOp_prod(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("*")
        self.clear = True

    def selectOp_div(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("/")
        self.clear = True

    def selectOp_sub(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("-")
        self.clear = True

    def selectOp_per(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("%")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()
    
    def inputDigit_dot(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        text = self.lineEdit.text()
        self.lineEdit.setText(text + ".") 

    def selectOp_sig(self):
        text = self.lineEdit.text()
        if text[0] == "-":
            text = text.replace("-", "")
            self.lineEdit.setText(text)
        else:
            self.lineEdit.setText("-" + text)
        
    def selectOp_eq(self):
        secondNumber = self.lineEdit.text()
        self.calculator.setSecondNumber(secondNumber)
        
        result = self.calculator.CalculateResult()
        strResult = str(result)
        if strResult[-1] == '0' and strResult[-2] == '.':
            strResult = strResult.replace(".0", "")

        self.lineEdit.setText(strResult)
        self.calculator.reset()
        self.clear = True

class AppControllerScientific(QMainWindow, Ui_MainWindowScientific): 
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.clear = False
        self.lineEdit.setText("0")

        # Calculator
        self.calculator = Calculator()

        # Connecting the signal 
        self.pushButton_c.clicked.connect(self.clear_c)
        self.pushButton_0.clicked.connect(self.inputDigit_0)
        self.pushButton_1.clicked.connect(self.inputDigit_1)
        self.pushButton_2.clicked.connect(self.inputDigit_2)
        self.pushButton_3.clicked.connect(self.inputDigit_3)
        self.pushButton_4.clicked.connect(self.inputDigit_4)
        self.pushButton_5.clicked.connect(self.inputDigit_5)
        self.pushButton_6.clicked.connect(self.inputDigit_6)
        self.pushButton_7.clicked.connect(self.inputDigit_7)
        self.pushButton_8.clicked.connect(self.inputDigit_8)
        self.pushButton_9.clicked.connect(self.inputDigit_9)
        self.pushButton_sum.clicked.connect(self.selectOp_sum)
        self.pushButton_prod.clicked.connect(self.selectOp_prod)
        self.pushButton_div.clicked.connect(self.selectOp_div)
        self.pushButton_sub.clicked.connect(self.selectOp_sub)
        self.pushButton_per.clicked.connect(self.selectOp_per)
        self.pushButton_eq.clicked.connect(self.selectOp_eq)
        self.pushButton_dot.clicked.connect(self.inputDigit_dot)
        self.pushButton_sig.clicked.connect(self.selectOp_sig)
        self.pushButton_fact.clicked.connect(self.selectOp_fact) #fatorial
        self.pushButton_in.clicked.connect(self.selectOp_In) #logaritmo
        self.pushButton_log.clicked.connect(self.selectOp_log) # logaritmo base 10
        self.pushButton_raiz.clicked.connect(self.selectOp_raiz) # raiz
        self.pushButton_pow.clicked.connect(self.selectOp_pow) # potencia
        self.pushButton_pi.clicked.connect(self.InputDigit_pi) # pi
        self.pushButton_sin.clicked.connect(self.selectOp_sin) # seno em radiano
        self.pushButton_cos.clicked.connect(self.selectOp_cos) # cosseno em radiano
        self.pushButton_tan.clicked.connect(self.selectOp_tan) # tangente em radiano
        self.pushButton_eps.clicked.connect(self.selectOp_eps) # epsilon 
        self.actionBasic.triggered.connect(self.SwitchMode)
        self.actionLicence.triggered.connect(self.about)

    def about(self):
        Dialog = QDialog()
        ui = Ui_About()
        ui.setupUi(Dialog)
        Dialog.exec_()

    def SwitchMode(self):
        ChangeMode.scientific.hide()
        ChangeMode.basic.show()

    def clear_c(self):
        self.lineEdit.clear()
        self.lineEdit.setText("0")

    def inputDigit_0(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "0")

    def inputDigit_1(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "1")

    def inputDigit_2(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "2")

    def inputDigit_3(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "3")

    def inputDigit_4(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "4")

    def inputDigit_5(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "5")

    def inputDigit_6(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "6")

    def inputDigit_7(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "7")

    def inputDigit_8(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "8")

    def inputDigit_9(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        if self.lineEdit.text() == "0":
            self.lineEdit.clear()
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "9")
    
    def selectOp_sum(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("+")
        self.clear = True

    def selectOp_prod(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("*")
        self.clear = True

    def selectOp_div(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("/")
        self.clear = True

    def selectOp_sub(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("-")
        self.clear = True

    def selectOp_per(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("%")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()
    
    def inputDigit_dot(self):
        if self.clear is True:
            self.lineEdit.clear()
            self.lineEdit.setText("0")
            self.clear = False
        text = self.lineEdit.text()
        self.lineEdit.setText(text + ".") 

    def selectOp_sig(self):
        text = self.lineEdit.text()
        if text[0] == "-":
            text = text.replace("-", "")
            self.lineEdit.setText(text)
        else:
            self.lineEdit.setText("-" + text)
        
    def selectOp_fact(self): 
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("x!")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()
        
    def selectOp_In(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("In")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()

    def selectOp_log(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("log")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()
    
    def selectOp_raiz(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("√")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()

    def selectOp_pow(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("pow")
        self.clear = True

    def InputDigit_pi(self):
        self.lineEdit.clear()
        self.lineEdit.setText(str(math.pi))

    def selectOp_sin(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("sin")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()

    def selectOp_cos(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("cos")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()

    def selectOp_tan(self):
        firstNumber = self.lineEdit.text()
        self.calculator.setFirstNumber(firstNumber)
        self.calculator.setOperator("tan")

        result = self.calculator.CalculateResult()
        self.lineEdit.setText(str(result))
        self.calculator.reset()

    def selectOp_eps(self):
        self.lineEdit.clear()
        self.lineEdit.setText(str(math.e))
    
    def selectOp_eq(self):
        secondNumber = self.lineEdit.text()
        self.calculator.setSecondNumber(secondNumber)
        
        result = self.calculator.CalculateResult()
        strResult = str(result)
        if strResult[-1] == '0' and strResult[-2] == '.':
            strResult = strResult.replace(".0", "")

        self.lineEdit.setText(strResult)
        self.calculator.reset()
        self.clear = True