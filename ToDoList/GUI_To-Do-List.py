import tkinter as tk
from tkinter import messagebox, simpledialog
class ToDoList:
    def __init__(app, window):

        #Window
        app.window = window
        app.window.title("To Do List")
        window.geometry("500x500")
        app.task_list = []

        #Main_Frame
        app.main_frame = tk.frame(window, bg='LightSkyBlue')
        app.main_frame.pack(padx=10, pady=10)

        #Heading
        app.heading_label = tk.Label(app.main_frame, text="To Do List",font=('BankGothic Lt BT', 20, 'bold'), bg='LightSkyBlue',fg='DarkBlue')
        app.heading_label.grid(row=0, column=0, padx=10, pady=10)

        #Entry
        app.input_entry = tk.Entry(app.main_frame, width=40, font=('BankGothic Lt BT', 16))
        app.input_entry.grid(row=1, column=0, padx=5, pady=5)

        #Buttons
        app.add_


window = tk.Tk()
app = ToDoList(window)

window.mainloop()