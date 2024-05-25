import tkinter as tk
from PIL import ImageGrab, Image, ImageTk
import pyautogui
import threading


def create_window():
    WINDOW_SIZE = 400
    ZOOM_FACTOR = 3
    root1 = tk.Tk()
    root1.overrideredirect(True)  # 无边框窗口
    root1.attributes("-topmost", True)  # 窗口保持在最前面
    root1.bind("<Escape>", lambda event: root1.destroy())

    # 获取屏幕宽度和高度
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # 计算窗口右上角的位置
    x_position = screen_width - WINDOW_SIZE
    y_position = 0  # 屏幕顶端

    # 设置窗口位置
    root1.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+{x_position}+{y_position}")

    # 创建画布来显示放大图像
    canvas = tk.Canvas(root1, width=WINDOW_SIZE, height=WINDOW_SIZE)
    canvas.pack()

    def update_image():

        x, y = pyautogui.position()

        # 捕获鼠标附近的屏幕区域
        bbox = (
            x - WINDOW_SIZE // (2 * ZOOM_FACTOR),
            y - WINDOW_SIZE // (2 * ZOOM_FACTOR),
            x + WINDOW_SIZE // (2 * ZOOM_FACTOR),
            y + WINDOW_SIZE // (2 * ZOOM_FACTOR),
        )
        screenshot = ImageGrab.grab(bbox)

        # 放大图像
        zoomed_screenshot = screenshot.resize((WINDOW_SIZE, WINDOW_SIZE), Image.LANCZOS)

        # 更新画布上的图像
        tk_image = ImageTk.PhotoImage(zoomed_screenshot)
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        canvas.image = tk_image  # 防止tk_image被垃圾回收

        # 在窗口中间绘制红点
        center_x = WINDOW_SIZE // 2
        center_y = WINDOW_SIZE // 2
        red_dot_radius = 5  # 调整红点大小
        canvas.delete("red_dot")  # 删除之前绘制的红点（如果有）
        canvas.create_oval(
            center_x - red_dot_radius,
            center_y - red_dot_radius,
            center_x + red_dot_radius,
            center_y + red_dot_radius,
            fill="red",
            outline="red",
            tags="red_dot",
        )

        root1.after(8, update_image)  # 每100ms更新一次图像

    update_image()
    root1.mainloop()


if __name__ == "__main__":
    create_window()
