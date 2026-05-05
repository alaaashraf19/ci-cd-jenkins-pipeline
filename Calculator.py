class Calculator:

    def __init__(self):
        pass
    ## Add Function
    def add(self, x, y):
        return x + y
    ## Divide Function
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return x - y


