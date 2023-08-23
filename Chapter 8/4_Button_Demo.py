"""
File: Button_Demo.py
"""

from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)

        # A single label in the first row.
        self.title_label = self.addLabel(text = "Hello world!",row = 0, column = 0, columnspan = 2,sticky = "NSEW")
        # Two command buttons in the second row.
        self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0)
        self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, state = "disabled")
        
def main():
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()