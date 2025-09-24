import cv2
import mediapipe as mp
import pygame  # play the sound

# 初始化音效
pygame.mixer.init()
pygame.mixer.music.load("correct.mp3")  # the sound I assigned

# initial MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# turn on camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # change color (MediaPipe uses RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # get key point coordinates
        landmarks = results.pose_landmarks.landmark

        left_wrist_y = landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y
        left_shoulder_y = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        right_wrist_y = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST].y
        right_shoulder_y = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y

        # determine whether your hands are above your shoulders
        if left_wrist_y < left_shoulder_y and right_wrist_y < right_shoulder_y:
            cv2.putText(frame, "Correct Pose!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if not pygame.mixer.music.get_busy():  # prevent sound effects from playing repeatedly
                pygame.mixer.music.play()
        else:
            cv2.putText(frame, "Raise your hands higher!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # display image
    cv2.imshow('Pose Detection', frame)

    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
