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
print(path)


path2 = getfilepath()
workbook2 = xlrd.open_workbook(path2)
worksheet2 = workbook2.sheet_by_index(0)
column1_data2 = []
column2_data2 = []

# 假设您要读取第一列（索引为0）和第二列（索引为1）的数据
for row_idx in range(1,worksheet.nrows):
    # 获取当前行对应两列的单元格值
    cell_value1 = worksheet.cell(row_idx, 0).value
    cell_value2 = worksheet.cell(row_idx, 2).value

    # 将单元格值添加到对应的列表中
    column1_data.append(cell_value1)
    column2_data.append(cell_value2)

# 假设您要读取第一列（索引为0）和第二列（索引为1）的数据
for row_idx in range(1,worksheet2.nrows):
    # 获取当前行对应两列的单元格值
    cell_value12 = worksheet2.cell(row_idx, 0).value
    cell_value22 = worksheet2.cell(row_idx, 2).value

    # 将单元格值添加到对应的列表中
    column1_data2.append(cell_value12)
    column2_data2.append(cell_value22)

coefficients = np.polyfit(column1_data, column2_data, 2)
coefficients2 = np.polyfit(column1_data2, column2_data2, 2)

print(f"{coefficients[0]:.2f}X^2 + {2+coefficients[1]:.2f}X + {coefficients[2]:.2f}")
print(f"{coefficients2[0]:.2f}X^2 + {2+coefficients2[1]:.2f}X + {coefficients2[2]:.2f}")
def f(x):
    return coefficients[0]*x**2+coefficients[1]*x+coefficients[2]

def f2(x):
    return coefficients2[0]*x**2+coefficients2[1]*x+coefficients2[2]

data_f = [f(i) for i in column1_data]
data_f2 = [f2(i) for i in column1_data2]
#
plt.plot(column1_data,column2_data,'o',label='data1')
plt.plot(column1_data2,column2_data2,'o',label='data2')
plt.plot(column1_data,data_f,'-',label='fit1')
plt.plot(column1_data2,data_f2,'-',label='fit2')
plt.xlabel('T/s')
plt.ylabel('H/cm')
plt.legend()
plt.show()
