import tkinter as tk
import subprocess

archivo_texto = "texto_guardado.txt"

def guardar_texto():
    texto = cuadro_texto.get("1.0", "end-1c") 
    with open(archivo_texto, "w") as archivo:
        archivo.write(texto) 

def recuperar_texto():
    try:
        with open(archivo_texto, "r") as archivo:
            texto = archivo.read() 
            cuadro_texto.insert("1.0", texto) 
    except FileNotFoundError:
        pass

entrenamientos = tk.Tk()
entrenamientos.title("Entrenamiento!!")
entrenamientos.geometry("700x600")
entrenamientos.config(bg="#F3F4F6")


label_total = tk.Label(entrenamientos, text="Tu Entrenamiento", font=("Helvetica", 14, "bold"), bg="#F3F4F6", fg="#2D3748")
label_total.config(bg="white")
label_total.pack(pady=20)

cuadro_texto = tk.Text(entrenamientos, height=10, width=40)
cuadro_texto.pack(pady=20)

def mostrar_texto():
    texto = cuadro_texto.get("1.0", "end-1c")  
    print("Texto ingresado:", texto)

def eliminar_texto():
    cuadro_texto.delete("1.0", "end")  

def habilitar_edicion():
    cuadro_texto.config(state=tk.NORMAL)  

def deshabilitar_edicion():
    cuadro_texto.config(state=tk.DISABLED)  

boton_mostrar = tk.Button(entrenamientos, text="Mostrar Texto", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=mostrar_texto)
boton_mostrar.pack(pady=10)

boton_eliminar = tk.Button(entrenamientos, text="Eliminar Texto", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=eliminar_texto)
boton_eliminar.pack(pady=10)

boton_editar = tk.Button(entrenamientos, text="Habilitar Edición", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=habilitar_edicion)
boton_editar.pack(pady=10)

boton_deshabilitar = tk.Button(entrenamientos, text="Deshabilitar Edición", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF",  activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=deshabilitar_edicion)
boton_deshabilitar.pack(pady=10)

def irAtras():
    guardar_texto() 
    subprocess.Popen(["python", "./Parcial2/main.py"])
    entrenamientos.destroy()

boton_atras = tk.Button(entrenamientos, text="Atras", font=("Helvetica", 14, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=irAtras)
boton_atras.pack(pady=20)

def destroy():
    entrenamientos.destroy()

boton_cerrar = tk.Button(entrenamientos, text="Cerrar Página", font=("Helvetica", 12, "bold"), bg="#4FD1C5", fg="#FFFFFF", activebackground="#38B2AC", activeforeground="#FFFFFF", relief="flat", command=destroy)
boton_cerrar.pack()

recuperar_texto()

deshabilitar_edicion()

entrenamientos.mainloop()
