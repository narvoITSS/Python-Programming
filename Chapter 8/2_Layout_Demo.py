"""
File: Layout_Demo.py
"""
from breezypythongui import EasyFrame
class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""
    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self, width = 300, height = 200, resizable = False)
        self.addLabel(text = "(0, 0)", row = 0, column = 0)
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky="NSEW") # means kind of center that label
        self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky="EW")
        self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky="NSEW")
        self.addLabel(text = "(1, 0 and 1)", row = 2, column = 0,sticky = "NSEW", columnspan = 2)

def main():
    LayoutDemo().mainloop()

if __name__ == "__main__":
    main()
	
