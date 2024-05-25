import cv2
import math
import xlwt
import pyautogui
import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QImage, QPixmap, QFont
from tkinter import filedialog
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from cal_ui2 import Ui_MainWindow
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar
from rich.console import Console
from rich.style import Style
import matplotlib.pyplot as plt
import io
import os
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

arr_x = []
arr_y = []
arr = []
console = Console()
style = Style(bgcolor="red", color="white")
appdata_dir = os.path.expandvars("%APPDATA%\\CAPA\\log.txt")

def log(str):
    with open(appdata_dir, "a") as log_file:
        log_file.write(str + "\n")


def printt(str):
    console.print(str, style=style)


def test(a, b):
    return a + b


def math2cv(x, y):
    return x, -y


def cv2math(x, y):
    return x, -y


def getfilepath():
    # 初始化一个tkinter窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    a = filedialog.askopenfilename(
        title="选择文件", filetypes=[("视频文件", "*.mp4;*.mov"), ("所有文件", "*.*")]
    )
    # 完成选择后，销毁窗口
    root.destroy()
    return a


def showimg(lab: QLabel, buf):
    fig = Figure()
    lab.setStyleSheet("")
    fig.savefig(buf, format='png')
    buf.seek(0)  # 移动到流的开始处

    # 从BytesIO对象创建QPixmap
    pixmap = QPixmap()
    pixmap.loadFromData(buf.getvalue(), 'PNG')
    lab.setPixmap(
        pixmap.scaled(
            lab.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation,
        )
    )


def setBut(but: QPushButton):
    but.setStyleSheet(
        "QPushButton{font-size: 13pt;background-color: #9bc2df;border-radius:10px;padding:2px 4px;border-style: outset;}"
        "QPushButton:hover{background-color:#b1deff; color: black;}"
        "QPushButton:pressed{background-color:#b1deff;border-style: inset;}")


def setButs(buts):
    for but in buts:
        setBut(but)


def get_len(arrs):
    a = []
    for arr in arrs:
        a.append(len(arr))
    return a


def setPic(pic: QLabel):
    pic.setStyleSheet('QLabel {background-color:#bde7cb;border-radius:10px}')


def track(path, xloc, yloc):
    cap = cv2.VideoCapture(path)
    # tracker = cv2.TrackerKCF_create()
    # tracker = cv2.legacy_TrackerBoosting.create()
    tracker = cv2.TrackerCSRT_create()
    ret, frame = cap.read()
    # messagebox.showinfo("提示", "请框选追踪物体")
    bbox = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)
    tracker.init(frame, bbox)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("帧率：", fps)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("总帧数：", frame_count)
    global video_duration
    video_duration = frame_count / fps
    t = video_duration
    height = frame.shape[0]
    print("xloc,yloc", xloc[0], xloc[1])
    arr_x = []
    arr_y = []
    success_times = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 使用KCF追踪器来追踪物体
        success, bbox = tracker.update(frame)
        # time.sleep(1)
        if success:
            # 如果成功追踪，绘制边界框
            (x, y, w, h) = [int(i) for i in bbox]
            # arr.append([(x - origin[0]) * scaling_x, (y - origin[1]) * scaling_y])
            arr_x.append(x + w/2)
            arr_y.append(height - y - h/2)
            cv2.line(
                frame,
                (xloc[0][0], height - xloc[0][1]),
                (xloc[1][0], height - xloc[1][1]),
                (0,255,  0),
                2,
            )
            cv2.line(
                frame,
                (yloc[0][0], height - yloc[0][1]),
                (yloc[1][0], height - yloc[1][1]),
                (0, 255, 0),
                2,
            )
            current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 当前帧数
            success_times.append(current_frame)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        img_scaled = cv2.resize(
            frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA
        )
        cv2.imshow("Tracking", img_scaled)
        if cv2.waitKey(1) & 0xFF == 27:  # 按Esc键退出循环
            break

    cap.release()
    cv2.destroyAllWindows()
    print("追踪完成")
    print(get_len((arr_x, arr_y)))
    print(success_times)
    success_timestamps = [(frame_num / fps) for frame_num in success_times]
    return arr_x, arr_y, success_timestamps


def pil2pixmap(pil_image):
    image_data = pil_image.tobytes("raw", "RGBA")
    image_format = QImage.Format_RGBA8888
    image = QImage(image_data, pil_image.width, pil_image.height, image_format)
    pixmap = QPixmap.fromImage(image)
    return pixmap


def cv2pix(pic):
    cv_image = pic

    # 将BGR图像转换为RGB图像
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    # 将OpenCV图像转换为QImage
    height, width, channels = cv_image.shape
    bytes_per_line = channels * width
    q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

    # 将QImage转换为QPixmap
    pixmap = QPixmap.fromImage(q_image)
    return pixmap


def get_frame(path):
    path_video = path
    print(path)
    # 打开视频文件
    video = cv2.VideoCapture(path_video)
    # 检查视频是否成功打开
    if not video.isOpened():
        print("Error: Could not open video.")
        exit()
    # 读取第一帧
    ret, frame = video.read()
    # 检查是否成功读取帧
    if not ret:
        print("Error: Could not read frame.")
        exit()
    # 释放视频对象
    video.release()
    return frame


# get_location()

def array_prc(arr1, arr2):
    arr = []
    if len(arr1) != len(arr2):
        return 0
    for i in range(0, len(arr1)):
        arr.append([arr1[i], arr2[i]])
    print("arr长度为", len(arr))
    return arr


def get_line(loc):
    if loc[1][0] != loc[0][0]:
        k = (loc[1][1] - loc[0][1]) / (loc[1][0] - loc[0][0])
        b = loc[1][1] - k * loc[1][0]
        return k, -1, b
    else:
        print("竖直线")
        return -1, 0, loc[1][0]


def get_dis(point, a, b, c):
    d = (a * point[0] + point[1] * b + c) / math.sqrt(a * a + b * b)
    return d


def fix_rate(rate, a, b):
    if b == 0:
        return rate
    else:
        return rate / math.cos(math.atan(-a / b))


def get_rate(real_dis, pic_dis):
    return real_dis / pic_dis


def get_dis_d(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def handle_output(video_duration, arr_x, arr_y):
    f = xlwt.Workbook('encoding = utf-8')
    sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)
    x = np.linspace(0, video_duration, len(arr_y))
    sheet1.write(0, 0, "time")
    sheet1.write(0, 1, "x")
    sheet1.write(0, 2, "y")
    for i in range(len(x)):
        sheet1.write(i + 1, 0, x[i])
        sheet1.write(i + 1, 1, arr_x[i])
        sheet1.write(i + 1, 2, arr_y[i])

    f.save('data.xls')
