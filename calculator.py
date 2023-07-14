import math


class Calculator():
    def __init__(self):
        self.firstNumber = None
        self.operator = None
        self.secondNumber = None
        self.result = None

    def setFirstNumber(self, _number):
        self.firstNumber = float(_number)

    def setOperator(self, _operator):
        self.operator = _operator

    def setSecondNumber(self, _number):
        self.secondNumber = float(_number)

    def CalculateResult(self):
        if self.operator == "+":
            self.result = self.firstNumber + self.secondNumber
        elif self.operator == "-":
            self.result = self.firstNumber - self.secondNumber
        elif self.operator == "/":
            self.result = self.firstNumber / self.secondNumber
        elif self.operator == "*":
            self.result = self.firstNumber * self.secondNumber
        elif self.operator == "%":
            self.result = self.firstNumber / 100
        elif self.operator == "x!":
            self.result = math.factorial(int(self.firstNumber))
        elif self.operator == "pow":
            self.result = math.pow(self.firstNumber, self.secondNumber)
        elif self.operator == "√":
            self.result = math.sqrt(self.firstNumber)
        elif self.operator == "In":
            self.result = math.log(self.firstNumber)
        elif self.operator == "log":
            self.result = math.log10(self.firstNumber)
        elif self.operator == "sin":
            numero = math.radians(self.firstNumber)
            self.result = math.sin(numero)
        elif self.operator == "cos":
            numero = math.radians(self.firstNumber)
            self.result = math.cos(numero)
        elif self.operator == "tan":
            numero = math.radians(self.firstNumber)
            self.result = math.tan(numero)
        
        return self.result
    
    def reset(self):
        self.firstNumber = None
        self.operator = None
        self.secondNumber = None
