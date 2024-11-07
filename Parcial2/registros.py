# import tkinter as tk
# import subprocess
# from tkinter import *
# import sqlite3
# from tkinter import messagebox


# #Crear la ventana principal
# registros=tk.Tk()
# registros.title("Registros de Usuarios")
# registros.geometry("600x400")
# registros.configure(bg="#F3F4F6")

# #etitueta principal
# label_total=tk.Label(registros, text="Registros de Usuarios", font=("Helvetica", 14, "bold"),  bg="#F3F4F6", fg="#2D3748")
# label_total.pack(pady=10)

# conn = sqlite3.connect('fitconnect.db')
# c = conn.cursor()

# #Funciones para manejar la base de datos

# def mostrar_registros():
#     lista_registros.delete(0, tk.END)
#     c.execute("SELECT * FROM fitconnect")
#     for fila in c.fetchall():
#         lista_registros.insert(tk.END, fila)

# def eliminar_registro():
#     try:
#         seleccion = lista_registros.curselection()[0]
#         id_registro = lista_registros.get(seleccion)[0]
#         c.execute("DELETE FROM fitconnect WHERE id=?", (id_registro,))
#         conn.commit()
#         mostrar_registros()
#     except IndexError:
#         messagebox.showwarning("Advertencia", "Por favor selecciona un registro.")

# btn_eliminar = tk.Button(registros, text="Eliminar Registro", font=("Helvetica", 12, "bold"), relief="flat",command=eliminar_registro)
# btn_eliminar.pack(pady=10)

# lista_registros = tk.Listbox(registros, font=("Arial", 12), bg="#FFFFFF", fg="#2D3748", borderwidth=0,highlightthickness=1, relief="flat")
# lista_registros.pack(padx=20, pady=10, expand=True)

# #Mostrar registros al inicio
# mostrar_registros()

# def irAtras():
#     subprocess.Popen(["python", "bienvenidos.py"])
#     registros.destroy()

# botonLogros=tk.Button(registros,text="Menu principal",font=("Helvetica", 12, "bold"), relief="flat", command=irAtras)
# botonLogros.pack(pady=20)


# #Iniciar el bucle principal
# registros.mainloop()

# #Cerrar conexión a la base de datos al finalizar
# conn.close()


# registros.mainloop()