
import cv2
import numpy as np
import random
import time
import win32api
import win32con
import mss
import pyautogui



def move_mouse(x, y):
    # 使用 win32api 將鼠標移動到 (x, y) 坐標
    win32api.SetCursorPos((x, y))
    # 模擬鼠標左鍵按下（如果需要）
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def is_right_mouse_button_pressed():
    # 檢查右鍵是否被按下
    return win32api.GetAsyncKeyState(win32con.VK_RBUTTON) & 0x8000
    
def plot_one_box(x, img, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def detect_purple_area_contour(region = None):
    # 使用 MSS 來擷取螢幕
    with mss.mss() as sct:
        while True:
            if region:
                monitor = {
                    "left": region[0],
                    "top": region[1],
                    "width": region[2] - region[0],
                    "height": region[3] - region[1]
                }
                # 抓取特定範圍
                screen = sct.grab(monitor)
            # 抓取整個螢幕
            else:
                screen = sct.grab(sct.monitors[1])

            # 將圖片轉換為 NumPy 陣列
            img = np.array(screen)

            # 將圖片轉換為 BGR 格式（因為螢幕截圖是 RGB 格式）
            #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

            # 定義目標顏色的 RGB 範圍
            target_color = np.array([71, 131, 171])
            
            # 設定一個範圍，這裡我們給一個小的偏差以考慮色彩匹配的誤差
            lower_bound = target_color - 30
            upper_bound = target_color + 90

            # 確保上下限範圍在 [0, 255] 之內
            lower_bound = np.clip(lower_bound, 0, 255)
            upper_bound = np.clip(upper_bound, 0, 255)

            # 將圖像從 BGR 轉換為 HSV 色彩空間
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # 根據紫色的範圍創建遮罩
            mask_purple = cv2.inRange(hsv_img, lower_bound, upper_bound)

            # 對遮罩進行中值濾波以減少噪點
            mask_purple = cv2.medianBlur(mask_purple, 7)

            # 查找遮罩中的輪廓
            contours, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # 初始化變數以存儲中心點
            centers = []

            # 遍歷輪廓並繪製邊界框
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                if w * h > 1000:  # 過濾掉太小的區域
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    center_x = x + w // 2
                    center_y = y + h // 2
                    centers.append((center_x, center_y))
                    # 在圖像上繪製中心點
                    cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)
                    print(center_x,center_y)
                    if is_right_mouse_button_pressed():
                        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,center_x+region[0]-960,center_y+region[1]-550)
                    # 將鼠標移動到中心點
                    #move_mouse(center_x, center_y)


            # 顯示結果
            cv2.imshow('Detected Purple Areas', img)

            # 按下 'q' 鍵退出循環
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

if __name__ == "__main__":
    region = (780,470,1134,680)
    detect_purple_area_contour(region)