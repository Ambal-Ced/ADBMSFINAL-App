from tkinter import *

class HomePage:
    def __init__(self, System_window):
        self.System_window = System_window
        
        #window size and placement
        System_window.rowconfigure(0, weight= 1)
        System_window.columnconfigure(0, weight=1)
        height = 650
        width = 750
        x = (System_window.winfo_screenwidth()//2)-(width//2)
        y = (System_window.winfo_screenheight()//4)-(height//4)
        System_window.geometry('{}x{}+{}+{}'.format(width,height,x,y))

def page():
    window = Tk()
    HomePage(window)
    window.mainloop()
    
    
if __name__ == '__main__':
    page()