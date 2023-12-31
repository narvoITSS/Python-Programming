# Title:    Lab8A1
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user for input on a number of miles and upon clicking a button or pressing "Enter/Return" on the keyboard
#           it converts those miles into kilometers and prints that conversion out to the GUI.

from breezypythongui import EasyFrame

def main():
    Miles_Converter().mainloop()

class Miles_Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 450, height = 200, resizable = False, title = "Miles Converter")
        # Label for instructions
        self.addLabel(row = 0, column = 0, columnspan = 3, text = "Enter the number of miles below ", sticky="NSEW")
        
        # Label for Miles
        self.addLabel(row = 1, column=2, text="Miles", sticky='W')
        #  Float Field for number of miles
        self.miles = self.addFloatField(value = 0, row = 1, column=3, sticky = 'E')
        self.miles.bind("<Return>", lambda event: self.compute())
        
        # Label for Kilometer
        self.addLabel(row=2,column=2,text= "Kilometers", sticky='W')
        # FloatField for number of kilometers from conversion (km = 1.60934 * mi)
        self.kilometers = self.addFloatField(value = 0.00, row = 2, column=3, state = "readonly",sticky="E", precision = 2)
        
        # Compute button. Call compute function on: button click OR enter keypress
        self. outputBtn = self.addButton(row = 3, column = 1, columnspan = 3, text = "Compute", command = self.compute)

    def compute(self):
        kilometers = float(self.miles.getValue()) * 1.60934
        self.kilometers.setValue(kilometers)

    def reset(self):
        self.kilometers.setNumber(0)

if __name__ == "__main__":
    main()
