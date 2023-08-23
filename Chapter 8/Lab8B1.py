# Title:    Lab8B1
# Author:   Nicholas Arvo
# Purpose:  This program will take a fahrenheit value from the user and calculate the corresponding celsius value.

from breezypythongui import EasyFrame

def main():
    Temp_Converter().mainloop()

class Temp_Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 450, height = 250, title = "Temperature Conversion", resizable = False)
        
        # Label for prompt:
        self.addLabel(row = 0, column = 0, columnspan = 3, text = "Please enter a temperature in Fahrenheit to convert to Celsius.")
                
        # Farhenheit: Label and associated input field
        self.addLabel(row = 1, column = 0, text = "Fahrenheit")
        self.inputField = self.addFloatField(row = 1, column = 2, value = 0.0)
        # On "Enter" keyboard press -> temperatureConversion()
        self.inputField.bind("<Return>", lambda event: self.temperatureConversion())

        # Compute Button
        self.addButton(row = 2, column = 1, text = "Compute", command = self.temperatureConversion)

        # Celsius: Label and associated output field for conversion
        self.addLabel(row = 3, column = 0, text = "Celsius")
        self.outputField = self.addFloatField(row = 3, column = 2, value = 0.0, state = "readonly")
    
    def temperatureConversion(self):
        # Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
        fTemp = float(self.inputField.getValue())
        cTemp = (fTemp - 32.0) * (5/9)
        self.outputField.setValue(cTemp)
        
if __name__ == "__main__": 
    main()