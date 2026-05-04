import tkinter as tk  # tkinter library import ki GUI banane ke liye
from time import strftime # time format karne ke liye function import

root = tk.Tk()  # main window create karta hai
root.title("Digital Clock") # window ka title set karta hai

def time():   # ek function jo har second time update karega
    string = strftime('%H:%M:%S %p \n %D')  # current time ko string me convert karta hai
    label.config(text=string)  # label par time display karta hai
    label.after(1000,time)  # 1000 ms (1 sec) baad function ko fir call karta hai


label = tk.Label(root, font=('calibri',30, 'bold'), background="pink",foreground="White")    # ek label (text box) create karte hain
label.pack(anchor="center")  # label ko center me place karta hai

time()

root.mainloop()  # GUI ko run karta hai (window open rakhta hai)
