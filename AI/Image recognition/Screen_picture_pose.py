from PIL import ImageGrab
import numpy as np
import cv2
import mediapipe as mp
import pyautogui
import pydirectinput
#import pywinauto
import win32api
import win32con 
from pynput import mouse 
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()
img_rgb = ImageGrab.grab((905,450,1005,600))
#print(pydirectinput.size())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('test.mp4', fourcc, 60, (img_rgb.size[0], img_rgb.size[1]))
width = float(1920) 
height = float(1080)
while True:
    img_rgb = ImageGrab.grab((905,450,1005,600))
    #img_rgb = ImageGrab.grab()
    img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_BGR2RGB)
    video.write(img_rgb)
    
    reault = pose.process(img_rgb)
    landmark = reault.pose_landmarks
    if reault.pose_landmarks != None:
        #pydirectinput.moveTo(None,1)
        #pywinauto.mouse.move(coords=(962, 540))
        #print(pydirectinput.position())
        pose_x = int(reault.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 100)
        pose_x = pose_x+905
        pose_y = int(reault.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 150)
        pose_y = pose_y+450
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,pose_x-960,pose_y-540)
        #pydirectinput.move(pose_x,pose_y)
        #win32api.SetCursorPos([960, 540+i])
        #pyautogui.click()
        #pyautogui.mouseDown()
        #print(pose_x-960,pose_y-540)
        #print(pydirectinput.position())
        

    #print(reault.pose_landmarks)
    if reault.pose_landmarks:
        mp_drawing.draw_landmarks(img_rgb,reault.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow('video',img_rgb)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()