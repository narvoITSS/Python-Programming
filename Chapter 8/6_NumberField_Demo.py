import math
from breezypythongui import EasyFrame


class NumberFieldDemo(EasyFrame):
    """ Computes and displays the square root of an input number."""

    def __init__(self):
        # """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Number Field Demo")
        # Label and field for the input
        self.addLabel(text = "An integer", row = 0, column = 0)
        self.inputField = self.addIntegerField(value = 0,  row = 0, column = 1, width = 10) # needs a starting value
        # Label and field for the output
        self.addLabel(text = "Square root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 10, precision = 2, state = "readonly")
        # The command button
        self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)

    # The event handling method for the button
    def computeSqrt(self):
        """Inputs the integer, computes the square root, and outputs the result."""
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)
	
def main():
    NumberFieldDemo().mainloop()

if __name__ == "__main__":
    main()