from cal_tools import *
import multiprocessing
import t2


class MainWindow(QMainWindow):
    filepath1 = ''
    frame0 = None
    sr_x = 1
    sr_y = 1
    x_loc = []
    y_loc = []
    origin_ax, origin_ay = [], []
    array_x = []
    array_y = []
    array_x1 = []
    array_y1 = []
    t = 0
    px = 0
    py = 0

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        font = QFont()
        font.setPointSize(18)

        o = self.ui
        self.ui.pushButton_7.clicked.connect(lambda :print("asd"))
        setButs((self.ui.pushButton_2,self.ui.pushButton_3,self.ui.pushButton_4,self.ui.pushButton_5,self.ui.pushButton_6,self.ui.pushButton_7))
        setPic(self.ui.label_2)
        setPic(self.ui.label_3)

        self.ui.widget.setStyleSheet("background-color: #eecac1;;border-radius:10px")
        self.ui.widget_2.setStyleSheet("background-color: #eecac1;;border-radius:10px")
        self.ui.lineEdit.setText("100-100")
        self.ui.centralwidget.setStyleSheet("background-color: #f8f9fb")
        self.ui.lineEdit.setStyleSheet("QLineEdit { background-color: #9bc2df; border-radius: 5px; }")
        self.ui.pushButton_7.clicked.connect(self.getfile)
        self.ui.pushButton_2.clicked.connect(self.iii)
        self.ui.pushButton_3.clicked.connect(lambda id: self.handle_draw(1))
        self.ui.pushButton_4.clicked.connect(lambda id: self.handle_draw(2))
        self.ui.pushButton_5.clicked.connect(lambda id: self.handle_draw(3))
        self.ui.pushButton_6.clicked.connect(self.handle_output)
        o.label_2.setText("待显示...")
        o.label_3.setText("待显示...")
        o.pushButton_7.setText("选择文件")
        o.pushButton_2.setText("处理")
        o.pushButton_6.setText("输出")
        o.label_5.setText("长度")
        o.label_4.setText("绘制")
        o.label_4.setAlignment(Qt.AlignCenter)
        o.label_5.setAlignment(Qt.AlignCenter)
        o.label_3.setAlignment(Qt.AlignCenter)
        o.label_2.setAlignment(Qt.AlignCenter)
        o.label_3.setFont(font)
        o.label_2.setFont(font)

    def process(self,p):
        log("********************************************************************")

        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print("self.py",self.py)
                print(f"Mouse clicked at ({2*x}, {self.py - 2*y})")
                log(f"鼠标点击位置： ({2*x}, {self.py - 2*y})")
                global loc_temp
                loc_temp = (2 * x, self.py - 2 * y)
                cv2.destroyAllWindows()

        self.x_loc = []
        self.y_loc = []
        self.origin_ax = []
        self.origin_ay = []
        self.array_x = []
        self.array_y = []
        self.array_x1 = []
        self.array_y1 = []
        arr_loc = []

        if self.ui.lineEdit != "":
            real_x = int(self.ui.lineEdit.text().split("-")[0])
            real_y = int(self.ui.lineEdit.text().split("-")[1])
        printt(real_x+real_y)

        self.notice(1)

        for i in range(2):
            # 创建窗口
            cv2.namedWindow("Image")
            # 设置鼠标回调函数
            cv2.setMouseCallback("Image", mouse_callback)
            img_scaled = cv2.resize(self.frame0, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)    
            cv2.imshow("Image", img_scaled)
            cv2.waitKey(0)

            self.x_loc.append(loc_temp)
            print("self.x_loc.append(loc_temp)")
        try:
            real_x = int(self.input(1))
            print('real_x',real_x)
            self.ui.lineEdit.setText(str(real_x)+"-"+str(real_y))
        except:
            print("未赋值")

        log(f"真实的x轴长度为{real_x}cm")

        self.notice(2)
        for i in range(2):
            # t2.go()
            # 创建窗口
            cv2.namedWindow("Image")
            # 设置鼠标回调函数
            cv2.setMouseCallback("Image", mouse_callback)
            img_scaled = cv2.resize(self.frame0, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) 
            cv2.imshow("Image", img_scaled)
            cv2.waitKey(0)

            self.y_loc.append(loc_temp)
            print("self.y_loc.append(loc_temp)")
        try:
            real_y = int(self.input(2))
            print('real_y',real_y)
            self.ui.lineEdit.setText(str(real_x)+"-"+str(real_y))
        except:
            print("未赋值")
        log(f"真实的y轴长度为{real_y}cm")
        self.notice(3)

        print(get_len((self.x_loc,self.y_loc)),self.x_loc, self.y_loc)

        ax, bx, cx = get_line(self.x_loc)
        print(ax, bx, cx)
        log(f"x轴直线方程为：{ax}x+{bx}y+{cx}=0")

        ay, by, cy = get_line(self.y_loc)
        log(f"y轴直线方程为：{ay}x+{by}y+{cy}=0")
        print(ay, by, cy)

        self.origin_ax, self.origin_ay,self.t = track(self.filepath1, self.x_loc, self.y_loc)
        # printt(self.x_loc,self.y_loc)

        # for i in len(data_o):
        #     data_o[i][0],data_o[i][1],data_o[i][2] = track(self.filepath1, self.x_loc, self.y_loc)
        #     for j in range(len(data_o[i][0])):
        #         data_f[i][0].append(get_dis([data_o[i][0],data_o[i][1]], ax, bx, cx))
        #         data_f[i][1].append(get_dis([data_o[i][0],data_o[i][1]], ay, by, cy))
                
        p.terminate()

        printt("获取数据"+str(get_len((self.origin_ax,self.origin_ax))))
        print(get_len((self.origin_ax,self.origin_ax)))  # 720

        arr_loc = array_prc(self.origin_ax, self.origin_ay)  #给出基于像素的坐标
        # log(f"物体在视频中的坐标为：{arr_loc}")

        for i in range(0, len(arr_loc)):
            dx = get_dis(arr_loc[i], ax, bx, cx)    #与x的距离
            dy = get_dis(arr_loc[i], ay, by, cy)    #与y的距离
            self.array_x1.append(dx)
            self.array_y1.append(dy)

        sr_x = get_rate(real_x, get_dis_d(self.x_loc[0], self.x_loc[1]))
        sr_y = get_rate(real_y, get_dis_d(self.y_loc[0], self.y_loc[1]))
        log(f"x轴分辨率为{sr_x}cm/像素，y轴分辨率为{sr_y}cm/像素")
        print("rate0",sr_x,sr_y)

        self.array_x = [x * sr_y for x in self.array_x1]
        self.array_y = [x * sr_x for x in self.array_y1]

        # x1,y1,t1 = track(self.filepath1, self.x_loc, self.y_loc)
        # x2,y2,t2 = track(self.filepath1, self.x_loc, self.y_loc)
        # x3,y3,t3 = track(self.filepath1, self.x_loc, self.y_loc)
        # al1 = array_prc(x1,y1)
        # al2 = array_prc(x2,y2)
        # al3 = array_prc(x3,y3)

        self.handle_draw(3)
        printt("213123123")
        print(self.x_loc, self.y_loc, ax, bx, cx, ay, by, cy, real_x, real_y)

    def iii(self):

        p1 = multiprocessing.Process(target=t2.create_window)
        print("多进程")
        p1.start()
        self.process(p1)

    def handle_draw(self, id):
        # x = np.linspace(0, self.t, len(self.array_y))
        x = self.t
        if id == 3:
            # plt.plot(x, self.array_x)
            fig = Figure()
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            print(get_len((x,self.array_x)))
            ax.plot(x, self.array_x)
            # plt.show()
            buf = io.BytesIO()
            # showimg(self.ui.label_3,buf)
            fig.savefig(buf, format='png')
            buf.seek(0)  # 移动到流的开始处

            # 从BytesIO对象创建QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue(), 'PNG')
            self.ui.label_3.setStyleSheet("")
            self.ui.label_3.setPixmap(pixmap.scaled(
                    self.ui.label_3.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                ))
            self.ui.label_3.setAlignment(Qt.AlignCenter)
            print("绘制yt")
        elif id == 2:
            # plt.plot(x, self.array_y)
            # plt.show()
            fig = Figure()
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            ax.plot(x, self.array_y)
            # plt.show()
            buf = io.BytesIO()
            # showimg(self.ui.label_3,buf)
            fig.savefig(buf, format='png')
            buf.seek(0)  # 移动到流的开始处

            # 从BytesIO对象创建QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue(), 'PNG')
            self.ui.label_3.setStyleSheet("")
            self.ui.label_3.setPixmap(pixmap.scaled(
                    self.ui.label_3.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                ))
            self.ui.label_3.setAlignment(Qt.AlignCenter)
            print("绘制xt")
        elif id == 1:
            # plt.plot(self.array_x, self.array_y)
            # plt.show()
            fig = Figure()
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            ax.plot(self.array_y, self.array_x)
            # plt.show()
            buf = io.BytesIO()
            # showimg(self.ui.label_3,buf)
            fig.savefig(buf, format='png')
            buf.seek(0)  # 移动到流的开始处

            # 从BytesIO对象创建QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue(), 'PNG')
            self.ui.label_3.setStyleSheet("")
            self.ui.label_3.setPixmap(pixmap.scaled(
                    self.ui.label_3.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                ))
            self.ui.label_3.setAlignment(Qt.AlignCenter)
            print("绘制xy")

    def handle_output(self):
        # t2.stop()
        f = xlwt.Workbook('encoding = utf-8')
        sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)
        x = self.t
        sheet1.write(0, 0, "time")
        sheet1.write(0, 1, "x")
        sheet1.write(0, 2, "y")
        for i in range(len(x)):
            sheet1.write(i + 1, 0, x[i])
            sheet1.write(i + 1, 1, self.array_y[i])
            sheet1.write(i + 1, 2, self.array_x[i])

        f.save('data.xls')
        messagebox.showinfo("提示", "导出成功(SUCCESS)")

    def getfile(self):
        self.filepath1 = getfilepath()
        print(self.filepath1)
        if(self.filepath1 != ''):
            print("获取文件成功")

            self.frame0 = get_frame(self.filepath1)
            pixmap = cv2pix(self.frame0)
            print("分辨率",pixmap.height(),pixmap.width())
            self.px = pixmap.width()
            self.py = pixmap.height()
            self.ui.label.setText(self.filepath1)
            self.ui.label_2.setStyleSheet("")
            self.ui.label_2.setPixmap(
                pixmap.scaled(
                    self.ui.label_2.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                )
            )

    def notice(self,id=0):
        root = tk.Tk()
        root.withdraw()
        if id == 1:
            messagebox.showinfo("提示", "请先后点击x轴参照物的两端")

        if id == 2:
            messagebox.showinfo("提示", "请先后点击y轴参照物的两端")

        if id == 3:
            messagebox.showinfo("提示", "请使用鼠标框选目标物体")

    def input(self,id):
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        if id == 1:
            user_input = simpledialog.askstring(
                title="输入信息", prompt="请输入x轴参照物的长度："
                
            )
            return user_input

        if id == 2:
            user_input = simpledialog.askstring(
                title="输入信息", prompt="请输入y轴参照物的长度："
                
            )
            return user_input


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def run():
    window = MainWindow()
    window.show()
    app.exec()
