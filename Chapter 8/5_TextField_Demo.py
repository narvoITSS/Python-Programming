from breezypythongui import EasyFrame

class TextFieldDemo(EasyFrame):
	# """ Converts an input string to uppercase and displays the result. """
    def __init__(self):
        """ Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Text Field Demo")

         # Label and field for the input
        self.addLabel(text = "Input", row = 0, column = 0)
        self.inputField = self.addTextField(text = " ", row = 0,	 column = 1) # assign it to inputField so we could retrieve text later with inputField.getText()
        # Label and field for the output
        self.addLabel(text = "Output", row = 1,  column = 0)
        self.outputField = self.addTextField(text = " ", row = 1, column = 1, state = "readonly") # readonly means we can't type anything there

        # The command button
        self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)


	# The event handling method for the button
    def convert(self):
    # """ Inputs the string, converts it to uppercase, and outputs the result."""
        text = self.inputField.getText() # these temporary variables are not part of the object. they are just used to do work.
        result = text.upper()
        self.outputField.setText(result)

def main():
    TextFieldDemo().mainloop()

if __name__ == "__main__":
    main()
