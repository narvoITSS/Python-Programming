# Title:    Lab8B2
# Author:   Nicholas Arvo
# Purpose:  This program will take a total number of seconds from the user and convert it corresponding integers for the
#           the number of days, hours, minutes, and remaining seconds in that input.

from breezypythongui import EasyFrame

def main():
    Time_Converter().mainloop()
    
class Time_Converter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Time converter", width=450, height=300, resizable=False)

        # Row 0: Label Prompt
        self.addLabel(row = 0, column = 0, text = "Please enter a number of seconds to convert: ")

        # Row 1: Input Label Input Int field
        self.addLabel(row = 1, column = 0, text = "Total seconds: ")
        self.inputField = self.addIntegerField(row = 1, column = 1, value = 0)
        self.inputField.bind("<Return>", lambda event: self.conversion())
        
        # Row 2: Compute Button
        self.addButton(row = 2, column = 0,columnspan = 2, text = "Compute", command = self.conversion)

        # Row 3: Day Label, Day Int Field
        self.addLabel(row = 3, column = 0, text = "Days: ")
        self.outputDays =self.addIntegerField(row = 3, column = 1, value = 0, state = "readonly")

        # Row 4:  Hours Label, Hours Int Field
        self.addLabel(row = 4, column = 0, text = "Hours: ")
        self.outputHours =self.addIntegerField(row = 4, column = 1, value = 0, state = "readonly")

        # Row 5: Minutes Label, Minutes Int Field
        self.addLabel(row = 5, column = 0, text = "Minutes: ")
        self.outputMinutes = self.addIntegerField(row = 5, column = 1, value = 0, state = "readonly")
    
        # Row 6: Seconds Label, Seconds Int Field
        self.addLabel(row = 6, column = 0, text = "Seconds: ")
        self.outputSeconds = self.addIntegerField(row = 6, column = 1, value = 0, state = "readonly") 

        self.test = self.addFloatField(value = 0, row = 1, column = 0)

        
    def conversion(self):
        time = 0
        try:
            time = int(self.inputField.getValue())
            if time < 0: raise ValueError
        except ValueError:
            self.messageBox(title = "Error!", message = "Invalid entry detected!")

        time_dict = {86400:0, 3600:0, 60:0, 1:0}

        for keys in time_dict:
            time_dict[keys] = time // keys
            time %= keys

        self.outputDays.setValue(time_dict[86400])
        self.outputHours.setValue(time_dict[3600])
        self.outputMinutes.setValue(time_dict[60])
        self.outputSeconds.setValue(time_dict[1])
        self.test.

if __name__ == "__main__":
    main()

