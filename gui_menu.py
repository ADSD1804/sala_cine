from pymongo import MongoClient
import tkinter as tk
import gui_actualizarDatos
import gui_actualizarDatosPelicula
import gui_comprarPelicula
import gui_crearPelicula
import gui_mostrarPelicula
import gui_mostrarUsuarios
import gui_registroUsuario

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["usuario"]

ventana_principal = tk.Tk()
ventana_principal.title("Menú Principal")
ventana_principal.geometry("500x500")

def abrir_ventana_actualizar():
    gui_actualizarDatos.ventana.deiconify() 

def abrir_ventana_actualizar_pelicula():
    gui_actualizarDatosPelicula.ventana.deiconify()

def abrir_ventana_crear_pelicula():
    gui_crearPelicula.ventana.deiconify()

def abrir_ventana_mostrar_peliculas():
    gui_mostrarPelicula.ventana.deiconify()

def abrir_ventana_mostrar_usuarios():
    gui_mostrarUsuarios.ventana.deiconify()  

def abrir_ventana_registro_usuario():
    gui_registroUsuario.ventana.deiconify()

def abrir_ventana_comprar_peliculas():
    gui_comprarPelicula.ventana.deiconify()

boton_registro_usuario = tk.Button(ventana_principal, text="Registrar Usuario", command=abrir_ventana_registro_usuario)
boton_registro_usuario.pack(pady=10)

boton_actualizar = tk.Button(ventana_principal, text="Editar Datos de Usuario", command=abrir_ventana_actualizar)
boton_actualizar.pack(pady=10)

boton_mostrar_usuarios = tk.Button(ventana_principal, text="Mostrar Usuarios", command=abrir_ventana_mostrar_usuarios)
boton_mostrar_usuarios.pack(pady=10)

boton_crear_pelicula = tk.Button(ventana_principal, text="Crear Película", command=abrir_ventana_crear_pelicula)
boton_crear_pelicula.pack(pady=10)

boton_actualizar_pelicula = tk.Button(ventana_principal, text="Editar Datos de la Película", command=abrir_ventana_actualizar_pelicula)
boton_actualizar_pelicula.pack(pady=10)

boton_mostrar_peliculas = tk.Button(ventana_principal, text="Mostrar Películas", command=abrir_ventana_mostrar_peliculas)
boton_mostrar_peliculas.pack(pady=10)

boton_comprar_pelicula = tk.Button(ventana_principal, text="Comprar Película", command=abrir_ventana_comprar_peliculas)
boton_comprar_pelicula.pack(pady=10)

def cerrar_ventana():
    ventana_principal.withdraw()  # Oculta la ventana

boton_cerrar = tk.Button(ventana_principal, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()

ventana_principal.mainloop()