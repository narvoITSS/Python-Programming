class Exam(object):
        BASE = 50.0
        def __init__(self,num,gr):
                self.nbrQuestions = num
                self.grade = gr
                temp = self.grade / self.nbrQuestions
                self.averagePoints = temp

        def getGrade(self):
                return self.grade

        def getNbrQuestions(self):
                return self.nbrQuestions

        def getAveragePts(self):
                return self.averagePoints

        def setGrade(self, gr):
                self.grade = gr
                self.averagePoints = self.grade / self.nbrQuestions

def main():
        b1 = Exam(20, 92)
        e1 = Exam(25, 79)
        e1.setGrade(100)
        print(e1.getAveragePts())
  
if __name__ == "__main__":
    main()