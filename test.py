from cal_tools import *

base = [] #loc,real,array
base = "[(156,494),(738,496)] [(748,654),(740,48)] 0.003436426116838488 -1 493.4639175257732 75.75 -1 -56007.0 100 100".split()
x_loc = eval(base[0])
y_loc = eval(base[1])
ax, bx, cx = eval(base[2]),eval(base[3]),eval(base[4])
ay, by, cy = eval(base[5]),eval(base[6]),eval(base[7])
real_x = eval(base[8])
real_y = eval(base[9])
array_x1 = []
array_y1 = []
t = []

# print(base)
# print(eval(base[0]))

filepath1 = getfilepath()

def handle_output(arrayx,arrayy,x,name):
        f = xlwt.Workbook('encoding = utf-8')
        sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet1.write(0, 0, "time")
        sheet1.write(0, 1, "x")
        sheet1.write(0, 2, "y")
        for i in range(len(x)):
            sheet1.write(i + 1, 0, x[i])
            sheet1.write(i + 1, 1, arrayy[i])
            sheet1.write(i + 1, 2, arrayx[i])

        f.save(name)
        messagebox.showinfo("提示", "导出成功(SUCCESS)")

for j in range(5):
    array_x1 = []
    array_y1 = []
    origin_ax, origin_ay,t = track(filepath1, x_loc, y_loc)

    arr_loc = array_prc(origin_ax, origin_ay)  #给出基于像素的坐标
        # log(f"物体在视频中的坐标为：{arr_loc}")

    for i in range(0, len(arr_loc)):
        dx = get_dis(arr_loc[i], ax, bx, cx)    #与x的距离
        dy = get_dis(arr_loc[i], ay, by, cy)    #与y的距离
        array_x1.append(dx)
        array_y1.append(dy)

    sr_x = get_rate(real_x, get_dis_d(x_loc[0], x_loc[1]))
    sr_y = get_rate(real_y, get_dis_d(y_loc[0], y_loc[1]))
    log(f"x轴分辨率为{sr_x}cm/像素，y轴分辨率为{sr_y}cm/像素")
    print("rate0",sr_x,sr_y)

    array_x = [x * sr_y for x in array_x1]
    array_y = [x * sr_x for x in array_y1]
    handle_output(array_x,array_y,t,f"data{j}.xls")
