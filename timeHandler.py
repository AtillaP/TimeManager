from tkinter import messagebox

class TimeHandler:
    def __init__(self):
        self.currentTime = None  # Az adattag, amely tárolja az időt

    def set_time(self, time_str):
        """Beállítja az időt a megadott HH:MM formátumban"""
        try:
            # Ellenőrizzük, hogy a formátum HH:MM-e
            hours, minutes = map(int, time_str.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                self.currentTime = time_str
                messagebox.showinfo("Siker", f"Az idő beállítva: {self.currentTime}")
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hiba", "Hibás időformátum. Kérlek, HH:MM formátumban adj meg egy időt.")
