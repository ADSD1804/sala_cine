from pymongo import MongoClient
import tkinter as tk

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["usuario"]

ventana = tk.Tk()
ventana.title("Mostrar Usuarios")
ventana.geometry("400x400")

def mostrar_todos_usuarios():
    usuarios = coleccion.find() 
    usuarios_texto = ""
    
    for usuario in usuarios:
        usuarios_texto += f"Cédula: {usuario.get('cedula', 'N/A')},\nNombre: {usuario.get('nombre', 'N/A')}\nCorreo: {usuario.get('correo')}\nPreferencias: {usuario.get('preferencias')}\nHistorial de Compras: {usuario.get('historial_compra')}\n\n"
    
    ventana_usuarios = tk.Toplevel(ventana)
    ventana_usuarios.title("Usuarios Registrados")
    ventana_usuarios.geometry("400x300")  

    texto_usuarios = tk.Text(ventana_usuarios, wrap=tk.WORD)
    texto_usuarios.pack(expand=True, fill=tk.BOTH)

    texto_usuarios.insert(tk.END, usuarios_texto)

    texto_usuarios.config(state=tk.DISABLED)

boton_mostrar_todos = tk.Button(ventana, text="Mostrar Todos los Usuarios", command=mostrar_todos_usuarios)
boton_mostrar_todos.pack()

ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw()  # Oculta la ventana

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()