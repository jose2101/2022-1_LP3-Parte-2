# -*- coding: utf-8 -*-

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ SELECT * 
                FROM EDITORIAL
            """
cursor = conexion.cursor()
cursor.execute(consulta)
editoriales = cursor.fetchall()
# Acá libros es una lista... entonces utilizamos un for

for editorial in editoriales:
    print(editorial)
conexion.close()