import tkinter as tk
import subprocess
from tkinter import *

bienvenidos=tk.Tk()
bienvenidos.title("Bienvenidos")
bienvenidos.geometry("700x600")
bienvenidos.configure(bg="#F3F4F6")

label_total=tk.Label(bienvenidos, text="¡Bienvenidos a FitConnect!",  font=("Helvetica", 18, "bold"),bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

def abrir_register():
    subprocess.Popen(["python", "login_register/register.py"])
    bienvenidos.destroy()

boton_abrir_login = tk.Button(bienvenidos, text="Registrarse", font=("Arial", 14, "bold"), bg="#4FD1C5", fg="#FFFFFF",activebackground= "#38B2AC", activeforeground="#FFFFFF", relief="flat", command=abrir_register)
boton_abrir_login.pack(pady=10)

def abrir_login():
    subprocess.Popen(["python", "login_register/login.py"])
    bienvenidos.destroy()

boton_abrir_register=tk.Button(bienvenidos,text="Loguearse",font=("Arial", 14, "bold"),  bg="#63B3ED",fg="#FFFFFF",
activebackground="#4299E1", activeforeground="#FFFFFF", relief="flat", command= abrir_login)
boton_abrir_register.pack()

bienvenidos.mainloop()