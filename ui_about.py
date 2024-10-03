# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutsrkceg.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 280)
        Form.setMinimumSize(QSize(550, 280))
        Form.setMaximumSize(QSize(550, 280))
        icon = QIcon()
        icon.addFile(u"res/about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 261, 251))
        self.label.setPixmap(QPixmap(u"res/app.png"))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 40, 191, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 80, 271, 51))
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 250, 281, 21))
        font1 = QFont()
        font1.setPointSize(7)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 130, 151, 41))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 160, 151, 111))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0438\u0432\u0443\u043b\u044c\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u043c \u0425\u0418\u0418\u041a \u0421\u0438\u0431\u0413\u0423\u0422\u0418 \u0433\u0440\u0443\u043f\u043f\u044b \u0418\u0421\u041f-330 \u0422\u0443\u0440\u0447\u0430\u043d\u043e\u0432\u044b\u043c \u0420\u043e\u0434\u0438\u043e\u043d\u043e\u043c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0435 \u0434\u043b\u044f \u0430\u0434\u0435\u043a\u0432\u0430\u0442\u043d\u043e\u0433\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"2023 \u0433. ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f - v0.2", None))
    # retranslateUi

