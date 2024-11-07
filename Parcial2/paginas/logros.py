import tkinter as tk
import subprocess
from tkinter import *
import random

logros=tk.Tk()
logros.title("Logros")
logros.geometry("700x600")
logros.config(bg="#F3F4F6")

label_total=tk.Label(logros, text="Estos son tu logros!", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

numero_aleatorio = random.randint(1, 40)

texto = tk.Label(logros, text=f"Has podido bajar {numero_aleatorio} kilos en total", font=("Helvetica", 14), bg="#F3F4F6", fg="#2D3748", padx=20, pady=20)
texto.pack(pady=30)

def irAtras():
    subprocess.Popen(["python", "./main.py"])
    logros.destroy()

boton_atras=tk.Button(logros, text="Atras",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= irAtras)
boton_atras.pack(pady=20)

def destroy():
    logros.destroy()

boton_cerrar=tk.Button(logros, text="Cerrar Página",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= destroy)
boton_cerrar.pack(pady=20)


logros.mainloop()

