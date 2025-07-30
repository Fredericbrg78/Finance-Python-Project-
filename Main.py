import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

# Fonction principale pour afficher le graphique
def show_graph():
    ticker = entry_ticker.get()
    start = entry_start.get()
    end = entry_end.get()

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end)

        if data.empty:
            messagebox.showwarning("Avertissement", "Aucune donnée disponible.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data.index, data['Close'], label='Prix de clôture')

        last_close = data['Close'].iloc[-1]
        last_date = data.index[-1]
        ax.text(last_date, last_close, f'{last_close:.2f}', fontsize=8, color='black')
        ax.axhline(y=last_close, color='black', linestyle='--', linewidth=1)

        ax.set_title(f"Cours de {ticker.upper()} de {start} à {end}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Prix de clôture")
        ax.grid(True)
        ax.legend()

        # Affichage dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

# Interface utilisateur (Tkinter)
window = tk.Tk()
window.title("Visualiseur de Cours Boursier")
window.geometry("600x400")

# Zone de saisie
tk.Label(window, text="Ticker boursier :").pack()
entry_ticker = tk.Entry(window)
entry_ticker.pack()

tk.Label(window, text="Date de début (YYYY-MM-DD) :").pack()
entry_start = tk.Entry(window)
entry_start.pack()

tk.Label(window, text="Date de fin (YYYY-MM-DD) :").pack()
entry_end = tk.Entry(window)
entry_end.pack()

# Bouton
btn = tk.Button(window, text="Afficher le graphique", command=show_graph)
btn.pack(pady=10)

# Lancer l’appli
window.mainloop()
