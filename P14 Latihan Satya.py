import cv2
import mediapipe as mp
mpose = mp.solutions.pose #inisiasi media pipe pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0) #video dari webcam
while True:
    success, img = cap.read()
    if not success:
        break
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)
    if hasil.pose_landmarks:
        #gambar semua landmark
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS)
        #ambil semua landmark
        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y)
        #ambil landmark tangan kanan dan kiri
        lm = hasil.pose_landmarks.landmark
        shoulder_right = lm[mpose.PoseLandmark.RIGHT_SHOULDER.value]
        wrist_right = lm[mpose.PoseLandmark.RIGHT_WRIST.value]
        shoulder_left = lm[mpose.PoseLandmark.LEFT_SHOULDER.value]
        wrist_left = lm[mpose.PoseLandmark.LEFT_WRIST.value]
        #deteksi tangan kanan
        if wrist_right.y < shoulder_right.y:
            cv2.putText(img, "Tangan kanan Terdeteksi", (10,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,225,0), 2)
        #deteksi tangan kiri
        if wrist_left.y < shoulder_left.y:
            cv2.putText(img, "Tangan Kiri Terdeteksi", (10,90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,225), 2)
    cv2.imshow("webcam",img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
