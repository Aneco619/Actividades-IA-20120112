import numpy as np
import cv2 as cv

# Cargar el clasificador Haarcascade para rostros
rostro = cv.CascadeClassifier('/Users/aneco/Documents/Instituto Tecnologico De Morelia/8vo Semestre/Inteligencia Artificial/Git Proyects/Proyectos Finales/Cubrebocas/cascade.xml')



cap = cv.VideoCapture(0)


x = y = w = h = 0
count = 0

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(150, 200))
    # scaleFactor si se aumenta puede generar falsos positivos Un valor más pequeño hará que se busquen objetos en escalas más pequeñas
    # minNeighbors + falsos positivos - menos sensible
    #tamaño mínimo del objeto que se considerará como una detección válida
    for(x, y, w, h) in rostros:
        m= int(h/2)
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame, f"({x}, {y})", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 5)

       # frame = cv.rectangle(frame, (x,y+m), (x+w, y+h), (255, 0 ,0), 2 )
       # img = 180- frame[y:y+h,x:x+w]
       # count = count + 1   
    
    #name = '/home/likcos/imgs/cara'+str(count)+'.jpg'
    #cv.imwrite(name, frame)
    cv.imshow('rostros', frame)
    #cv.imshow('cara', img)
    
    k = cv.waitKey(1)
    if k == 27:
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv.destroyAllWindows()

