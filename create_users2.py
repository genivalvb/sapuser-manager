# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUsers2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CreateUsers2(object):
    def setupUi(self, CreateUsers2):
        if not CreateUsers2.objectName():
            CreateUsers2.setObjectName(u"CreateUsers2")
        CreateUsers2.setWindowModality(Qt.WindowModal)
        CreateUsers2.resize(1440, 725)
        self.centralwidget = QWidget(CreateUsers2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1231, 661))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        CreateUsers2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CreateUsers2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1440, 21))
        CreateUsers2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CreateUsers2)
        self.statusbar.setObjectName(u"statusbar")
        CreateUsers2.setStatusBar(self.statusbar)

        self.retranslateUi(CreateUsers2)

        QMetaObject.connectSlotsByName(CreateUsers2)
    # setupUi

    def retranslateUi(self, CreateUsers2):
        CreateUsers2.setWindowTitle(QCoreApplication.translate("CreateUsers2", u"SAP Create Users by table", None))
    # retranslateUi

