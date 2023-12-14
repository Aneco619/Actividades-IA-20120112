import cv2 as cv

rostro = cv.CascadeClassifier('/Users/aneco/Documents/Instituto Tecnologico De Morelia/8vo Semestre/Inteligencia Artificial/Git Proyects/Proyectos Finales/Cubrebocas/cascade.xml')
cap = cv.VideoCapture(0)
i=0

while True:
    ret, frame = cap.read()
    i=i+1
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=30, minSize=(80, 80))
    for (x, y, w, h) in rostros:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        cv.putText(frame, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv.imshow('rostros', frame)
    k = cv.waitKey(1)
    if k == ord('s'):
        break

cap.release()
cv.destroyAllWindows()