from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

from usuarios.create_user import ingresar_usuario
from usuarios.delete_user import borrar_usuario

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]
coleccion = database["usuario"]

ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("600x500")

tk.Label(ventana, text="Creación de usuario nuevo").pack()

tk.Label(ventana, text="Ingrese su cedula: ").pack()
cedula = tk.Entry(ventana)
cedula.pack()

tk.Label(ventana, text="Ingrese su nombre: ").pack()
nombre = tk.Entry(ventana)
nombre.pack()

tk.Label(ventana, text="Ingrese su correo: ").pack()
correo = tk.Entry(ventana)
correo.pack()

tk.Label(ventana, text="Ingrese sus preferencias: ").pack()

lista_preferencias = Listbox(ventana, selectmode= "multiple",
                       yscrollcommand = Scrollbar.set)

lista_preferencias.pack()

values = ["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción", "Aventura", "Animación", "Historia", "Documental"]                        

for value in range(len(values)):
    lista_preferencias.insert(value, values[value])
    
def agregar_usuario():
    seleccionadas = lista_preferencias.curselection()
    preferencias = [lista_preferencias.get(i) for i in seleccionadas]
    
    ingresar_usuario(cedula.get(), nombre.get(), correo.get(), preferencias)
    messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
    
def eliminar_usuario():
    cedula_eliminar = cedula.get()
    borrar_usuario(cedula_eliminar)
    messagebox.showinfo("Éxito", "Usuario borrado con éxito.")

tk.Button(ventana, text="Ingresar", command = agregar_usuario).pack()
tk.Button(ventana, text="Eliminar", command = eliminar_usuario).pack()

ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw()  

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()