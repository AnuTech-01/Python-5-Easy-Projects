import tkinter as tk
from tkinter import filedialog,messagebox  # file open/save dialogs aur popup messages ke liye

# New file function (text area clear karta hai)
def new_file():
    text.delete(1.0,tk.END) # pura text delete kar deta hai (start se end tak)


# Open file function (file select karke uska content load karta hai)
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])  # default extension .txt ,  # default extension .txt
    if file_path:
        with open(file_path,'r'):
            text.delete(1.0 , tk.END) # pehle existing text clear
            text.insert(tk.END, file.read()) # file ka content text box me insert

# Save file function (text ko file me save karta hai)
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt" , filetypes=[("Text Files", "*.txt")])
    if file_path: # agar user ne location choose ki
        with open(file_path, 'w') as file:  # write mode me file open
            file.write(text.get(1.0,tk.END))    # text box ka content file me save
            messagebox.showinfo("Info" , "File saves successfully!")    # success popup

# Main window create karna
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Menu bar create karna
menu = tk.Menu(root)
root.config(menu=menu)

# File menu create karna
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",command=new_file) # New option
file_menu.add_command(label="Open",command=open_file) # Open option
file_menu.add_command(label="Save",command=save_file) # Save option
file_menu.add_separator()
file_menu.add_command(label="Edit",command=root.quit)  # program band karne ka option

# Text area create karna (jahan user likhega)
text=tk.Text(root,wrap=tk.WORD, font=("Helvetica",12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)  # text box ko window me expand karna


# Program run karna
root.mainloop()
