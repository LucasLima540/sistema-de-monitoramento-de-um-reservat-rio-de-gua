import tkinter as tk
from tkinter import ttk
import random
import time
from threading import Thread

# Cores por nível
cores = {
    1: "red",
    2: "yellow",
    3: "green",
    4: "cyan",
    5: "blue"
}

mensagens = {
    1: "Muito baixo (crítico)",
    2: "Baixo",
    3: "Médio",
    4: "Alto",
    5: "Muito alto (alerta)"
}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Reservatório")

        self.label = tk.Label(root, text="Nível: -", font=("Arial", 20))
        self.label.pack(pady=20)

        self.status = tk.Label(root, text="", font=("Arial", 16))
        self.status.pack(pady=10)

        self.running = False

        self.btn_start = ttk.Button(root, text="Iniciar Simulação", command=self.start)
        self.btn_start.pack(pady=5)

        self.btn_stop = ttk.Button(root, text="Parar", command=self.stop)
        self.btn_stop.pack(pady=5)

    def update_ui(self, nivel):
        self.label.config(text=f"Nível: {nivel}")
        self.status.config(
            text=mensagens[nivel],
            fg=cores[nivel]
        )

    def simulate(self):
        while self.running:
            nivel = random.randint(1, 5)
            self.update_ui(nivel)
            time.sleep(2)

    def start(self):
        if not self.running:
            self.running = True
            Thread(target=self.simulate, daemon=True).start()

    def stop(self):
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
