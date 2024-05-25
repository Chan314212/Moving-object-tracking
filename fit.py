import numpy as np
import xlrd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def getfilepath():
    # 初始化一个tkinter窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()
    a = filedialog.askopenfilename(
        title="选择文件", filetypes=[("文件", "*.xls"), ("所有文件", "*.*")]
    )
    # 完成选择后，销毁窗口
    root.destroy()
    return a


path = getfilepath()
workbook = xlrd.open_workbook(path)
worksheet = workbook.sheet_by_index(0)
column1_data = []
column2_data = []

# 假设您要读取第一列（索引为0）和第二列（索引为1）的数据
for row_idx in range(1,worksheet.nrows):
    # 获取当前行对应两列的单元格值
    cell_value1 = worksheet.cell(row_idx, 0).value
    cell_value2 = worksheet.cell(row_idx, 2).value

    # 将单元格值添加到对应的列表中
    column1_data.append(cell_value1)
    column2_data.append(cell_value2)


times = int(input("次数"))

coefficients = np.polyfit(column1_data, column2_data, times)

print(coefficients)

def get_y(x):
    return np.polyval(coefficients, x)

y_fit = get_y(column1_data)
plt.plot(column1_data, y_fit, 'r-', label='Fitted Curve')
plt.plot(column1_data, column2_data, 'o', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
# print("\n",coefficients[0],"\n")

# x = int(input("请输入倍率：\n"))
# dis = coefficients[0]*x*x*2

# print(f"\n误差值为{(980-dis)/980}\n")
# input()
