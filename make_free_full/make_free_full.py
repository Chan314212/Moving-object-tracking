import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
def getfilepath():
    # 初始化一个tkinter窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    a = filedialog.askopenfilename(
        title="选择文件", filetypes=[("文件", "*.png"), ("所有文件", "*.*")]
    )
    # 完成选择后，销毁窗口
    root.destroy()
    return a


# 读取背景图片和小点图片
background = cv2.imread(getfilepath())
cv2.imshow("background", background)
dot = cv2.imread(getfilepath(), cv2.IMREAD_UNCHANGED)  # 保持透明度

# 获取图片尺寸
bg_height, bg_width, _ = background.shape
dot_height, dot_width, _ = dot.shape

# 视频参数
fps = 120
duration = 5  # 秒
total_frames = fps * duration

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter("free_fall.mp4", fourcc, fps, (bg_width, bg_height))

# 自由落体运动参数
initial_y = 100  # 小点初始位置
gravity = 3 # 重力加速度，单位：m/s^2
pixel_per_meter = 800  # 将实际物理距离转为像素

for frame_num in range(total_frames):
    # 计算时间
    t = frame_num / fps

    # 计算小点的 y 坐标 (s = 1/2 * g * t^2)
    y = int(initial_y + 0.5 * gravity * t * t * pixel_per_meter)

    # 如果 y 坐标超出背景图片的高度，则停止移动
    if y + dot_height > 900:
        y = 900

    # 创建当前帧
    frame = background.copy()

    # 计算小点的 x 坐标，使其居中
    # x = (bg_width - dot_width) // 2
    x = 900

    # 将小点放置在当前帧中
    for i in range(dot_height):
        for j in range(dot_width):
            if dot[i, j, 3] > 0:  # 检查 alpha 通道（透明度）
                frame[y + i, x + j] = dot[i, j, :3]  # 复制 RGB 通道

    # 写入当前帧
    video_writer.write(frame)

# 释放视频写入对象
video_writer.release()

print("视频已生成并保存为 free_fall.mp4")
