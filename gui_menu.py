from pymongo import MongoClient
import tkinter as tk

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]
coleccion = database["usuario"]

#boton para actualizar datos

#boton para registrar usuario