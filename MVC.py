import tkinter as tk
from tkinter import ttk

# ====================================================================
# 1. MODEL (Logika Danych)
# ====================================================================

class KwadratModel:
    """Model Danych: Przechowuje dane do obliczenia kwadratu."""
    def __init__(self):
        self._wynik = 0

    def oblicz(self, liczba):
        """Oblicza kwadrat liczby."""
        self._wynik = liczba ** 2

    def get_wynik(self):
        return self._wynik


# ====================================================================
# 2. VIEW (Interfejs Graficzny)
# ====================================================================

class KalkulatorView(tk.Tk):
    """Widok: Tworzy i wyświetla interfejs Tkinter."""
    def __init__(self, controller):
        super().__init__()
        self.title("Kalkulator kwadratów w Pythonie")
        self.geometry("300x200")

        self.controller = controller

        self.wynik_var = tk.StringVar(value="Wynik: 0")

        self._utworz_widzety()
        
    def _utworz_widzety(self):
        self.liczba_entry = ttk.Entry(self, font=("Arial", 16))
        self.liczba_entry.pack(pady=10)

        self.oblicz_button = ttk.Button(self, text="Oblicz")
        self.oblicz_button.config(command=self.controller.obsluz_oblicz)
        self.oblicz_button.pack(pady=10)

        self.wynik_label = ttk.Label(self, textvariable=self.wynik_var, font=("Arial", 16))
        self.wynik_label.pack(pady=10)

    def ustaw_wynik(self, nowy_wynik):
        self.wynik_var.set(f"Wynik: {nowy_wynik}")


# ====================================================================
# 3. CONTROLLER (Pośrednik)
# ====================================================================

class KalkulatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view 

    def aktualizuj_view(self):
        wynik = self.model.get_wynik()
        self.view.ustaw_wynik(wynik)

    def obsluz_oblicz(self):
        try:
            liczba = int(self.view.liczba_entry.get())
            self.model.oblicz(liczba)  
            self.aktualizuj_view()
        except ValueError:
            self.view.ustaw_wynik("Błąd: Wprowadź liczbę całkowitą!")


# ====================================================================
# 4. PUNKT STARTOWY
# ====================================================================

if __name__ == "__main__":
    model = KwadratModel()

    controller_instance = KalkulatorController(model, view=None) 
    
    view_instance = KalkulatorView(controller_instance)
    
    controller_instance.view = view_instance 

    view_instance.mainloop()
