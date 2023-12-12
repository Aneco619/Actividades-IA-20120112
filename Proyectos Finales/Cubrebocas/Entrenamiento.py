import cv2
import os
import numpy as np

direccion = '/Users/aneco/Documents/Instituto Tecnologico De Morelia/8vo Semestre/Inteligencia Artificial/Git Proyects/Proyectos Finales/Cubrebocas/Fotos'
lista = os.listdir(direccion)

etiquetas = []
rostros = []
con = 0

for nameDir in lista:
    nombre = os.path.join(direccion, nameDir)

    if os.path.isdir(nombre):
        for fileName in os.listdir(nombre):
            filePath = os.path.join(nombre, fileName)

            # Verificar si es un archivo de imagen
            if fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                # Leer la imagen en escala de grises
                imagen = cv2.imread(filePath, 0)

                # Verificar si la lectura de la imagen fue exitosa
                if imagen is not None:
                    etiquetas.append(con)
                    rostros.append(imagen)
                else:
                    print(f"Error al leer la imagen: {filePath}")
            else:
                print(f"Archivo no válido: {filePath}")

        con += 1
    else:
        print(f"{nombre} no es un directorio.")

reconocimiento = cv2.face.LBPHFaceRecognizer_create()

reconocimiento.train(rostros, np.array(etiquetas))

reconocimiento.write('ModeloLBP.xml')
print("Modelo creado")
