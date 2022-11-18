class Programmers:
    company = "Microsoft"

    @staticmethod
    def greet():
        print("Welcome to Microsoft")

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getData(self):
        print(f"The name of the new employee is {self.name} and the product is {self.product}")

sagar = Programmers("sagar", "GitHub")


sagar.greet()
sagar.getData()


