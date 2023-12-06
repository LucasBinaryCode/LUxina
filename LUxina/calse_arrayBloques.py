from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from LUxina.con_InterfazGrafica import main
import json
import sqlite3

class LUxina:

    patron_alternado = [[1,0,1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0,1,0],
                        [0,1,0,1,0,1,0,1,0,1],
                        [1,0,1,0,1,0,1,0,1,0]]
    
    casa = [[1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,1,1,1,1],
            [1,1,1,0,0,0,0,1,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,0,0,0,0,0,0,0,0,1]]

    cara = [[0,0,0,1,0,0,1],
            [0,0,0,1,0,0,1],
            [0,0,0,1,0,0,1],
            [0],
            [0,1,0,0,0,0,0,0,1],
            [0,1,1,0,0,0,0,1,1],
            [0,0,1,1,1,1,1,1]]



    def __init__(self):
        self.app = Ursina()


    
    # 1 = Editoro camara     2 = controlador en primera persona

    def iniciar_ventana(self, tipo_camara):

        if tipo_camara == "editor":
            self.camera = EditorCamera()
        elif tipo_camara == "person":
            self.camera = FirstPersonController()
        else:
            self.camera = EditorCamera()
        self.app.run()

    def con_ventana_grafica(self):
        matriz = main()
        return matriz

    def mandar_matriz_baseDatos(self, matriz, nombre_base, nombre_tabla, nombre_columna):

        conn = sqlite3.connect(nombre_base)
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO {nombre_tabla} ({nombre_columna}) VALUES (?)', (self.convertir_matriz_json(matriz),))

        conn.commit()
        conn.close()

    def convertir_matriz_json(self, matriz):
        matriz_como_cadena = json.dumps(matriz)
        return matriz_como_cadena

    def desconvertir_matriz(self, matriz_como_cadena):
        matriz = json.loads(matriz_como_cadena)
        return matriz

    def analizar_array(self, lista, y, z, color_ingresado):

        for i in range(len(lista)):
            if lista[i] == 1:
                e = Entity(model = "cube", color = color_ingresado, texture = "white_cube", position = Vec3(i, y, z))

    def invertir_matriz(self,matriz):
        return matriz[::-1]

    def dibujar_matriz(self, matriz, color_ingresado, modelo,  x, y,z, profundida, escala, tipo_collider):
        i = 0
        j = 0
        matriz = self.invertir_matriz(matriz)
        for k in range(profundida):
            for fila in matriz:
                for elemento in fila:
                    if elemento == 1:
                        e = Entity(model = modelo, color = color_ingresado, texture = "white_cube", position = Vec3((x+j)*escala, (y+i)*escala, (z+k)*escala), scale = escala, collider = tipo_collider)
                    j += 1
                j = 0
                i +=1
            i = 0
    
    def dibujar_escalera(self, matriz, color_ingresado, modelo,  x, y, z, profundida, escala, tipo_collider):
        i = 0
        j = 0
        matriz = self.invertir_matriz(matriz)
        for k in range(profundida):
            for fila in matriz:
                for elemento in fila:
                    if elemento == 1:
                        e = Entity(model = modelo, color = color_ingresado, texture = "white_cube", position = Vec3((x+j)*escala, (y+i)*escala, (z+i)*escala), scale = escala, collider = tipo_collider)
                    j += 1
                j = 0
                i +=1
            i = 0
    
    def dibujar_matriz_CambiarModelo_profundidad(self, matriz, color_ingresado, modelo,  x, y,z, profundida, escala, tipo_collider, rango_eliminar, matriz_sustituta):
        rango1 = rango_eliminar[0] 
        rango2 = rango_eliminar[1] 
        k = 0
        j = 0
        i = 0
        matriz = self.invertir_matriz(matriz)
        matriz_sustituta = self.invertir_matriz(matriz_sustituta)
        for k in range(profundida):

            if k >= rango1 and k <rango2:
                for fila in matriz_sustituta:
                    for elemento in fila:
                        if elemento == 1:
                            e = Entity(model = modelo, color = color_ingresado, texture = "white_cube", position = Vec3((x+j)*escala, (y+i)*escala, (z+k)*escala), scale = escala, collider = tipo_collider)
                        j += 1
                    j = 0
                    i +=1
                i = 0
                
            else:
                for fila in matriz:
                    for elemento in fila:
                        if elemento == 1:
                            e = Entity(model = modelo, color = color_ingresado, texture = "white_cube", position = Vec3((x+j)*escala, (y+i)*escala, (z+k)*escala), scale = escala, collider = tipo_collider)
                        j += 1
                    j = 0
                    i +=1
                i = 0

