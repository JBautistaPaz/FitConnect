import tkinter as tk
import sqlite3
from tkinter import messagebox
import subprocess

conn = sqlite3.connect("fitconnect.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fitconnect (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    contrasenia TEXT NOT NULL
)
""")

conn.commit()

def guardar_usuario():
    usuario = ingresar_usuario.get()
    contrasenia = ingresar_contrasenia.get()
    contrasenia_repetida = ingresar_contrasenia_2.get()
   
    if not usuario or not contrasenia:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    if contrasenia != contrasenia_repetida:
        messagebox.showwarning("Error", "Las contraseñas no coinciden. Por favor, intente de nuevo.")
        ingresar_contrasenia.delete(0, tk.END)
        ingresar_contrasenia_2.delete(0, tk.END)
        return

    cursor.execute("SELECT * FROM fitconnect WHERE usuario=?", (usuario,))
    if cursor.fetchone():
        messagebox.showwarning("Advertencia", "El nombre de usuario ya existe. Por favor, elige otro.")
        ingresar_usuario.delete(0, tk.END)
        return
    try:
        cursor.execute("INSERT INTO fitconnect (usuario, contrasenia) VALUES (?, ?)", (usuario, contrasenia))
        conn.commit()
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
        subprocess.Popen(["python", "login_register/login.py"])
        register.destroy()  # Cerrar la ventana de registro
        
    except sqlite3.IntegrityError:
        messagebox.showwarning("Error", "Hubo un problema al registrar el usuario")


register = tk.Tk()
register.geometry("700x600")
register.title("Formulario de Registro")
register.configure(bg="#F3F4F6")


tk.Label(register, text="Usuario:", width=18, font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748").grid(row=0, column=0, padx=10, pady=10)
tk.Label(register, text="Contraseña:", width=18, font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748").grid(row=1, column=0, padx=10, pady=10)
tk.Label(register, text="Repetir contraseña:", width=18, font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748").grid(row=2, column=0, padx=10, pady=10)


ingresar_usuario = tk.Entry(register, font=("Helvetica", 12))
ingresar_contrasenia = tk.Entry(register, show="*", font=("Helvetica", 12))
ingresar_contrasenia_2 = tk.Entry(register, show="*", font=("Helvetica", 12))

ingresar_usuario.grid(row=0, column=1, padx=10, pady=10)
ingresar_contrasenia.grid(row=1, column=1, padx=10, pady=10)
ingresar_contrasenia_2.grid(row=2, column=1, padx=10, pady=10)


boton_subir = tk.Button(register, text="Enviar",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", command=guardar_usuario, activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat")
boton_subir.grid(row=5, column=1,padx=10 ,pady=10)

# def abrir_registros():
#     subprocess.Popen(["python", "registros.py"])
#     register.destroy()

# boton_registros = tk.Button(register, text="Ver Registros",font=("Helvetica", 12, "bold"), bg="#63B3ED", fg="#FFFFFF",  activebackground="#4299E1", activeforeground="#FFFFFF", relief="flat", command=abrir_registros)
# boton_registros.grid(row=7, column=1, padx=10, pady=10)

register.mainloop()

conn.close()
