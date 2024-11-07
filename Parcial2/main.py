import tkinter as tk
import subprocess

main=tk.Tk()
main.title("Main")
main.geometry("700x600")
main.config(bg="#F3F4F6")

label_total=tk.Label(main, text="Bienvenido a tu aplicación favorita de Fitness!!", font=("Helvetica", 14, "bold"),
bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

def abrir_desafio():
    # entrar el archivo desafio.py
    subprocess.Popen(["python", "paginas/desafios.py"])
    main.destroy()

boton_abrir_desafio = tk.Button(main, text="Desafíos", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",
activeforeground="#FFFFFF", relief="flat", command=abrir_desafio)
boton_abrir_desafio.pack(pady=10)

def irEntrenamiento():
    subprocess.Popen(["python", "paginas/entrenamientos.py"])
    main.destroy()

boton_entrenamientos = tk.Button(main,text="Entrenamientos", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=irEntrenamiento)
boton_entrenamientos.pack(pady=10)

def irLogros():
    subprocess.Popen(["python", "paginas/logros.py"])
    main.destroy()

boton_logros=tk.Button(main,text="Logros",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF",relief="flat", command=irLogros)
boton_logros.pack(pady=10)

main.mainloop() 