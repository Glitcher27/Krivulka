# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'licensedjSFru.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(767, 373)
        icon = QIcon()
        icon.addFile(u"res/license_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"res/license_icon.png"))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.license_text = QTextEdit(Form)
        self.license_text.setObjectName(u"license_text")
        self.license_text.setReadOnly(True)

        self.gridLayout.addWidget(self.license_text, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.label.setText("")
        self.license_text.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI Variable Text'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u044b\u0432</span><span style=\" font-size:14pt;"
                        "\">\u044b\u0432\u044b\u0432</span><span style=\" font-size:14pt; font-weight:700;\">\u044b\u0432\u044b\u0432</span><span style=\" font-size:14pt; font-style:italic;\">\u044b\u0432\u044b\u0432</span><span style=\" font-size:14pt; text-decoration: underline;\">\u044b\u0432\u044b\u0432</span><span style=\" font-size:14pt; font-weight:700; font-style:italic; text-decoration: underline;\">\u044b\u0432\u044b\u0432</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u044b\u0432\u044b\u0432</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u044b\u0432\u044b\u0432</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u044b"
                        "\u0432\u044b\u0432\u044b\u0432</span></p>\n"
"<p dir='rtl' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0444\u044b</span></p>\n"
"<p dir='rtl' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; vertical-align:sub;\">\u0444\u044b</span><span style=\" font-size:14pt; vertical-align:super;\">\u0444\u044b</span><span style=\" font-size:14pt;\">\u0444\u044b</span></p></body></html>", None))
    # retranslateUi

