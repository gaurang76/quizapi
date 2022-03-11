import requests
from tkinter import *
from tkinter import messagebox
THEME_COLOR = "#375362"

class difficulty:
    def __init__(self):
        self.window1 = Tk()
        self.window1.geometry("200x200")
        self.window1.title("Quiz Game")
        self.window1.config(padx=20, pady=20, bg=THEME_COLOR)
        options = ["Easy", "Medium", "Hard"]
        self.clicked = StringVar()
        self.clicked.set("Choose your difficulty")
        self.drop = OptionMenu(self.window1, self.clicked, *options,command=self.get_selected)
        self.drop.pack()
        Button(self.window1, text="Start Game",command=self.window1.destroy).pack()

        self.window1.mainloop()

    def get_selected(self,choice):
        self.choice=self.clicked.get()



    def question_data(self):

        try:
            response = requests.get(url=f"https://opentdb.com/api.php?amount=10&difficulty={self.choice.lower()}&type=boolean")
            self.question_data = response.json()['results']
            return self.question_data
        except AttributeError:
            messagebox.showerror(title="No difficulty selected",message="Difficulty level not selected")
