# Title:    Lab8A3
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user for the number of miles and total hours used for a rental car and outputs 
#           the total cost of this rental to the user based on a service pricing formula.

from breezypythongui import EasyFrame

def main():
    Miles_Converter().mainloop()

class Miles_Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=410, height=300, title= "Miles Converter", resizable=False)

        self.addLabel(row = 0, column = 0, columnspan = 3, text = "Enter the number of miles below.", sticky = "W")

        self.addLabel(row = 1, column = 0, text = "Hours:", sticky = "W")
        self.hours = self.addFloatField(row = 1, column = 2, value = 0.0, sticky = "E")

        self.addLabel(row = 2, column = 0, text = "Miles:", sticky = "W")
        self.miles = self.addFloatField(row = 2, column = 2, value = 0.0, sticky = "E")

        self.addButton(row = 3, column = 0, columnspan = 3, text = "Compute", command = self.compute)

        self.addLabel(row = 4, column = 0, text = "Rental Cost ($):", sticky = "W")
        self.rentalCost = self.addFloatField(row = 4, column = 2, value = 0.0, precision = 0.2, sticky = 'E', state = "readonly")

    def compute(self):
        totalCost = 200 + (150 * float(self.hours.getValue())) + (2 * float(self.miles.getValue()))
        self.rentalCost.setValue(totalCost)

if __name__ == "__main__":
    main()

        

