# Title:    Lab8B1
# Author:   Nicholas Arvo
# Purpose:  This program will take two string inputs form the user and report if a word exists in a sentence input

# some sort of user input(s) -> use that to calculate an output value.

from breezypythongui import EasyFrame

def main():
    String_Compare().mainloop()

class String_Compare(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, width = 535, height = 250, title = "String Comparison", resizable = False)
        
        # Label for prompt:
        self.addLabel(row = 0, column = 0, columnspan = 2, text = "Please enter a string of words and a word below.", sticky = "NW")
        self.addLabel(row = 3, column = 0, columnspan = 2, text =  "Press \"Search\" button or press \"Enter\" on your keyboard to determine\nif your word exists in the sentence.", sticky = "NW")
                
        # Label and TextField for Strings
        self.addLabel(row = 1, column=0, text = "Enter your sentence to search:")
        self.inputString1 = self.addTextField(row = 1, column = 1, text = "")
        self.inputString1.bind("<Return>", lambda even: self.compareString())
        
        self.addLabel(row = 2, column=0, text = "Enter your word to search for:")
        self.inputString2 = self.addTextField(row = 2, column = 1, text = "")
        self.inputString2.bind("<Return>", lambda even: self.compareString())

        # Button to run comparision
        self.cmpBtn = self.addButton(row = 4, column = 0, columnspan = 2, text="Search", command= self.compareString)

        # Label and TextField for Output
        self.addLabel(row=5, column=0, text= "Is your word contained in the sentence? ")
        self.outputField = self.addTextField(row=5, column=1, text = "", state = "readonly")        
    
    def compareString(self):
        inputSentence = self.inputString1.getText()
        inputWord = self.inputString2.getText()
        comparisonFlag = False
        
        for words in inputSentence.split():
            if inputWord == words:
                comparisonFlag = True
            else:
                pass

        # If two strings are the same but there exists a " " in both strings
        # such as: 'test 123' == 'test 123'
        if inputSentence == inputWord:
            comparisonFlag = True

        # Output   
        if comparisonFlag:
            self.outputField.setText("Yes")
        else:
            self.outputField.setText("No")
            
if __name__ == "__main__": 
    main()
