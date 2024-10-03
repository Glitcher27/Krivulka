# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KrivQoWggd.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 602)
        icon = QIcon()
        icon.addFile(u"res/app.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.forget = QAction(MainWindow)
        self.forget.setObjectName(u"forget")
        self.clear = QAction(MainWindow)
        self.clear.setObjectName(u"clear")
        self.exit = QAction(MainWindow)
        self.exit.setObjectName(u"exit")
        self.NONE = QAction(MainWindow)
        self.NONE.setObjectName(u"NONE")
        self.howto = QAction(MainWindow)
        self.howto.setObjectName(u"howto")
        self.license = QAction(MainWindow)
        self.license.setObjectName(u"license")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.code = QAction(MainWindow)
        self.code.setObjectName(u"code")
        self.docs = QAction(MainWindow)
        self.docs.setObjectName(u"docs")
        self.task = QAction(MainWindow)
        self.task.setObjectName(u"task")
        self.installators = QAction(MainWindow)
        self.installators.setObjectName(u"installators")
        self.docs_ac = QAction(MainWindow)
        self.docs_ac.setObjectName(u"docs_ac")
        self.code_ac = QAction(MainWindow)
        self.code_ac.setObjectName(u"code_ac")
        self.installers = QAction(MainWindow)
        self.installers.setObjectName(u"installers")
        self.task_ac = QAction(MainWindow)
        self.task_ac.setObjectName(u"task_ac")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pager = QStackedWidget(self.frame)
        self.pager.setObjectName(u"pager")
        self.pager.setMinimumSize(QSize(500, 275))
        self.solo = QWidget()
        self.solo.setObjectName(u"solo")
        self.horizontalLayout_2 = QHBoxLayout(self.solo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output = QWidget(self.solo)
        self.output.setObjectName(u"output")

        self.horizontalLayout_2.addWidget(self.output)

        self.pager.addWidget(self.solo)
        self.duo = QWidget()
        self.duo.setObjectName(u"duo")
        self.horizontalLayout_3 = QHBoxLayout(self.duo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_l = QWidget(self.duo)
        self.output_l.setObjectName(u"output_l")

        self.horizontalLayout_3.addWidget(self.output_l)

        self.output_r = QWidget(self.duo)
        self.output_r.setObjectName(u"output_r")

        self.horizontalLayout_3.addWidget(self.output_r)

        self.pager.addWidget(self.duo)

        self.verticalLayout.addWidget(self.pager)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 250))
        self.widget.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f1 = QFrame(self.widget)
        self.f1.setObjectName(u"f1")
        self.f1.setMaximumSize(QSize(16777215, 50))
        self.f1.setFrameShape(QFrame.Shape.StyledPanel)
        self.f1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.f1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.f1)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.f1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.draw = QPushButton(self.f1)
        self.draw.setObjectName(u"draw")
        self.draw.setMinimumSize(QSize(78, 0))
        self.draw.setMaximumSize(QSize(78, 16777215))

        self.horizontalLayout_4.addWidget(self.draw)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.f1)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.f6 = QFrame(self.frame_3)
        self.f6.setObjectName(u"f6")
        self.f6.setFrameShape(QFrame.Shape.StyledPanel)
        self.f6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.f6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.split_option = QCheckBox(self.f6)
        self.split_option.setObjectName(u"split_option")

        self.horizontalLayout_9.addWidget(self.split_option)


        self.gridLayout.addWidget(self.f6, 1, 3, 1, 1)

        self.f3 = QFrame(self.frame_3)
        self.f3.setObjectName(u"f3")
        self.f3.setFrameShape(QFrame.Shape.StyledPanel)
        self.f3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.f3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.f3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.input_b = QLineEdit(self.f3)
        self.input_b.setObjectName(u"input_b")
        font1 = QFont()
        font1.setFamilies([u"Cascadia Code"])
        self.input_b.setFont(font1)

        self.horizontalLayout_6.addWidget(self.input_b)


        self.gridLayout.addWidget(self.f3, 1, 1, 1, 1)

        self.block_y = QFrame(self.frame_3)
        self.block_y.setObjectName(u"block_y")
        self.block_y.setEnabled(False)
        self.block_y.setFrameShape(QFrame.Shape.StyledPanel)
        self.block_y.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.block_y)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.block_y)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.input_y = QLineEdit(self.block_y)
        self.input_y.setObjectName(u"input_y")
        self.input_y.setFont(font1)

        self.horizontalLayout_10.addWidget(self.input_y)


        self.gridLayout.addWidget(self.block_y, 2, 3, 1, 1)

        self.f4 = QFrame(self.frame_3)
        self.f4.setObjectName(u"f4")
        self.f4.setFrameShape(QFrame.Shape.StyledPanel)
        self.f4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.f4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.f4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.color = QComboBox(self.f4)
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.setObjectName(u"color")

        self.horizontalLayout_7.addWidget(self.color)

        self.hashtag = QLabel(self.f4)
        self.hashtag.setObjectName(u"hashtag")
        self.hashtag.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.hashtag)

        self.hex = QLineEdit(self.f4)
        self.hex.setObjectName(u"hex")
        self.hex.setEnabled(True)
        self.hex.setFont(font1)
        self.hex.setMaxLength(6)
        self.hex.setFrame(True)

        self.horizontalLayout_7.addWidget(self.hex)


        self.gridLayout.addWidget(self.f4, 2, 1, 1, 1)

        self.f2 = QFrame(self.frame_3)
        self.f2.setObjectName(u"f2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f2.sizePolicy().hasHeightForWidth())
        self.f2.setSizePolicy(sizePolicy)
        self.f2.setMinimumSize(QSize(230, 0))
        self.f2.setMaximumSize(QSize(1677215, 16777215))
        self.f2.setFrameShape(QFrame.Shape.StyledPanel)
        self.f2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.f2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.f2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.input_a = QLineEdit(self.f2)
        self.input_a.setObjectName(u"input_a")
        self.input_a.setFont(font1)

        self.horizontalLayout_5.addWidget(self.input_a)


        self.gridLayout.addWidget(self.f2, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.f5 = QFrame(self.frame_3)
        self.f5.setObjectName(u"f5")
        sizePolicy.setHeightForWidth(self.f5.sizePolicy().hasHeightForWidth())
        self.f5.setSizePolicy(sizePolicy)
        self.f5.setMinimumSize(QSize(230, 0))
        self.f5.setMaximumSize(QSize(1677215, 16777215))
        self.f5.setFrameShape(QFrame.Shape.StyledPanel)
        self.f5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.f5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.f5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.input_x = QLineEdit(self.f5)
        self.input_x.setObjectName(u"input_x")
        self.input_x.setFont(font1)

        self.horizontalLayout_8.addWidget(self.input_x)


        self.gridLayout.addWidget(self.f5, 0, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 576, 33))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.recent = QMenu(self.file)
        self.recent.setObjectName(u"recent")
        self.info = QMenu(self.menubar)
        self.info.setObjectName(u"info")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.info.menuAction())
        self.file.addAction(self.save)
        self.file.addAction(self.forget)
        self.file.addSeparator()
        self.file.addAction(self.recent.menuAction())
        self.file.addAction(self.clear)
        self.file.addSeparator()
        self.file.addAction(self.exit)
        self.recent.addAction(self.NONE)
        self.info.addAction(self.howto)
        self.info.addAction(self.license)
        self.info.addAction(self.about)
        self.info.addSeparator()
        self.info.addAction(self.docs_ac)
        self.info.addAction(self.code_ac)
        self.info.addAction(self.installers)
        self.info.addAction(self.task_ac)

        self.retranslateUi(MainWindow)

        self.pager.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0432\u0443\u043b\u044c\u043a\u0430", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.forget.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.NONE.setText(QCoreApplication.translate("MainWindow", u"[\u043f\u0443\u0441\u0442\u043e]", None))
        self.howto.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.license.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.code.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.docs.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.task.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.installators.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0430\u043b\u043b\u044f\u0442\u043e\u0440\u044b", None))
        self.docs_ac.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.code_ac.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.installers.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a\u0438", None))
        self.task_ac.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0192(\u2179)=ax\u00b2+b", None))
        self.draw.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u0442\u0438\u0442\u044c", None))
        self.split_option.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0440\u0430\u0437\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 B", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u043f\u043e Y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442", None))
        self.color.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u044b\u0439", None))
        self.color.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.color.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.color.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.color.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u0443\u0431\u043e\u0439", None))
        self.color.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u044b\u0439", None))
        self.color.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.color.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))
        self.color.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0439", None))

        self.hashtag.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.hex.setInputMask(QCoreApplication.translate("MainWindow", u"HHHHHH;-", None))
        self.hex.setText(QCoreApplication.translate("MainWindow", u"000000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 A", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0441\u0435\u0447\u0435\u043d\u0438\u0435 \u043f\u043e X", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.recent.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0430\u0432\u043d\u0435\u0435", None))
        self.info.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

