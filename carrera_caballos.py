import tkinter as tk
from tkinter import ttk
import threading
import random
import time

class CarreraCaballos:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrera de Caballos")
        self.root.geometry("500x300")
        style = ttk.Style(self.root)
        style.theme_use('default')
        style.configure("Red.Horizontal.TProgressbar", foreground='red', background='red')
        
        
        self.caballos = [
            {"nombre": "Galán del Rancho", "progreso": 0},
            {"nombre": "Pegaso", "progreso": 0},
            {"nombre": "Rocinante", "progreso": 0},
            {"nombre": "Tornado", "progreso": 0},
        ]
        
        self.barras = []
        self.etiquetas = []

        for i, caballo in enumerate(self.caballos):
            label = tk.Label(root, text=f"{caballo['nombre']}: 0%")
            label.pack()
            self.etiquetas.append(label)
            
            barra = ttk.Progressbar(
                root, orient="horizontal", length=400, mode="determinate", 
                        maximum=100, style="Red.Horizontal.TProgressbar"
                        )
            barra.pack(pady=5)
            self.barras.append(barra)

        self.boton_iniciar = tk.Button(root, text="Iniciar carrera", command=self.iniciar_carrera)
        self.boton_iniciar.pack(pady=10)

        self.ganador_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.ganador_label.pack()

    def iniciar_carrera(self):
        self.ganador_label.config(text="")
        self.boton_iniciar.config(state="disabled")

        # Reiniciar barras y progreso
        for i in range(4):
            self.caballos[i]["progreso"] = 0
            self.barras[i]["value"] = 0
            self.etiquetas[i].config(text=f"{self.caballos[i]['nombre']}: 0%")
        
        self.terminada = False

        for i in range(4):
            hilo = threading.Thread(target=self.correr, args=(i,))
            hilo.start()

    def correr(self, indice):
        while self.caballos[indice]["progreso"] < 100 and not self.terminada:
            avance = random.randint(1, 15)
            self.caballos[indice]["progreso"] += avance
            if self.caballos[indice]["progreso"] > 100:
                self.caballos[indice]["progreso"] = 100

            self.barras[indice]["value"] = self.caballos[indice]["progreso"]
            self.etiquetas[indice].config(text=f"{self.caballos[indice]['nombre']}: {self.caballos[indice]['progreso']}%")
            time.sleep(0.2)

        if not self.terminada:
            self.terminada = True
            self.ganador_label.config(text=f"🏁 ¡Ganó {self.caballos[indice]['nombre']}!")
            self.boton_iniciar.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarreraCaballos(root)
    root.mainloop()
