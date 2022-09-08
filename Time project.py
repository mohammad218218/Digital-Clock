import tkinter as tk
from time import strftime

bg_color = "white"
fg_color = "darkviolet"

window = tk.Tk()
window.geometry("390x80")
window.configure(background=bg_color)
window.title("Digital Clock")

lbl = tk.Label(window,
               font=("digital-7", 50, "bold"),
               background=bg_color,
               foreground=fg_color)

def show_time():
    text = strftime(" %H:%M:%S %p ")
    lbl.config(text=text)
    lbl.after(1000, show_time)


lbl.pack(anchor="center")

show_time()
tk.mainloop()


