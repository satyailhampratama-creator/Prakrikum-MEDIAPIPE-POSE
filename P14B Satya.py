import  cv2
import  mediapipe as mp

mpose = mp.solutions.pose # inisiasi mediapipe pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0) #video dari webcam

while True:
    success, img = cap.read() #pembaca img
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #merubah warna bgr ke rgb
    hasil =pose.process(imgRGB) #melakukan pemrosesan dari citra imgRGB
    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS) #menggambar koneksi landmark
    for id,lm in enumerate(hasil.pose_landmarks.landmark):
        print(id, lm.x, lm.y) #eksrtaksi id, posisi x, posisi y

    cv2.imshow("webcam",img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release() # Tutup wabcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()