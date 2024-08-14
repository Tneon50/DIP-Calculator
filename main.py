import tkinter as tk

class MyCalculator:
    def __init__(self):
       
       self.root = tk.Tk()

       self.root.geometry("300x300")
       self.root.title("My calculator")

       self.label= tk.Label(self.root, text="Hello DIP02", font=('Arial',18))
       self.label.pack()

       self.num1= tk.Button(self.root, text="1", height=3, width=6)
       self.num1.place(x=20, y=50)

       self.button= tk.Button(self.root, text="=", height=3, width=6, command=self.ansFn)
       self.button.place(x=225, y=225)

       self.root.mainloop()

    def ansFn(self):
        self.label()

MyCalculator()      
