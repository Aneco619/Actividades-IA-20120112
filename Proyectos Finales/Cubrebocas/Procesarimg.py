import os
import cv2

# Ruta de la carpeta principal que contiene las imágenes
carpeta_principal = '/Users/aneco/Downloads/ppp'

# Ruta donde quieres guardar las imágenes ajustadas
ruta_destino = '/Users/aneco/Documents/Instituto Tecnologico De Morelia/8vo Semestre/Inteligencia Artificial/Git Proyects/Proyectos Finales/Cubrebocas/Fotos/p/cubrebocas'

# Ancho y alto deseados
nuevo_ancho = 150
nuevo_alto = 200

# Crear la carpeta de destino si no existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Iterar sobre los archivos en la carpeta principal
for archivo in os.listdir(carpeta_principal):
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_principal, archivo)
    
    # Leer la imagen en color
    imagen_color = cv2.imread(ruta_archivo)

    # Verificar si la lectura de la imagen fue exitosa
    if imagen_color is not None:
        # Ajustar el tamaño de la imagen
        imagen_ajustada = cv2.resize(imagen_color, (nuevo_ancho, nuevo_alto), interpolation=cv2.INTER_CUBIC)

        # Convertir la imagen a escala de grises
        imagen_gris = cv2.cvtColor(imagen_ajustada, cv2.COLOR_BGR2GRAY)

        # Guardar la imagen ajustada en escala de grises en la nueva ubicación
        nueva_ruta = os.path.join(ruta_destino, f'{archivo}')
        cv2.imwrite(nueva_ruta, imagen_gris)
    else:
        print(f"Error al leer la imagen: {ruta_archivo}")

print('Proceso completado.')
