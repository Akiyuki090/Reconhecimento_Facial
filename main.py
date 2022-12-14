import time
import os
import cv2
import mediapipe as mp


webcam = cv2.VideoCapture(0)

reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

while webcam.isOpened():
    validacao, frame = webcam.read()
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(imagem, rosto)
    else:
        cmd = 'Shutdown /h'
        os.system(cmd)
        cv2.destroyAllWindows()
        break

    cv2.imshow("CAM", imagem)
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()