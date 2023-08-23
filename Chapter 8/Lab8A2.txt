# Title:    Lab8A2
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user an amount of cents to enter and converts that into
#           the smallest number of associated coins to create that value.

from breezypythongui import EasyFrame

def main():
    Money_Converter().mainloop()

class Money_Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width=425, height=350, title="Money Converter", resizable=False)

        # Instruction prompt
        self.addLabel(row = 0, column=0, columnspan=3, text="Enter a currency amount in cents and press the button. ", sticky="N")

        # Row 1 : Amount Label and Input Text Box
        self.addLabel(row = 1, column=0, text="Amount", sticky="W")
        self.inputValue = self.addIntegerField(row = 1, column = 2, columnspan = 2, value=0, sticky="E")
        self.inputValue.bind("<Return>", lambda event: self.change_conversion())

        # Row 2 : Convert button
        self.addButton(row=2, column=1, text="Convert", command = self.change_conversion)

        # Row 3: Quarter Label and Output Text Box
        self.addLabel(row=3,column=0,text="Quarters")
        self.quarter_count = self.addIntegerField(row=3, column=2, value=0, state="readonly")
        
        # Row 4: Dimes Label and Output Text Box
        self.addLabel(row=4,column=0,text="Dimes")
        self.dime_count = self.addIntegerField(row=4, column=2,value=0, state="readonly")   
        
        # Row 5: Nickels Label and Output Text Box
        self.addLabel(row=5,column=0,text="Nickels")
        self.nickel_count = self.addIntegerField(row=5, column=2,value=0, state="readonly")

        # Row 6: Pennies Label and Output Text Box
        self.addLabel(row=6,column=0,text="Pennies")
        self.penny_count = self.addIntegerField(row=6, column=2,value=0, state="readonly")
    
    def change_conversion(self):
        change_dictionary = {25:0, 10:0, 5:0, 1:0}
        amount = int(self.inputValue.getValue()) 

        # for each value in change types:
        for keys in change_dictionary.keys():
            # coin count = Amount // change_type[i]. 
            change_dictionary[keys] = amount // keys
            # Amount = Amount % change_type[i]
            amount %= keys

        self.quarter_count.setValue(change_dictionary[25])
        self.dime_count.setValue(change_dictionary[10])
        self.nickel_count.setValue(change_dictionary[5])
        self.penny_count.setValue(change_dictionary[1])
        
if __name__ == "__main__":
    main()
