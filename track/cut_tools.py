import os
import shutil
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from moviepy.video.io.VideoFileClip import VideoFileClip
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QStatusBar, QWidget)

from cut_ui import Ui_MainWindow


def test():
    print("im ok")


def getfilepath():
    a = filedialog.askopenfilename(
        title="选择文件", filetypes=[("视频文件", "*.mp4;*.mov"), ("所有文件", "*.*")]
    )
    print(a)
    return a


def load0(lab: QLabel, lab2: QLabel):
    a = getfilepath()
    lab.setText(a)
    # lab2.setPixmap(get_frame(a,0))
    lab2.setPixmap(
        f2pix(get_frame(a, 0)).scaled(
            lab2.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation,
        )
    )
    return a


def setBut(but: QPushButton):
    but.setStyleSheet(
        "QPushButton{font-size: 13pt;background-color: #9bc2df;border-radius:10px;padding:2px 4px;border-style: outset;}"
        "QPushButton:hover{background-color:#b1deff; color: black;}"
        "QPushButton:pressed{background-color:#b1deff;border-style: inset;}"
    )


def setButs(buts):
    for but in buts:
        setBut(but)


def setPic(pic: QLabel):
    pic.setStyleSheet("QLabel {background-color:#bde7cb;border-radius:10px}")


def get_video_duration(video_path):
    """
    返回指定视频文件的时长（以秒为单位）。

    参数：
    video_path (str): 视频文件路径

    返回值：
    float: 视频时长（秒）
    """
    try:
        # 创建VideoFileClip对象
        video = VideoFileClip(video_path)

        # 获取并返回视频时长
        duration = video.duration
        video.close()  # 关闭视频资源（非必须，但在大型项目中建议进行资源管理）

        return duration

    except Exception as e:
        print(f"读取视频时长时发生错误: {e}")
        return None


def cut_video_by_time(
    input_video_path,
    start_time,
    end_time,
    output_dir=os.path.dirname(os.path.abspath(__file__)),
):
    # 解析时间格式
    # start_seconds = parse_start_time_to_seconds(
    #     start_time
    # )  # 自定义函数解析时间字符串到秒数
    if end_time <= start_time:
        return

    start_seconds = start_time

    # 创建剪辑对象
    clip = VideoFileClip(input_video_path)

    # 确保剪切的区间在视频长度范围内
    end_seconds = min(clip.duration, end_time)
    print(
        f"剪切的起始时间：{start_seconds}，剪切的时长：{end_time}，剪切的结束时间：{end_seconds}"
    )

    # 提取剪辑片段
    subclip = clip.subclip(start_seconds, end_seconds)

    # 输出文件名
    output_filename = "temp" + ".mp4"  # 或者自定义有意义的文件名
    output_path = os.path.join(output_dir, output_filename)

    # 输出剪辑片段
    subclip.write_videofile(output_path)
    return output_path


def get_frame(input_video_path, time):
    clip = VideoFileClip(input_video_path)
    frame = clip.get_frame(time)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame


def f2pix(frame):
    h, w, ch = frame.shape
    bytesPerLine = ch * w
    q_image = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)

    # 创建 QPixmap 对象
    pixmap = QPixmap.fromImage(q_image)
    return pixmap
