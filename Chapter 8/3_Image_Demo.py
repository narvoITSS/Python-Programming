'''
File: Image_Demo.py
'''
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        imageLabel = self.addLabel(text = " ",row = 0, column = 0,sticky = "N S E W") #now we assign the label to a variable name to edit or reuse later.
        textLabel = self.addLabel(text = "Smokey the cat",row = 1, column = 0, sticky = "N S E W")
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "smokey.gif")
        imageLabel["image"] = self.image # changing/adding an ATTRIBUTE for this label after it has been made.

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"
        textLabel["background"] = "yellow"

def main():
    """Instantiates and pops up the window."""
    ImageDemo().mainloop()
	
if __name__ == "__main__":
    main()
