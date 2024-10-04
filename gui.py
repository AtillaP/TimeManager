import tkinter as tk

class TimeAppGUI:
    _instance = None  # Singleton osztály egyetlen példánya

    def __new__(cls, root, handler):
        if cls._instance is None:
            cls._instance = super(TimeAppGUI, cls).__new__(cls)
            return cls._instance
        else:
            messagebox.showwarning("Figyelmeztetés", "Az alkalmazás már meg van nyitva.")
            return None  # Nem hozunk létre új példányt

    def __init__(self, root, handler):
        if hasattr(self, 'initialized') and self.initialized:
            return
        self.root = root
        self.handler = handler
        self.create_widgets()
        self.initialized = True

    def create_widgets(self):
        """A GUI elemeinek létrehozása"""
        self.root.title("Időpont beállító")

        # Input mező címke
        label = tk.Label(self.root, text="Add meg az időt HH:MM formátumban:")
        label.pack(pady=10)

        # Input mező létrehozása
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=10)

        # Gomb létrehozása
        submit_button = tk.Button(self.root, text="Beállít", command=self.submit_time)
        submit_button.pack(pady=10)

    def submit_time(self):
        """Az idő továbbítása a handler-nek"""
        time_str = self.time_entry.get()
        self.handler.set_time(time_str)
