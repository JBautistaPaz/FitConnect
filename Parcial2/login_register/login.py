import tkinter as tk
import sqlite3
from tkinter import messagebox
import subprocess

conn = sqlite3.connect("fitconnect.db")
cursor = conn.cursor()

def iniciar_sesion():
    usuario = ingresar_usuario.get()
    contrasenia = ingresar_contrasenia.get()

    if not usuario or not contrasenia:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    cursor.execute("SELECT * FROM fitconnect WHERE usuario=?", (usuario,))
    registro = cursor.fetchone()

    if registro is None:
        messagebox.showwarning("Usuario no encontrado", "El usuario no está registrado. Redirigiendo a la página de registro...")
        subprocess.Popen(["python", "login_register/register.py"])
        login.destroy()
    else:
        if registro[2] == contrasenia: 
            subprocess.Popen(["python", "./main.py"])
            login.destroy()
        else:
            messagebox.showerror("Error", "La contraseña es incorrecta. Por favor, inténtelo de nuevo.")

login = tk.Tk()
login.geometry("700x600")
login.title("LogIn")
login.configure(bg="#F3F4F6")

tk.Label(login, text="Usuario:", width=18, font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748").grid(row=0, column=0, padx=10, pady=10)
tk.Label(login, text="Contraseña:", width=18, font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748").grid(row=1, column=0, padx=10, pady=10)

ingresar_usuario = tk.Entry(login, font=("Helvetica", 12))
ingresar_contrasenia = tk.Entry(login, show="*", font=("Helvetica", 12))
ingresar_usuario.grid(row=0, column=1, padx=10, pady=10)
ingresar_contrasenia.grid(row=1, column=1, padx=10, pady=10)

boton_subir = tk.Button(login, text="Enviar", command= iniciar_sesion, font=("Helvetica", 12, "bold"), bg="#4FD1C5",fg="#FFFFFF", activebackground="#38B2AC",  activeforeground="#FFFFFF", relief="flat", padx=10, pady=5)
boton_subir.grid(row=4, column=1, columnspan=2, pady=10)

login.mainloop()

conn.close()