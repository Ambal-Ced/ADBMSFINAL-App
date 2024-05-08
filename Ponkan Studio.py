from tkinter import *
from tkinter.ttk import Progressbar, Style
import sys
import home
import os
from random import randint
import subprocess
import threading
import matplotlib.pyplot as plt
from matplotlib import *
from data import product_sales, progress_work, product_sales1
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from connect import create_connection
from tkinter import ttk
import psycopg2


root = Tk(className='loading')

image = PhotoImage(file='resources\\stdio.png')

# Set the window size to the screen size to make it full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')

# Remove overrideredirect(1) to allow the window to be movable
root.overrideredirect(1)



# Set the window to always stay on top
root.wm_attributes('-topmost', True)

# Lift the window to the front
root.lift()


bg_label = Label(root, image=image, bg='white')
bg_label.place(x=0, y=0)

progress_label = Label(root, text="Please Wait...", font=('Comic Sans MS', 13, 'bold'), fg='white', bg='#000F84')
progress_label.place(x=600, y=600)

style = Style()
style.configure("TProgressbar", background="blue")

progress = Progressbar(root, orient=HORIZONTAL, length=360, mode='determinate', style="TProgressbar")
progress.place(x=(screen_width - progress.cget('length')) // 2, y=580)  # Center the progress bar

def top():
    root.withdraw()



i = 0
def load():
    global i
    if i <= 9:
        percentint = randint(4, 10)
        txt = 'Please Wait... ' + (str(10 * i + percentint) + '%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10 * i + percentint
        i += 1
    else:
        top()





def mainframe():
    
    root = tk.Tk()
    root.title("Ponkan Studion")
    root.state('zoomed')
    
    def ptr():
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["blue", "#d0efff","#187bcd","#1f1a83",
                "#00b4d8","#3ACBE8","#03254c"]
        )

#chart 1 for product sales pie

        fig1, ax1 = plt.subplots()
        ax1.pie(product_sales.values(), labels=product_sales.keys(),autopct='%1.1f%%')
        ax1.set_xlabel("\nProducts")
        ax1.set_ylabel("")
#plt.show()

#chart 1 bar
        fig2, ax2 = plt.subplots()
        ax2.bar(product_sales1.keys(), product_sales1.values())
        ax2.set_xlabel("\nProducts")
        ax2.set_ylabel("")
#plt.show()

#chart 2

        fig3, ax3 = plt.subplots()
        ax3.pie( progress_work.values(),labels=progress_work.keys(),autopct='%1.1f%%')
        ax3.set_title("Current Progress")
        ax3.set_xlabel("Percentage")
        ax3.set_ylabel("")
#plt.show()


        side_frame = tk.Frame(root, bg="#03254c")
        side_frame.pack(side="left", fill="y")

#create a frame for upper and lower frame
        
        
        lb = tk.Label(main_frame)
        lb.pack()
        
        

#create a upper frame
        upper_frame = tk.Frame(lb)
        upper_frame.pack(fill="both", expand=True)

        canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

#create a lower frame
        lower_frame = tk.Frame(lb)
        lower_frame.pack(fill="both", expand=True)

        canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)
    
    
    def ivy():
        update_frame = tk.Frame(main_frame)
        
        lb = tk.Label(update_frame, text='Second Page', font=('bold',30))
        lb.pack()
        
        update_frame.pack(pady=20)
    
    def bnm():
        setting_frame = tk.Frame(main_frame)
        
        lb = tk.Label(setting_frame, text='Third Page', font=('bold',30))
        lb.pack()
        
        setting_frame.pack(pady=20)
    
    
    def hide_indicators():
        home_indicate.config(bg='blue')
        update_indicate.config(bg='blue')
        setting_indicate.config(bg='blue')
    
    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()
    
    def indicate(lb, page):
        hide_indicators()
        lb.config(bg='white')
        delete_pages()
        page()
    
    options_frame = tk.Frame(root, bg='blue')
    
    home_btn = tk.Button(options_frame,text='Dashboard', font=('Bold',15), bg='Blue',
                        command=lambda: indicate(home_indicate, ptr))
    home_btn.place(x=10, y=50)
    
    home_indicate = tk.Label(options_frame, text='',bg='blue')
    home_indicate.place(x=3, y=50, width=5,height=40)
    
    
    update_btn = tk.Button(options_frame,text='Update Product', font=('Bold',15), bg='Blue',
                            command=lambda: indicate(update_indicate, ivy))
    update_btn.place(x=10, y=100)
    
    update_indicate = tk.Label(options_frame, text='',bg='blue')
    update_indicate.place(x=3, y=100, width=5,height=40)
    
    setting_btn = tk.Button(options_frame,text='Setting', font=('Bold',15), bg='Blue',
                            command=lambda: indicate(setting_indicate, bnm))
    setting_btn.place(x=10, y=150)
    
    setting_indicate = tk.Label(options_frame, text='',bg='blue')
    setting_indicate.place(x=3, y=150, width=5,height=40)
    
    exit_btn = tk.Button(options_frame,text='Exit', font=('Bold',15), bg='Blue', command=root.destroy)
    exit_btn.place(x=10, y=200)
    
    exit_indicate = tk.Label(options_frame, text='',bg='blue')
    exit_indicate.place(x=3, y=200, width=5,height=40)
    
    
    options_frame.pack(side=tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width=210, height=800)
    
    main_frame = tk.Frame(root)
    main_frame.pack(side=tk.LEFT)
    
    
    ptr()



    # Start the loading process
load()
mainframe()
root.mainloop()
