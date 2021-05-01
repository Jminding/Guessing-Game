from tkinter import *
# For some reason, importing tkinter doesn't import messagebox in Python 3.6+
from tkinter import messagebox
from tkinter import simpledialog

guessList = []
class GuessNumber(Frame):
    '''represents a board of guess your number'''
    def __init__(self,master,lowerRange,upperRange):
        '''GuessNumber(lowerRange,upperRange)
        creates a guessing number button board'''
        Frame.__init__(self,master)
        self.grid()
        self.lowerRange = lowerRange
        self.upperRange = upperRange
        self.computerGuess = (self.lowerRange + self.upperRange)//2
        self.endgame = None
        Label(self,text="My Guess").grid(row=0,column=0)
        Label(self,text=self.computerGuess).grid(row=2,column=0)
        Label(self,text="Result").grid(row=0,column=1)
        self.tooHighButton = Button(self,text="Too High",command=self.too_high).grid(row=1,column=1)
        self.tooLowButton = Button(self,text="Too Low",command=self.too_low).grid(row=3,column=1)
        self.correctButton = Button(self,text="Correct!",command=self.correct).grid(row=2,column=1)

    def too_high(self):
        '''if answer is too high'''
        guessList.append(self.computerGuess)
        self.upperRange = self.computerGuess
        return GuessNumber(root,self.lowerRange,self.computerGuess)

    def too_low(self):
        '''if answer is too low'''
        guessList.append(self.computerGuess)
        self.lowerRange = self.computerGuess
        return GuessNumber(root,self.computerGuess,self.upperRange)

    def correct(self):
        '''if the answer is correct'''
        guessList.append(self.computerGuess)
        if messagebox.showinfo('Thinking of your number',"Yay -- I got it!  It took me " + str(len(guessList)) + " tries.  Here's my full list of guesses: " + str(guessList) + ". YAY",parent=self):
            self.destroy()
            self.quit()


root = Tk()
def play():
    lowerRange = int(simpledialog.askstring(title="Lower Bound", prompt="Lower Bound:"))
    upperRange = int(simpledialog.askstring(title="Upper Bound", prompt="Upper Bound:"))
    root.title('Guess')
    guess = GuessNumber(root,lowerRange,upperRange)
    guess.mainloop()

play()
