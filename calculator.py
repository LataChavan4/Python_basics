class Calculator:
    def __init__(self,num):
        self.num = num

    def squareofNumber(self):
        print(f"Square of the number is: {self.num **2}")
    
    def qubeofNumber(self):
        print(f"qube of the number is: {self.num**3}")
    
    def squarerootofNumber(self):
        print(f"Suuareroot of the number is: {self.num**0.5}")

number = Calculator(9)
number.squareofNumber()
number.qubeofNumber()
number.squarerootofNumber()

    