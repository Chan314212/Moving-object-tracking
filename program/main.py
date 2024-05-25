from tools import *
import cal,cut
import t2


class MainWindow(QMainWindow):
    output = ""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        o = self.ui
        o.centralwidget.setStyleSheet("background-color: #f8f9fb")
        o.widget_3.setStyleSheet("background-color: #eecac1;;border-radius:10px")
        o.widget.setStyleSheet("background-color: #bde7cb;;border-radius:10px")
        o.widget_2.setStyleSheet("background-color: #bde7cb;;border-radius:10px")
        setButs((o.pushButton,o.pushButton_2))
        o.pushButton.clicked.connect(self.cut)
        o.pushButton_2.clicked.connect(self.cal)

    def cut(self):
        # subprocess.run(["python", "cut/main.py"])
        cut.run()
        # t2.go()


    def cal(self):
        # subprocess.run(["python", "cal/face.py"])
        cal.run()
        # t2.stop()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
