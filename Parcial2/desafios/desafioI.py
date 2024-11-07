import tkinter as tk
import subprocess

desafioI = tk.Tk()
desafioI.title("Intermedios")
desafioI.geometry("700x600")
desafioI.config(bg="#F3F4F6") 

label_total = tk.Label(desafioI, text="Desafío Para Intermedio", font=("Helvetica", 18, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

texto1 = tk.Label(desafioI,text="1- Sentadillas con barra: 4 series de 8-10 repeticiones",font=("Helvetica", 14),bg="#F3F4F6",fg="#4A5568"
)
texto1.pack(pady=10)

texto2 = tk.Label(desafioI, text="2- Press de banca: 4 series de 6-8 repeticiones", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568")
texto2.pack(pady=10)

texto3 = tk.Label(desafioI, text="3- Peso muerto con barra: 4 series de 6-8 repeticiones", font=("Helvetica", 14), bg="#F3F4F6",fg="#4A5568")
texto3.pack(pady=10)

def irAtras():
    subprocess.Popen(["python", "./paginas/desafios.py"])
    desafioI.destroy()

boton_atras = tk.Button(desafioI, text="Atrás", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#A0AEC0",activeforeground="#2D3748", relief="flat" ,command=irAtras
)
boton_atras.pack(pady=20)

def destroy():
    desafioI.destroy()

boton_cerrar=tk.Button(desafioI, text="Cerrar Página",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= destroy)
boton_cerrar.pack(pady=20)

desafioI.mainloop()
