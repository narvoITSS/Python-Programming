"""
File: GUI_labeldemo.py
"""
from breezypythongui import EasyFrame
class LabelDemo(EasyFrame): # extends EasyFrame
	"""Displays a greeting in a window."""
	def __init__(self): # the constructor, a must have, calls the constructor for EasyFrame()
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title="Label Demo",height= 200, width= 300, resizable= False, background="yellow")
		self.setResizable(False) 
		self.addLabel(text = "Hello world! ", row = 0, column = 0)
def main():
	"""Instantiates and pops up the window."""
	LabelDemo().mainloop()
if __name__ == "__main__":
    main()