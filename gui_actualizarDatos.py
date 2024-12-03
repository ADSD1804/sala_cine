from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

from usuarios.update_user import actualizar_usuario

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["usuario"]

ventana = tk.Tk()
ventana.title("Actualizar Usuario")
ventana.geometry("400x400")

tk.Label(ventana, text="Actualizar Datos del Usuario").pack()

tk.Label(ventana, text="Ingrese la cédula del usuario:").pack()
cedula_entry = tk.Entry(ventana)
cedula_entry.pack()

tk.Label(ventana, text="Nuevo Nombre:").pack()
nuevo_nombre_entry = tk.Entry(ventana)
nuevo_nombre_entry.pack()

tk.Label(ventana, text="Nuevo Correo:").pack()
nuevo_correo_entry = tk.Entry(ventana)
nuevo_correo_entry.pack()

preferencias_disponibles = ["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción", "Aventura", "Animación", "Historia", "Documental"]

tk.Label(ventana, text="Seleccione Nuevas Preferencias:").pack()
preferencias_listbox = tk.Listbox(ventana, selectmode=tk.MULTIPLE) 
for preferencia in preferencias_disponibles:
    preferencias_listbox.insert(tk.END, preferencia) 
preferencias_listbox.pack()

def actualizar_datos():
    cedula = cedula_entry.get()
    nuevo_nombre = nuevo_nombre_entry.get()
    nuevo_correo = nuevo_correo_entry.get()
    
    indices_seleccionados = preferencias_listbox.curselection()
    nuevas_preferencias = [preferencias_disponibles[i] for i in indices_seleccionados]
    
    if cedula:
        actualizar_usuario(cedula, nuevo_nombre if nuevo_nombre else None, nuevo_correo if nuevo_correo else None, nuevas_preferencias if nuevas_preferencias else None)
        messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una cédula.")

tk.Button(ventana, text="Actualizar Usuario", command= actualizar_datos).pack()

ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw() 

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()