# limit the number of cpus used by high performance libraries
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

import sys
sys.path.insert(0, './yolov5')
import numpy as np
import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
import random
from yolov5.models.experimental import attempt_load
from yolov5.utils.downloads import attempt_download
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.datasets import LoadImages, LoadStreams
from yolov5.utils.general import (LOGGER, check_img_size, non_max_suppression, scale_coords, 
                                  check_imshow, xyxy2xywh, increment_path)
from yolov5.utils.torch_utils import select_device, time_sync
from yolov5.utils.plots import Annotator, colors
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
from grabscreen import grab_screen


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # yolov5 deepsort root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

conf_thres=0.25
iou_thres=0.45
#classes = [0,1,2,3,5,6,7]
classes = None
agnostic_nms=False
max_det=1000
device=''
project=ROOT / 'runs/detect'
name='results'
exist_ok=False
save_txt=False
#weights=ROOT / 'yolov5s.pt'
weights=ROOT / 'best.pt'
imgsz=(1080, 1920)
half=False
augment=False
visualize=False
dnn=False
names =  ['Pedestrian']
colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]
#data=ROOT / 'data/coco128.yaml'
data=ROOT / 'data/apex_Pedestrian.yaml'
'''names = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush']'''


cfg = get_config()
cfg.merge_from_file('deep_sort/configs/deep_sort.yaml')
device = select_device('')
deepsort = DeepSort('osnet_x0_25',
                        device,
                        max_dist=cfg.DEEPSORT.MAX_DIST,
                        max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                        max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                        )

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

def letterbox(img, new_shape=(640, 640), color=(114, 114, 114), auto=False, scaleFill=False, scaleup=True):
    # Resize image to a 32-pixel-multiple rectangle https://github.com/ultralytics/yolov3/issues/232
    shape = img.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, 64), np.mod(dh, 64)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)

device = select_device(device)
model = DetectMultiBackend(weights, device=device, dnn=dnn)
view_img = check_imshow()
dt, seen = [0.0, 0.0, 0.0], 0

while True:

    img_rgb = grab_screen((0,0,1920,1080))
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    img = letterbox(img_rgb)[0]
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img)
    t1 = time_sync()
    img = torch.from_numpy(img).to(device).unsqueeze(0)
    img = img.half() if half else img.float()
    img /= 255.0 
    t2 = time_sync()
    dt[0] += t2 - t1

    results = model(img, augment=augment, visualize=visualize)
    t3 = time_sync()
    dt[1] += t3 - t2
    results = non_max_suppression(results, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
    dt[2] += time_sync() - t3
    gn = torch.tensor(img_rgb.shape)[[1, 0, 1, 0]]
    results = results[0]
    if results is not None and len(results):
        results[:, :4] = scale_coords(img.shape[2:], results[:, :4], img_rgb.shape).round()
        for c in results[:, -1].unique():
            n = (results[:, -1] == c).sum()  # detections per class

        img_object = []
        cls_object = []
        hero_conf = 0
        hero_index = 0
        
        xywhs = xyxy2xywh(results[:, 0:4])
        confs = results[:, 4]
        clss = results[:, 5]

        t4 = time_sync()
        outputs = deepsort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), img_rgb)
        t5 = time_sync()
        if len(outputs) > 0:
            for j, (output, conf) in enumerate(zip(outputs, confs)):

                bboxes = output[0:4]
                id = output[4]
                cls = output[5]

                c = int(cls)  # integer class
                label = f'{id} {names[c]} {conf:.2f}'
                plot_one_box(bboxes, img_rgb, label=label, color=colors[int(cls)], line_thickness=2)

    img_rgb = cv2.resize(img_rgb, (1920,1080))
    if view_img:
        cv2.imshow('window', img_rgb)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
            raise StopIteration
    