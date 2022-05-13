from pynput.mouse import Listener
from PIL import ImageGrab
import numpy as np
import cv2
import mediapipe as mp
import win32api
import win32con 
import pyautogui

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()
img_rgb = ImageGrab.grab((905,450,1005,600))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('test.mp4', fourcc, 60, (img_rgb.size[0], img_rgb.size[1]))
width = float(1920) 
height = float(1080)

AI_type =  False

def on_click(x, y, button, is_press):
    global AI_type
    #print(f"鼠標{button}鍵在({x}, {y})處{'按下' if is_press else '松開'}")
    if is_press == True and str(button) == 'Button.right':
        print(f"鼠標{button}鍵在({x}, {y})處{'按下' if is_press else '松開'}")
        AI_type = True
    if is_press == False and str(button) == 'Button.right':
        AI_type = False


listener = Listener(on_click=on_click)
listener.start()

while True:
    img_rgb = ImageGrab.grab((805,450,1105,600))
    #img_rgb = ImageGrab.grab()
    img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_BGR2RGB)
    video.write(img_rgb)
    if AI_type:
        reault = pose.process(img_rgb)
        landmark = reault.pose_landmarks
        if reault.pose_landmarks != None:
            pose_x = int(reault.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 300)
            pose_x = pose_x+805
            pose_y = int(reault.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 150)
            pose_y = pose_y+450
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,pose_x-960,pose_y-540)
            pyautogui.click()
        if reault.pose_landmarks:
            mp_drawing.draw_landmarks(img_rgb,reault.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow('video',img_rgb)
    if cv2.waitKey(1) == ord('q'):
        break
listener.stop()
