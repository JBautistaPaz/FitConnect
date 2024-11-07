import tkinter as tk
import subprocess

desafios=tk.Tk()
desafios.title("Desafios")
desafios.geometry("700x600")
desafios.config(bg="#F3F4F6")

label_total=tk.Label(desafios, text="Los mejores desafios dependiendo tu nivel", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

texto = tk.Label(desafios, text="Aca podés decidir en que nivel de desafíos queres participar.", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748", padx=10, pady=10)
texto.pack(pady=20)

def irPrincipiante():
    subprocess.Popen(["python", "desafios/desafioP.py"])
    desafios.destroy()

boton_principiante = tk.Button(desafios,text="Principiantes",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=irPrincipiante
)
boton_principiante.pack(pady=10)

def irIntermedio():
    subprocess.Popen(["python", "desafios/desafioI.py"])
    desafios.destroy()

boton_intermedio = tk.Button(desafios, text="Intermedio", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=irIntermedio)
boton_intermedio.pack(pady=10)

def irExperto():
    subprocess.Popen(["python", "desafios/desafioE.py"])
    desafios.destroy()

boton_experto = tk.Button(desafios, text="Experto", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=irExperto)
boton_experto.pack(pady=10)

def irAtras():
    subprocess.Popen(["python", "Main.py"])
    desafios.destroy()

boton_atras=tk.Button(desafios, text="Atras",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= irAtras)
boton_atras.pack(pady=20)

desafios.mainloop()