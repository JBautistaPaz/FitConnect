import tkinter as tk
import subprocess

desafioE = tk.Tk()
desafioE.title("Expertos")
desafioE.geometry("700x600")
desafioE.config(bg="#F3F4F6")  

label_total = tk.Label( desafioE, text="Desafío Para Expertos", font=("Helvetica", 18, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.pack(pady=20)

texto1 = tk.Label( desafioE, text="1- Sentadillas Frontales: 5 series de 3-5 repeticiones", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568", wraplength=700  )
texto1.pack(pady=10)

texto2 = tk.Label( desafioE, text="2- Press de Banca con Barra: 5 series de 3-5 repeticiones", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568", wraplength=700)
texto2.pack(pady=10)

texto3 = tk.Label( desafioE, text="3- Peso Muerto: 5 series de 3-5 repeticiones (al 85% de tu máximo)", font=("Helvetica", 14), bg="#F3F4F6", fg="#4A5568", wraplength=700)
texto3.pack(pady=10)

def irAtras():
    subprocess.Popen(["python", "./paginas/desafios.py"])
    desafioE.destroy()

boton_atras = tk.Button(desafioE, text="Atrás", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#A0AEC0",activeforeground="#2D3748", relief="flat" ,command=irAtras)
boton_atras.pack(pady=20)

def destroy():
    desafioE.destroy()

boton_cerrar=tk.Button(desafioE, text="Cerrar Página",font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC",activeforeground="#FFFFFF", relief="flat", command= destroy)
boton_cerrar.pack(pady=20)

desafioE.mainloop()
