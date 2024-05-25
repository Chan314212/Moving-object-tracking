import re
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt
def getfilepath():
    # 初始化一个tkinter窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    a = filedialog.askopenfilename(
        title="选择文件", filetypes=[("所有文件", "*.*")]
    )
    # 完成选择后，销毁窗口
    root.destroy()
    return a


# 路径应根据你的实际文件位置进行修改
file_path = getfilepath()
print(file_path)

# 初始化三个列表以存储系数
coefficients_a = []  # 二次项系数
coefficients_b = []  # 一次项系数
coefficients_c = []  # 常数项系数

# 正则表达式匹配二次方程的系数
pattern = r"([-+]?\d*\.?\d+)\s*X\^2\s*([-+]?\d*\.?\d+)\s*X\s*([-+]?\d*\.?\d+)"
pattern = r"([-+]?\d*\.?\d+)\s*\*\s*X\^2\s*([-+]?\d*\.?\d+)\s*\*\s*X\s*([-+]?\d*\.?\d+)"

pattern = r"([-+]?\d*\.?\d+)\s*X\^2"

try:
    with open(file_path, "r", encoding='gbk') as file:
        for line in file:
            # 使用正则表达式搜索匹配的二次方程系数
            match = re.search(pattern, line)
            if match:
                a = match.group(1)  # 获取匹配到的第一个组，即二次项系数
                coefficients_a.append(float(a))  # 转换为浮点数并添加到列表中
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except Exception as e:
    print(f"读取文件时发生错误：{e}")

# 输出二次项系数
print("二次项系数:", coefficients_a,max(coefficients_a),min(coefficients_a))
print("")
g = [i*16*2/100 for i in coefficients_a]
print(g)
mean = [sum(g)/len(g) for i in range(len(g))]
minus = [(i-j)/j for i,j in zip(g,mean)]
plt.plot(minus)
# plt.plot(mean)
# plt.plot(g)
plt.show()
