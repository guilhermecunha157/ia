import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=4)

while True:
  sucesso, imagem = webcam.read()
  coodernadas, imagem_maos = rastreador.findHands(imagem)

  print(coodernadas)

  cv2.imshow("projento 4 - IA", imagem)

  if cv2.waitKey(1) != -1:
    break

webcam.release()
cv2.destroyWindow()
