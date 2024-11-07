import tkinter as tk
import subprocess

desafioP = tk.Tk()
desafioP.title("Principiante")
desafioP.geometry("700x600")
desafioP.config(bg="#F3F4F6")  

label_total = tk.Label(desafioP, text="Desafío Para Principiantes", font=("Helvetica", 18, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

texto1 = tk.Label(desafioP, text="1- Sentadillas: 3 series de 12 repeticiones", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568")
texto1.pack(pady=10)

texto2 = tk.Label(desafioP, text="2- Flexiones: 3 series de 8-12 repeticiones", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568")
texto2.pack(pady=10)

texto3 = tk.Label(desafioP,text="3- Peso muerto con mancuernas: 3 series de 10 repeticiones",font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568")
texto3.pack(pady=10)

def irAtras():
    subprocess.Popen(["python", "./paginas/desafios.py"])
    desafioP.destroy()

boton_atras = tk.Button(desafioP, text="Atrás", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#A0AEC0",activeforeground="#2D3748", relief="flat" ,command=irAtras
)
boton_atras.pack(pady=20)

def destroy():
    desafioP.destroy()

boton_cerrar=tk.Button(desafioP, text="Cerrar Página",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= destroy)
boton_cerrar.pack(pady=20)

desafioP.mainloop()