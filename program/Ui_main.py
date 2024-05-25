# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(558, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 1, 16, 24)
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(240, 160))
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)

        self.verticalLayout.addWidget(self.pushButton)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(240, 160))
        self.pushButton_2.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u89c6\u9891\u7269\u4f53\u8ffd\u8e2a\u7a0b\u5e8f</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5207\u5272", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u70b9\u51fb\u6b64\u6309\u94ae\u4f1a\u8fdb\u884c\u89c6\u9891\u65f6\u957f\u88c1\u526a</p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u70b9\u51fb\u6b64\u6309\u94ae\u4f1a\u5bf9\u89c6\u9891\u4e2d\u7269\u4f53\u8fdb\u884c\u8ffd\u8e2a</p></body></html>", None))
    # retranslateUi

