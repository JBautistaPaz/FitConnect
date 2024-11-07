import tkinter as tk
import subprocess

entrenamientos=tk.Tk()
entrenamientos.title("Entrenamiento")
entrenamientos.geometry("700x600")
entrenamientos.config(bg="#F3F4F6")

label_total=tk.Label(entrenamientos, text="Tu Entrenamiento", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.config(bg="white")


texto1 = tk.Label(entrenamientos, text="Calentamiento Planchas 6x(40-50 Segundos)",font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
texto1.pack(pady=20)

texto2 = tk.Label(entrenamientos, text="1- Sentadillas 4x8", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
texto2.pack(pady=20)

texto3 = tk.Label(entrenamientos, text="2- Press de Pecho 4x6", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
texto3.pack(pady=20)

texto4 = tk.Label(entrenamientos, text="3- Remo con Mancuernas 4x12", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
texto4.pack(pady=20)

texto5 = tk.Label(entrenamientos, text="4- Press Militar con Mancuernas 4x8", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
texto5.pack(pady=20)

def irAtras():
    subprocess.Popen(["python", "./main.py"])
    entrenamientos.destroy()

boton_atras=tk.Button(entrenamientos,text="Atras",font=("Helvetica", 14, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command=irAtras)
boton_atras.pack(pady=20)

def destroy():
    entrenamientos.destroy()

boton_cerrar=tk.Button(entrenamientos, text="Cerrar Página",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= destroy)
boton_cerrar.pack()

entrenamientos.mainloop()