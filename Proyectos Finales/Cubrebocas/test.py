import cv2
import os 
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

LABELS = ["Con_cubrebocas","Sin_cubrebocas"]

face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("cascade.xml")


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5) as face_detection:

    while True:
        ret, frame = cap.read()
        if ret == False: break
        
        heigth, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        if results.detections is not None:
            for detection in results.detections:
                xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(detection.location_data.relative_bounding_box.ymin * heigth)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(detection.location_data.relative_bounding_box.heigth * heigth)

                cv2.rectangle(frame, (xmin,ymin),(xmin + h, ymin + h), (0, 255, 0), 5)

        cv2.imshow("Frame", frame)
        k= cv2.waitKey(1)
        if k ==27:
            break

cap.release()
cv2.destroyAllWindows()
