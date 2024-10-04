import tkinter as tk
from tkinter import messagebox
import gui
import timeHandler as tH

def Main():
    # Ellenőrizzük, hogy van-e már nyitott Tkinter ablak
    if tk._default_root is not None:
        messagebox.showwarning("Figyelmeztetés", "Már van egy nyitott ablak.")
        return

    root = tk.Tk()

    # Létrehozzuk a TimeHandler objektumot
    handler = tH.TimeHandler()

    # Létrehozzuk a GUI-t és átadjuk a TimeHandler-t
    app = gui.TimeAppGUI(root, handler)

    if app:  # Csak akkor induljon el a fő hurok, ha sikerült létrehozni a GUI-t
        root.mainloop()

if __name__ == '__main__':
	Main()