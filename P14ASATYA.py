import cv2
import mediapipe as mp
mpose = mp.solutions.pose #inisiasi media pipe pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0) #video dari webcam
while True:
    success, img = cap.read() #pembacaan image
    if not success:
        print ("kamera tidak terbaca")
        break
    imgrgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image
    if hasil.pose_landmarks:
        print ("terdeteksi")
    else:
        print ("tidak terdeteksi")
    cv2.imshow("webcam",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() #tutup webcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()
