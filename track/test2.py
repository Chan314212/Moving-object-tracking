import os
import xlrd
# from cal_tools import *
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
def save_to_desktop_txt(data):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 获取桌面路径
    file_path = os.path.join(desktop_path, "output.txt")  # 指定输出文件路径
    
    # 打开文件，如果文件不存在则创建
    with open(file_path, "a") as file:
        file.write(data + "\n")  # 追加字符串到文件末尾
def getfilepath1():
    # 初始化一个tkinter窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    a = filedialog.askdirectory(title="选择文件夹")
    # 完成选择后，销毁窗口
    root.destroy()
    return a

def read_files_from_folder(folder_path, num_files=5):
    file_count = 0
    data_list = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xls') or file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            try:
                workbook = xlrd.open_workbook(file_path)
                sheet = workbook.sheet_by_index(0)  # 假设数据在第一个表格中，如果不是请修改索引
                column1_data = sheet.col_values(0)  # 假设第一列是需要的数据
                column2_data = sheet.col_values(2)  # 假设第二列是需要的数据
                column1_data = column1_data[1:]
                column2_data = column2_data[1:]

                data_list.append((column1_data, column2_data))
                file_count += 1
                if file_count >= num_files:
                    break
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")

    return data_list

# 提示用户输入文件夹路径
folder_path = getfilepath1()
# 读取文件夹中的数据
data = read_files_from_folder(folder_path)
print(data)
save_to_desktop_txt(folder_path)
for i in range(5):
    y = data[i][1]
    t = data[i][0]
    coefficients = np.polyfit(t, y, 2)
    def f(x):
        return coefficients[0]*x**2+coefficients[1]*x+coefficients[2]
    temp = np.linspace(t[0],t[-1],100)
    tempy = [f(j) for j in temp]
    print(i)
    print(f"{coefficients[0]:.2f} X^2 + {2+coefficients[1]:.2f} X + {coefficients[2]:.2f}")
    save_to_desktop_txt(f"{coefficients[0]:.2f} X^2 + {2+coefficients[1]:.2f} X + {coefficients[2]:.2f}")
    plt.plot(t,y,"o",label = f"第{i+1}次")
    plt.plot(temp,tempy,label = f"第{i}次拟合")
    plt.ylabel("Y/cm")
    plt.xlabel("T/s")
plt.legend()
plt.savefig(folder_path+"/"+folder_path.split("/")[-1]+".png")
print(folder_path+"/"+folder_path.split("/")[-1]+".png")

plt.show()
