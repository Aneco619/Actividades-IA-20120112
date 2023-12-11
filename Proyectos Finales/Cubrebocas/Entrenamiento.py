import cv2
import os
import numpy as np

direccion = '/Users/aneco/Documents/Instituto Tecnologico De Morelia/8vo Semestre/Inteligencia Artificial/Git Proyects/Proyectos Finales/Cubrebocas/Fotos'
lista = os.listdir(direccion)

etiquetas = []
rostros = []
con = 0

for nameDir in lista:
    nombre = direccion + '/' + nameDir

    for fileName in os.listdir(nombre):
        etiquetas.append(con)
        rostros.append(cv2.imread(nombre + '/' + fileName,0))

    con = con + 1

reconocimiento = cv2.face.LBPHFaceRecognizer_create()

reconocimiento.train(rostros, np.array(etiquetas))

reconocimiento.write('ModeloLBP.xml')
print("Modelo creado")
