from breezypythongui import EasyFrame

# Question 22
class TestButton(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "", width = 300)
        self.inputField = self.addIntegerField(value = 0,  row = 0, column = 1)
        self.inputField.bind("<Return>", lambda event: self.computeSqrt())
        self.inputField2 = self.addFloatField(value = 0.0, row = 1, column = 1)
        self.addButton(text = "Compute", row = 2, column = 0, command = self.computeSqrt)

    def computeSqrt(self):
        print("debug")

# Question 23
class Calc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Number Field Demo", width = 300)
        self.xField = self.addIntegerField(value = 2,  row = 0, column = 1)
        self.yField = self.addIntegerField(value = 3,  row = 1, column = 1)
        self.zField = self.addIntegerField(value = 0,  row = 2, column = 1, width = 8)
        self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

    def compute(self):
        num1 = self.xField.getNumber()
        num2 = self.yField.getNumber()
        num3 = num1 + num2
        self.zField.setNumber(num3)

# Question 25
class Calc_2(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Demo", width = 300)
        self.addLabel(text = "Num", row = 1, column = 0)
        self.xField = self.addIntegerField(value = 0,  row = 1, column = 1)
        self.addButton(text = "Compute", row = 0, column = 0, columnspan = 2, command = self.compute)

    def compute(self):
        self.xField.setNumber(10)

# Question 27
class Demo(EasyFrame):
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Demo", width = 600)
        self.addLabel(text = "An integer", row = 0, column = 0)
        self.inputField = self.addFloatField(value = 0.0,  row = 0, column = 1)
        self.addLabel(text = "Square root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 3, state = "readonly")
        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)
        self.count = 0

    def computeSqrt(self):
        import math
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)
        self.count += 1

def main():
    #TestButton().mainloop()
    t = Demo()
    t.mainloop()
    print(t.count)
if __name__ == "__main__":
    main()