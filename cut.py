from cut_tools import *


# test()

class MainWindow(QMainWindow):
    video_du = 0  # 视频时长
    time_1 = 0
    time_2 = 0
    filepath = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        o = self.ui
        setButs((o.pushButton, o.pushButton_2, o.pushButton_3))
        o.centralwidget.setStyleSheet("background-color: #f8f9fb")
        setPic(o.label)
        o.widget.setStyleSheet("background-color: #eecac1;;border-radius:10px")
        o.widget_2.setStyleSheet("background-color: #eecac1;;border-radius:10px")
        o.horizontalSlider.valueChanged.connect(self.test)
        o.horizontalSlider_2.valueChanged.connect(self.test)
        o.horizontalSlider.sliderReleased.connect(self.setpic)
        o.horizontalSlider_2.sliderReleased.connect(self.setpic)
        o.pushButton.clicked.connect(self.load1)
        o.pushButton_2.clicked.connect(self.load2)
        o.pushButton_3.clicked.connect(self.load3)

    def updateRange(self):
        o = self.ui
        # 确保slider1的值总是小于等于slider2的值
        if (
                self.sender() == o.horizontalSlider
                and
                o.horizontalSlider.value() > o.horizontalSlider_2.value()
        ):
            o.horizontalSlider_2.setValue(o.horizontalSlider.value())

        elif (
                self.sender() == o.horizontalSlider_2
                and
                o.horizontalSlider_2.value() < o.horizontalSlider.value()
        ):
            o.horizontalSlider.setValue(o.horizontalSlider_2.value())

    def test(self):
        o = self.ui
        self.updateRange()
        if self.sender() == o.horizontalSlider:
            self.time_1 = o.horizontalSlider.value()/100
            print(self.time_1)
        if self.sender() == o.horizontalSlider_2:
            self.time_2 = o.horizontalSlider_2.value()/100
            print(self.time_2)
    def setpic(self):
        o = self.ui
        if self.sender() == o.horizontalSlider:
            o.label.setPixmap(
                f2pix(get_frame(self.filepath, self.time_1)).scaled(
                    o.label.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                )
            )
        if self.sender() == o.horizontalSlider_2:
            o.label.setPixmap(
                f2pix(get_frame(self.filepath, self.time_2)).scaled(
                    o.label.size(),
                    aspectMode=Qt.KeepAspectRatio,
                    mode=Qt.SmoothTransformation,
                )
            )

    def load1(self):
        o = self.ui
        self.filepath = load0(o.label_4, o.label)
        o.label.setAlignment(Qt.AlignCenter)
        print('self.filepath:',self.filepath)
        self.video_du = get_video_duration(self.filepath)
        print('self.video_du:',self.video_du)
        o.label_3.setText(str(self.video_du))
        o.horizontalSlider.setMaximum(self.video_du*100)
        o.horizontalSlider_2.setMaximum(self.video_du*100)
        o.horizontalSlider.setValue(0)
        o.horizontalSlider_2.setValue(self.video_du*100)

    def load2(self):
        o = self.ui
        appdata_dir = os.path.expandvars("%APPDATA%\\CAPA")
        if not os.path.exists(appdata_dir):
            os.mkdir(appdata_dir)
        otpt = cut_video_by_time(self.filepath, self.time_1, self.time_2,appdata_dir)
        # try : subprocess.call(["start", otpt], shell=True)
        try:
            os.startfile(otpt)
        except:
            print("打开失败")

    def load3(self):
        appdata_dir = os.path.expandvars("%APPDATA%\\CAPA")
        if not os.path.exists(appdata_dir):
            os.mkdir(appdata_dir)
        otpt = cut_video_by_time(self.filepath, self.time_1, self.time_2,appdata_dir)
        c = filedialog.asksaveasfilename(initialfile="video",title="video",defaultextension=".mp4",filetypes=[("Video Files", "*.mp4"), ("All Files", "*.*")])
        print(c)
        if c:shutil.copy2(otpt,c)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

def run():
    # app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
