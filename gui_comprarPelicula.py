from tkinter import messagebox
from pymongo import MongoClient
import tkinter as tk

from gui_mostrarPelicula import mostrar_peliculas
from usuarios.comprar_ticket import comprar_entradas

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["pelicula"]

ventana = tk.Tk()
ventana.title("Comprar Peliculas")
ventana.geometry("400x400")

tk.Label(ventana, text="Comprar Peliculas").pack()

tk.Label(ventana, text="Ingrese la cedula del usuario:").pack()
cedula = tk.Entry(ventana)
cedula.pack()

tk.Label(ventana, text="Ingrese el nombre de la pelicula:").pack()
nombre_pelicula = tk.Entry(ventana)
nombre_pelicula.pack()

tk.Label(ventana, text="Ingrese la cantidad de entradas para la pelicula:").pack()
cantidad_entradas = tk.Entry(ventana)
cantidad_entradas.pack()

def mostrar_recibo(nombre_pelicula, cantidad, total):
    ventana_recibo = tk.Toplevel(ventana)
    ventana_recibo.title("Recibo de Compra")
    ventana_recibo.geometry("300x200")
    

    tk.Label(ventana_recibo, text="Recibo de Compra", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana_recibo, text=f"Película: {nombre_pelicula}").pack(pady=5)
    tk.Label(ventana_recibo, text=f"Cantidad de Entradas: {cantidad}").pack(pady=5)

    boton_cerrar = tk.Button(ventana_recibo, text="Cerrar", command=ventana_recibo.destroy)
    boton_cerrar.pack(pady=10)

def comprar_pelicula():
    cedula_texto = cedula.get()
    nombre_pelicula_texto = nombre_pelicula.get()
    cantidad_entradas_texto = cantidad_entradas.get()

    try:
        cantidad_entradas_num = int(cantidad_entradas_texto)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para la cantidad de entradas.")
        return
    
    precio_por_entrada = 10
    total_a_pagar = cantidad_entradas_num * precio_por_entrada
    
    resultado_compra = comprar_entradas(cedula_texto, nombre_pelicula_texto, cantidad_entradas_num)

    if resultado_compra.startswith("Error"):
        messagebox.showerror("Error", resultado_compra)
    else:
        messagebox.showinfo("Compra realizada", resultado_compra)
        mostrar_recibo(nombre_pelicula_texto, cantidad_entradas_num, total_a_pagar)
        mostrar_peliculas()

button = tk.Button(ventana, text="Comprar", command=comprar_pelicula)
button.pack()

ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw()

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()