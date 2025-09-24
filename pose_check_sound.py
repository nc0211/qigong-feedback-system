import cv2
import mediapipe as mp
import pygame  # 用來播放音效

# 初始化音效
pygame.mixer.init()
pygame.mixer.music.load("correct.mp3")  # 替換成你的音效檔案

# 初始化 MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# 開啟攝影機
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 轉換顏色 (MediaPipe 使用 RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 取得關鍵點座標
        landmarks = results.pose_landmarks.landmark

        left_wrist_y = landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y
        left_shoulder_y = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        right_wrist_y = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y
        right_shoulder_y = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y

        # 判斷手是否高於肩膀
        if left_wrist_y < left_shoulder_y and right_wrist_y < right_shoulder_y:
            cv2.putText(frame, "Correct Pose!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if not pygame.mixer.music.get_busy():  # 避免音效一直重複播放
                pygame.mixer.music.play()
        else:
            cv2.putText(frame, "Raise your hands higher!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 顯示影像
    cv2.imshow('Pose Detection', frame)

    # 按 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
