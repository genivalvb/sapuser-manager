# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUsers.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(890, 607)
        self.tabWidget_2 = QTabWidget(Form)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1171, 821))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.txtQuerie = QTextEdit(self.tab_6)
        self.txtQuerie.setObjectName(u"txtQuerie")
        self.txtQuerie.setGeometry(QRect(330, 450, 291, 31))
        self.pbCheckALLUser = QPushButton(self.tab_6)
        self.pbCheckALLUser.setObjectName(u"pbCheckALLUser")
        self.pbCheckALLUser.setGeometry(QRect(20, 530, 221, 41))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pbCheckALLUser.setFont(font)
        self.pbInserirTexto = QPushButton(self.tab_6)
        self.pbInserirTexto.setObjectName(u"pbInserirTexto")
        self.pbInserirTexto.setGeometry(QRect(690, 500, 181, 41))
        self.pbInserirTexto.setFont(font)
        self.pbLoadingData = QPushButton(self.tab_6)
        self.pbLoadingData.setObjectName(u"pbLoadingData")
        self.pbLoadingData.setGeometry(QRect(690, 420, 181, 41))
        self.pbLoadingData.setFont(font)
        self.pbDownloadSAPUsers = QPushButton(self.tab_6)
        self.pbDownloadSAPUsers.setObjectName(u"pbDownloadSAPUsers")
        self.pbDownloadSAPUsers.setGeometry(QRect(690, 380, 181, 41))
        self.pbDownloadSAPUsers.setFont(font)
        self.pbValidateRecord = QPushButton(self.tab_6)
        self.pbValidateRecord.setObjectName(u"pbValidateRecord")
        self.pbValidateRecord.setGeometry(QRect(690, 340, 181, 41))
        self.pbValidateRecord.setFont(font)
        self.pbCreateUser = QPushButton(self.tab_6)
        self.pbCreateUser.setObjectName(u"pbCreateUser")
        self.pbCreateUser.setGeometry(QRect(690, 300, 181, 41))
        self.pbCreateUser.setFont(font)
        self.cbUserExisted = QCheckBox(self.tab_6)
        self.cbUserExisted.setObjectName(u"cbUserExisted")
        self.cbUserExisted.setGeometry(QRect(700, 280, 121, 17))
        self.tabWidget = QTabWidget(self.tab_6)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 260, 681, 161))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget_5 = QWidget(self.tab)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(10, 0, 261, 141))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.formLayoutWidget_5)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.txtRole01 = QLineEdit(self.formLayoutWidget_5)
        self.txtRole01.setObjectName(u"txtRole01")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.txtRole01)

        self.label_28 = QLabel(self.formLayoutWidget_5)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.txtRole02 = QLineEdit(self.formLayoutWidget_5)
        self.txtRole02.setObjectName(u"txtRole02")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.txtRole02)

        self.label_29 = QLabel(self.formLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.txtRole03 = QLineEdit(self.formLayoutWidget_5)
        self.txtRole03.setObjectName(u"txtRole03")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.txtRole03)

        self.label_30 = QLabel(self.formLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_30)

        self.txtRole04 = QLineEdit(self.formLayoutWidget_5)
        self.txtRole04.setObjectName(u"txtRole04")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.txtRole04)

        self.label_31 = QLabel(self.formLayoutWidget_5)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_31)

        self.txtRole05 = QLineEdit(self.formLayoutWidget_5)
        self.txtRole05.setObjectName(u"txtRole05")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.txtRole05)

        self.formLayoutWidget_6 = QWidget(self.tab)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(320, 0, 261, 141))
        self.formLayout_6 = QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.formLayoutWidget_6)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_32)

        self.label_33 = QLabel(self.formLayoutWidget_6)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_33)

        self.label_34 = QLabel(self.formLayoutWidget_6)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_34)

        self.label_35 = QLabel(self.formLayoutWidget_6)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_35)

        self.label_36 = QLabel(self.formLayoutWidget_6)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_36)

        self.txtRole06 = QLineEdit(self.formLayoutWidget_6)
        self.txtRole06.setObjectName(u"txtRole06")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.txtRole06)

        self.txtRole07 = QLineEdit(self.formLayoutWidget_6)
        self.txtRole07.setObjectName(u"txtRole07")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.txtRole07)

        self.txtRole08 = QLineEdit(self.formLayoutWidget_6)
        self.txtRole08.setObjectName(u"txtRole08")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.txtRole08)

        self.txtRole09 = QLineEdit(self.formLayoutWidget_6)
        self.txtRole09.setObjectName(u"txtRole09")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.txtRole09)

        self.txtRole10 = QLineEdit(self.formLayoutWidget_6)
        self.txtRole10.setObjectName(u"txtRole10")

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.txtRole10)

        self.pbCK01 = QPushButton(self.tab)
        self.pbCK01.setObjectName(u"pbCK01")
        self.pbCK01.setGeometry(QRect(280, 0, 21, 23))
        self.pbCK02 = QPushButton(self.tab)
        self.pbCK02.setObjectName(u"pbCK02")
        self.pbCK02.setGeometry(QRect(280, 25, 21, 23))
        self.pbCK03 = QPushButton(self.tab)
        self.pbCK03.setObjectName(u"pbCK03")
        self.pbCK03.setGeometry(QRect(280, 50, 21, 23))
        self.pbCK04 = QPushButton(self.tab)
        self.pbCK04.setObjectName(u"pbCK04")
        self.pbCK04.setGeometry(QRect(280, 76, 21, 23))
        self.pbCK05 = QPushButton(self.tab)
        self.pbCK05.setObjectName(u"pbCK05")
        self.pbCK05.setGeometry(QRect(280, 102, 21, 23))
        self.pbCK06 = QPushButton(self.tab)
        self.pbCK06.setObjectName(u"pbCK06")
        self.pbCK06.setGeometry(QRect(590, -1, 21, 23))
        self.pbCK07 = QPushButton(self.tab)
        self.pbCK07.setObjectName(u"pbCK07")
        self.pbCK07.setGeometry(QRect(590, 25, 21, 23))
        self.pbCK08 = QPushButton(self.tab)
        self.pbCK08.setObjectName(u"pbCK08")
        self.pbCK08.setGeometry(QRect(590, 52, 21, 23))
        self.pbCK09 = QPushButton(self.tab)
        self.pbCK09.setObjectName(u"pbCK09")
        self.pbCK09.setGeometry(QRect(590, 78, 21, 23))
        self.pbCK10 = QPushButton(self.tab)
        self.pbCK10.setObjectName(u"pbCK10")
        self.pbCK10.setGeometry(QRect(590, 103, 21, 23))
        self.pbNumber = QLabel(self.tab)
        self.pbNumber.setObjectName(u"pbNumber")
        self.pbNumber.setGeometry(QRect(620, 30, 41, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.pbNumber.setFont(font1)
        self.pbNumber.setFrameShape(QFrame.Box)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayoutWidget_7 = QWidget(self.tab_2)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(10, 0, 261, 161))
        self.formLayout_7 = QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.formLayoutWidget_7)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.label_38 = QLabel(self.formLayoutWidget_7)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_38)

        self.label_39 = QLabel(self.formLayoutWidget_7)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_39)

        self.label_40 = QLabel(self.formLayoutWidget_7)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_40)

        self.label_41 = QLabel(self.formLayoutWidget_7)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.label_41)

        self.txtRole11 = QLineEdit(self.formLayoutWidget_7)
        self.txtRole11.setObjectName(u"txtRole11")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.txtRole11)

        self.txtRole12 = QLineEdit(self.formLayoutWidget_7)
        self.txtRole12.setObjectName(u"txtRole12")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.txtRole12)

        self.txtRole13 = QLineEdit(self.formLayoutWidget_7)
        self.txtRole13.setObjectName(u"txtRole13")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.txtRole13)

        self.txtRole14 = QLineEdit(self.formLayoutWidget_7)
        self.txtRole14.setObjectName(u"txtRole14")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.txtRole14)

        self.txtRole15 = QLineEdit(self.formLayoutWidget_7)
        self.txtRole15.setObjectName(u"txtRole15")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.txtRole15)

        self.formLayoutWidget_8 = QWidget(self.tab_2)
        self.formLayoutWidget_8.setObjectName(u"formLayoutWidget_8")
        self.formLayoutWidget_8.setGeometry(QRect(320, 0, 261, 161))
        self.formLayout_8 = QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.formLayoutWidget_8)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_42)

        self.label_43 = QLabel(self.formLayoutWidget_8)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_43)

        self.label_44 = QLabel(self.formLayoutWidget_8)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_44)

        self.label_45 = QLabel(self.formLayoutWidget_8)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_45)

        self.label_46 = QLabel(self.formLayoutWidget_8)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_46)

        self.txtRole16 = QLineEdit(self.formLayoutWidget_8)
        self.txtRole16.setObjectName(u"txtRole16")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.txtRole16)

        self.txtRole17 = QLineEdit(self.formLayoutWidget_8)
        self.txtRole17.setObjectName(u"txtRole17")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.txtRole17)

        self.txtRole18 = QLineEdit(self.formLayoutWidget_8)
        self.txtRole18.setObjectName(u"txtRole18")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.txtRole18)

        self.txtRole19 = QLineEdit(self.formLayoutWidget_8)
        self.txtRole19.setObjectName(u"txtRole19")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.txtRole19)

        self.txtRole20 = QLineEdit(self.formLayoutWidget_8)
        self.txtRole20.setObjectName(u"txtRole20")

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.txtRole20)

        self.pbCK12 = QPushButton(self.tab_2)
        self.pbCK12.setObjectName(u"pbCK12")
        self.pbCK12.setGeometry(QRect(280, 25, 21, 23))
        self.pbCK13 = QPushButton(self.tab_2)
        self.pbCK13.setObjectName(u"pbCK13")
        self.pbCK13.setGeometry(QRect(280, 50, 21, 23))
        self.pbCK14 = QPushButton(self.tab_2)
        self.pbCK14.setObjectName(u"pbCK14")
        self.pbCK14.setGeometry(QRect(280, 76, 21, 23))
        self.pbCK15 = QPushButton(self.tab_2)
        self.pbCK15.setObjectName(u"pbCK15")
        self.pbCK15.setGeometry(QRect(280, 102, 21, 23))
        self.pbCK11 = QPushButton(self.tab_2)
        self.pbCK11.setObjectName(u"pbCK11")
        self.pbCK11.setGeometry(QRect(280, 0, 21, 23))
        self.pushButton_17 = QPushButton(self.tab_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(590, 78, 21, 23))
        self.pushButton_18 = QPushButton(self.tab_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(590, 103, 21, 23))
        self.pushButton_19 = QPushButton(self.tab_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(590, -1, 21, 23))
        self.pushButton_20 = QPushButton(self.tab_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(590, 52, 21, 23))
        self.pushButton_21 = QPushButton(self.tab_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(590, 25, 21, 23))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.formLayoutWidget_9 = QWidget(self.tab_3)
        self.formLayoutWidget_9.setObjectName(u"formLayoutWidget_9")
        self.formLayoutWidget_9.setGeometry(QRect(10, 0, 261, 161))
        self.formLayout_9 = QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.formLayoutWidget_9)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.label_48 = QLabel(self.formLayoutWidget_9)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_48)

        self.label_49 = QLabel(self.formLayoutWidget_9)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_49)

        self.label_50 = QLabel(self.formLayoutWidget_9)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.label_50)

        self.label_51 = QLabel(self.formLayoutWidget_9)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.label_51)

        self.txtRole21 = QLineEdit(self.formLayoutWidget_9)
        self.txtRole21.setObjectName(u"txtRole21")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.txtRole21)

        self.txtRole22 = QLineEdit(self.formLayoutWidget_9)
        self.txtRole22.setObjectName(u"txtRole22")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.txtRole22)

        self.txtRole23 = QLineEdit(self.formLayoutWidget_9)
        self.txtRole23.setObjectName(u"txtRole23")

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.txtRole23)

        self.txtRole24 = QLineEdit(self.formLayoutWidget_9)
        self.txtRole24.setObjectName(u"txtRole24")

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.txtRole24)

        self.txtRole25 = QLineEdit(self.formLayoutWidget_9)
        self.txtRole25.setObjectName(u"txtRole25")

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.txtRole25)

        self.formLayoutWidget_10 = QWidget(self.tab_3)
        self.formLayoutWidget_10.setObjectName(u"formLayoutWidget_10")
        self.formLayoutWidget_10.setGeometry(QRect(320, 0, 271, 161))
        self.formLayout_10 = QFormLayout(self.formLayoutWidget_10)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.formLayoutWidget_10)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_52)

        self.label_53 = QLabel(self.formLayoutWidget_10)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_53)

        self.label_54 = QLabel(self.formLayoutWidget_10)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_54)

        self.label_55 = QLabel(self.formLayoutWidget_10)
        self.label_55.setObjectName(u"label_55")

        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.label_55)

        self.label_56 = QLabel(self.formLayoutWidget_10)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.label_56)

        self.txtRole26 = QLineEdit(self.formLayoutWidget_10)
        self.txtRole26.setObjectName(u"txtRole26")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.txtRole26)

        self.txtRole27 = QLineEdit(self.formLayoutWidget_10)
        self.txtRole27.setObjectName(u"txtRole27")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.txtRole27)

        self.txtRole28 = QLineEdit(self.formLayoutWidget_10)
        self.txtRole28.setObjectName(u"txtRole28")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.txtRole28)

        self.txtRole29 = QLineEdit(self.formLayoutWidget_10)
        self.txtRole29.setObjectName(u"txtRole29")

        self.formLayout_10.setWidget(3, QFormLayout.FieldRole, self.txtRole29)

        self.txtRole30 = QLineEdit(self.formLayoutWidget_10)
        self.txtRole30.setObjectName(u"txtRole30")

        self.formLayout_10.setWidget(4, QFormLayout.FieldRole, self.txtRole30)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.formLayoutWidget_11 = QWidget(self.tab_4)
        self.formLayoutWidget_11.setObjectName(u"formLayoutWidget_11")
        self.formLayoutWidget_11.setGeometry(QRect(10, 0, 261, 161))
        self.formLayout_11 = QFormLayout(self.formLayoutWidget_11)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.formLayoutWidget_11)
        self.label_57.setObjectName(u"label_57")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_57)

        self.label_58 = QLabel(self.formLayoutWidget_11)
        self.label_58.setObjectName(u"label_58")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_58)

        self.label_59 = QLabel(self.formLayoutWidget_11)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_11.setWidget(2, QFormLayout.LabelRole, self.label_59)

        self.label_60 = QLabel(self.formLayoutWidget_11)
        self.label_60.setObjectName(u"label_60")

        self.formLayout_11.setWidget(3, QFormLayout.LabelRole, self.label_60)

        self.label_61 = QLabel(self.formLayoutWidget_11)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_11.setWidget(4, QFormLayout.LabelRole, self.label_61)

        self.txtRole31 = QLineEdit(self.formLayoutWidget_11)
        self.txtRole31.setObjectName(u"txtRole31")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.txtRole31)

        self.txtRole32 = QLineEdit(self.formLayoutWidget_11)
        self.txtRole32.setObjectName(u"txtRole32")

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.txtRole32)

        self.txtRole33 = QLineEdit(self.formLayoutWidget_11)
        self.txtRole33.setObjectName(u"txtRole33")

        self.formLayout_11.setWidget(2, QFormLayout.FieldRole, self.txtRole33)

        self.txtRole34 = QLineEdit(self.formLayoutWidget_11)
        self.txtRole34.setObjectName(u"txtRole34")

        self.formLayout_11.setWidget(3, QFormLayout.FieldRole, self.txtRole34)

        self.txtRole35 = QLineEdit(self.formLayoutWidget_11)
        self.txtRole35.setObjectName(u"txtRole35")

        self.formLayout_11.setWidget(4, QFormLayout.FieldRole, self.txtRole35)

        self.formLayoutWidget_12 = QWidget(self.tab_4)
        self.formLayoutWidget_12.setObjectName(u"formLayoutWidget_12")
        self.formLayoutWidget_12.setGeometry(QRect(320, 0, 271, 161))
        self.formLayout_12 = QFormLayout(self.formLayoutWidget_12)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.formLayoutWidget_12)
        self.label_62.setObjectName(u"label_62")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_62)

        self.label_63 = QLabel(self.formLayoutWidget_12)
        self.label_63.setObjectName(u"label_63")

        self.formLayout_12.setWidget(1, QFormLayout.LabelRole, self.label_63)

        self.label_64 = QLabel(self.formLayoutWidget_12)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_12.setWidget(2, QFormLayout.LabelRole, self.label_64)

        self.label_65 = QLabel(self.formLayoutWidget_12)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_12.setWidget(3, QFormLayout.LabelRole, self.label_65)

        self.label_66 = QLabel(self.formLayoutWidget_12)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_12.setWidget(4, QFormLayout.LabelRole, self.label_66)

        self.txtRole36 = QLineEdit(self.formLayoutWidget_12)
        self.txtRole36.setObjectName(u"txtRole36")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.txtRole36)

        self.txtRole37 = QLineEdit(self.formLayoutWidget_12)
        self.txtRole37.setObjectName(u"txtRole37")

        self.formLayout_12.setWidget(1, QFormLayout.FieldRole, self.txtRole37)

        self.txtRole38 = QLineEdit(self.formLayoutWidget_12)
        self.txtRole38.setObjectName(u"txtRole38")

        self.formLayout_12.setWidget(2, QFormLayout.FieldRole, self.txtRole38)

        self.txtRole39 = QLineEdit(self.formLayoutWidget_12)
        self.txtRole39.setObjectName(u"txtRole39")

        self.formLayout_12.setWidget(3, QFormLayout.FieldRole, self.txtRole39)

        self.txtRole40 = QLineEdit(self.formLayoutWidget_12)
        self.txtRole40.setObjectName(u"txtRole40")

        self.formLayout_12.setWidget(4, QFormLayout.FieldRole, self.txtRole40)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.formLayoutWidget_3 = QWidget(self.tab_5)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 0, 261, 161))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_18 = QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.formLayoutWidget_3)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_21)

        self.txtRole41 = QLineEdit(self.formLayoutWidget_3)
        self.txtRole41.setObjectName(u"txtRole41")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.txtRole41)

        self.txtRole42 = QLineEdit(self.formLayoutWidget_3)
        self.txtRole42.setObjectName(u"txtRole42")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.txtRole42)

        self.txtRole43 = QLineEdit(self.formLayoutWidget_3)
        self.txtRole43.setObjectName(u"txtRole43")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.txtRole43)

        self.txtRole44 = QLineEdit(self.formLayoutWidget_3)
        self.txtRole44.setObjectName(u"txtRole44")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.txtRole44)

        self.txtRole45 = QLineEdit(self.formLayoutWidget_3)
        self.txtRole45.setObjectName(u"txtRole45")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.txtRole45)

        self.formLayoutWidget_4 = QWidget(self.tab_5)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(320, 0, 271, 161))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.formLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.label_23 = QLabel(self.formLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.label_24 = QLabel(self.formLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_24)

        self.label_25 = QLabel(self.formLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_25)

        self.label_26 = QLabel(self.formLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_26)

        self.txtRole46 = QLineEdit(self.formLayoutWidget_4)
        self.txtRole46.setObjectName(u"txtRole46")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.txtRole46)

        self.txtRole47 = QLineEdit(self.formLayoutWidget_4)
        self.txtRole47.setObjectName(u"txtRole47")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.txtRole47)

        self.txtRole48 = QLineEdit(self.formLayoutWidget_4)
        self.txtRole48.setObjectName(u"txtRole48")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.txtRole48)

        self.txtRole49 = QLineEdit(self.formLayoutWidget_4)
        self.txtRole49.setObjectName(u"txtRole49")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.txtRole49)

        self.txtRole50 = QLineEdit(self.formLayoutWidget_4)
        self.txtRole50.setObjectName(u"txtRole50")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.txtRole50)

        self.tabWidget.addTab(self.tab_5, "")
        self.pbExceptional2 = QPushButton(self.tab_6)
        self.pbExceptional2.setObjectName(u"pbExceptional2")
        self.pbExceptional2.setGeometry(QRect(290, 504, 21, 23))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(255, 255, 63, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 127, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 170, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.pbExceptional2.setPalette(palette)
        self.pbExceptional2.setFont(font)
        self.pbExceptional2.setAutoFillBackground(False)
        self.pbExceptional2.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(self.tab_6)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 425, 261, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtexceptional2 = QLineEdit(self.gridLayoutWidget)
        self.txtexceptional2.setObjectName(u"txtexceptional2")

        self.gridLayout.addWidget(self.txtexceptional2, 3, 0, 1, 1)

        self.txtexceptional1 = QLineEdit(self.gridLayoutWidget)
        self.txtexceptional1.setObjectName(u"txtexceptional1")

        self.gridLayout.addWidget(self.txtexceptional1, 2, 0, 1, 1)

        self.label_67 = QLabel(self.gridLayoutWidget)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout.addWidget(self.label_67, 0, 0, 1, 1)

        self.txtexceptional = QLineEdit(self.gridLayoutWidget)
        self.txtexceptional.setObjectName(u"txtexceptional")
        self.txtexceptional.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.txtexceptional, 1, 0, 1, 1)

        self.pbExceptional1 = QPushButton(self.tab_6)
        self.pbExceptional1.setObjectName(u"pbExceptional1")
        self.pbExceptional1.setGeometry(QRect(290, 477, 21, 23))
        self.pbExceptional1.setFont(font)
        self.pbExceptional = QPushButton(self.tab_6)
        self.pbExceptional.setObjectName(u"pbExceptional")
        self.pbExceptional.setGeometry(QRect(290, 450, 21, 23))
        self.pbExceptional.setFont(font)
        self.groupBox = QGroupBox(self.tab_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 210, 311, 41))
        self.rbN1 = QRadioButton(self.groupBox)
        self.rbN1.setObjectName(u"rbN1")
        self.rbN1.setGeometry(QRect(10, 20, 51, 22))
        self.rbN2 = QRadioButton(self.groupBox)
        self.rbN2.setObjectName(u"rbN2")
        self.rbN2.setGeometry(QRect(60, 20, 51, 22))
        self.rbN3 = QRadioButton(self.groupBox)
        self.rbN3.setObjectName(u"rbN3")
        self.rbN3.setGeometry(QRect(120, 20, 51, 22))
        self.rbN4 = QRadioButton(self.groupBox)
        self.rbN4.setObjectName(u"rbN4")
        self.rbN4.setGeometry(QRect(170, 20, 51, 22))
        self.rbN5 = QRadioButton(self.groupBox)
        self.rbN5.setObjectName(u"rbN5")
        self.rbN5.setGeometry(QRect(220, 20, 51, 22))
        self.formLayoutWidget = QWidget(self.tab_6)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 311, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txtrequestId = QLineEdit(self.formLayoutWidget)
        self.txtrequestId.setObjectName(u"txtrequestId")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtrequestId)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.txtsystemType = QLineEdit(self.formLayoutWidget)
        self.txtsystemType.setObjectName(u"txtsystemType")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtsystemType)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.txtsystemEnv = QLineEdit(self.formLayoutWidget)
        self.txtsystemEnv.setObjectName(u"txtsystemEnv")
        self.txtsystemEnv.setAutoFillBackground(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtsystemEnv)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.txtgroup = QLineEdit(self.formLayoutWidget)
        self.txtgroup.setObjectName(u"txtgroup")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtgroup)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.txtsncName = QLineEdit(self.formLayoutWidget)
        self.txtsncName.setObjectName(u"txtsncName")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txtsncName)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.txtlanguage = QLineEdit(self.formLayoutWidget)
        self.txtlanguage.setObjectName(u"txtlanguage")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.txtlanguage)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.txtplant = QLineEdit(self.formLayoutWidget)
        self.txtplant.setObjectName(u"txtplant")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.txtplant)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.txtlogin = QLineEdit(self.formLayoutWidget)
        self.txtlogin.setObjectName(u"txtlogin")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.txtlogin.setPalette(palette1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.txtlogin)

        self.lblExiste = QLabel(self.tab_6)
        self.lblExiste.setObjectName(u"lblExiste")
        self.lblExiste.setGeometry(QRect(340, 250, 331, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.lblExiste.setFont(font2)
        self.lblExiste.setAcceptDrops(False)
        self.lblExiste.setAutoFillBackground(True)
        self.lblExiste.setFrameShape(QFrame.Box)
        self.lblExiste.setFrameShadow(QFrame.Raised)
        self.pbLast = QPushButton(self.tab_6)
        self.pbLast.setObjectName(u"pbLast")
        self.pbLast.setGeometry(QRect(590, 220, 81, 27))
        self.pbNext = QPushButton(self.tab_6)
        self.pbNext.setObjectName(u"pbNext")
        self.pbNext.setGeometry(QRect(500, 220, 81, 27))
        self.pbBack = QPushButton(self.tab_6)
        self.pbBack.setObjectName(u"pbBack")
        self.pbBack.setGeometry(QRect(420, 220, 81, 27))
        self.pbFirst = QPushButton(self.tab_6)
        self.pbFirst.setObjectName(u"pbFirst")
        self.pbFirst.setGeometry(QRect(330, 220, 81, 27))
        self.formLayoutWidget_2 = QWidget(self.tab_6)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(330, 0, 341, 211))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.txtlastName = QLineEdit(self.formLayoutWidget_2)
        self.txtlastName.setObjectName(u"txtlastName")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.txtlastName)

        self.label_12 = QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.txtfunction = QLineEdit(self.formLayoutWidget_2)
        self.txtfunction.setObjectName(u"txtfunction")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.txtfunction)

        self.label_13 = QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.txtemail = QLineEdit(self.formLayoutWidget_2)
        self.txtemail.setObjectName(u"txtemail")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.txtemail)

        self.label_14 = QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_14)

        self.txtsexo = QLineEdit(self.formLayoutWidget_2)
        self.txtsexo.setObjectName(u"txtsexo")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.txtsexo)

        self.label_15 = QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.txtdepartment = QLineEdit(self.formLayoutWidget_2)
        self.txtdepartment.setObjectName(u"txtdepartment")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.txtdepartment)

        self.label_16 = QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.txtaliasUser = QLineEdit(self.formLayoutWidget_2)
        self.txtaliasUser.setObjectName(u"txtaliasUser")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.txtaliasUser)

        self.label_17 = QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.txtdeparture = QLineEdit(self.formLayoutWidget_2)
        self.txtdeparture.setObjectName(u"txtdeparture")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.txtdeparture)

        self.txtname = QLineEdit(self.formLayoutWidget_2)
        self.txtname.setObjectName(u"txtname")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.txtname)

        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.pbUserExisted = QPushButton(self.tab_6)
        self.pbUserExisted.setObjectName(u"pbUserExisted")
        self.pbUserExisted.setGeometry(QRect(690, 230, 181, 41))
        self.pbUserExisted.setFont(font)
        self.gbox2 = QGroupBox(self.tab_6)
        self.gbox2.setObjectName(u"gbox2")
        self.gbox2.setGeometry(QRect(690, 10, 151, 161))
        self.rbNew = QRadioButton(self.gbox2)
        self.rbNew.setObjectName(u"rbNew")
        self.rbNew.setGeometry(QRect(10, 20, 82, 17))
        self.rbUnlockUser = QRadioButton(self.gbox2)
        self.rbUnlockUser.setObjectName(u"rbUnlockUser")
        self.rbUnlockUser.setGeometry(QRect(10, 50, 101, 17))
        self.rbReplaceProfile = QRadioButton(self.gbox2)
        self.rbReplaceProfile.setObjectName(u"rbReplaceProfile")
        self.rbReplaceProfile.setGeometry(QRect(10, 80, 101, 17))
        self.rbExceptionalRequest = QRadioButton(self.gbox2)
        self.rbExceptionalRequest.setObjectName(u"rbExceptionalRequest")
        self.rbExceptionalRequest.setGeometry(QRect(10, 110, 131, 17))
        self.rbDeleteUser = QRadioButton(self.gbox2)
        self.rbDeleteUser.setObjectName(u"rbDeleteUser")
        self.rbDeleteUser.setGeometry(QRect(10, 140, 131, 17))
        self.pbUserExist = QPushButton(self.tab_6)
        self.pbUserExist.setObjectName(u"pbUserExist")
        self.pbUserExist.setGeometry(QRect(690, 190, 181, 41))
        self.pbUserExist.setFont(font)
        self.cbTrip = QCheckBox(self.tab_6)
        self.cbTrip.setObjectName(u"cbTrip")
        self.cbTrip.setGeometry(QRect(700, 170, 70, 17))
        self.lcdNumber = QLCDNumber(self.tab_6)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(630, 420, 51, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.lcdNumber.setFont(font3)
        self.txtrequestId_2 = QLineEdit(self.tab_6)
        self.txtrequestId_2.setObjectName(u"txtrequestId_2")
        self.txtrequestId_2.setGeometry(QRect(380, 490, 121, 31))
        self.label_68 = QLabel(self.tab_6)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(330, 490, 51, 20))
        font4 = QFont()
        font4.setPointSize(12)
        self.label_68.setFont(font4)
        self.pbProcurar = QPushButton(self.tab_6)
        self.pbProcurar.setObjectName(u"pbProcurar")
        self.pbProcurar.setGeometry(QRect(510, 490, 111, 31))
        self.pbLoadScreen = QPushButton(self.tab_6)
        self.pbLoadScreen.setObjectName(u"pbLoadScreen")
        self.pbLoadScreen.setGeometry(QRect(690, 460, 181, 41))
        self.pbLoadScreen.setFont(font)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.widget = QWidget(self.tab_7)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 371, 111))
        self.label_70 = QLabel(self.widget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 10, 51, 16))
        font5 = QFont()
        font5.setPointSize(10)
        self.label_70.setFont(font5)
        self.label_69 = QLabel(self.widget)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 40, 51, 20))
        self.label_69.setFont(font5)
        self.label_71 = QLabel(self.widget)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(10, 70, 51, 16))
        self.label_71.setFont(font5)
        self.pBQuery01 = QPushButton(self.widget)
        self.pBQuery01.setObjectName(u"pBQuery01")
        self.pBQuery01.setGeometry(QRect(200, 10, 75, 23))
        self.pBQuery02 = QPushButton(self.widget)
        self.pBQuery02.setObjectName(u"pBQuery02")
        self.pBQuery02.setGeometry(QRect(200, 40, 75, 23))
        self.pBQuery03 = QPushButton(self.widget)
        self.pBQuery03.setObjectName(u"pBQuery03")
        self.pBQuery03.setGeometry(QRect(200, 70, 75, 23))
        self.txtQuery01 = QLineEdit(self.widget)
        self.txtQuery01.setObjectName(u"txtQuery01")
        self.txtQuery01.setGeometry(QRect(70, 10, 113, 20))
        self.txtQuery02 = QLineEdit(self.widget)
        self.txtQuery02.setObjectName(u"txtQuery02")
        self.txtQuery02.setGeometry(QRect(70, 40, 113, 20))
        self.txtQuery03 = QLineEdit(self.widget)
        self.txtQuery03.setObjectName(u"txtQuery03")
        self.txtQuery03.setGeometry(QRect(70, 70, 113, 20))
        self.pBQuery01_2 = QPushButton(self.widget)
        self.pBQuery01_2.setObjectName(u"pBQuery01_2")
        self.pBQuery01_2.setGeometry(QRect(280, 10, 75, 23))
        self.pBQuery02_2 = QPushButton(self.widget)
        self.pBQuery02_2.setObjectName(u"pBQuery02_2")
        self.pBQuery02_2.setGeometry(QRect(280, 40, 75, 23))
        self.pBQuery03_2 = QPushButton(self.widget)
        self.pBQuery03_2.setObjectName(u"pBQuery03_2")
        self.pBQuery03_2.setGeometry(QRect(280, 70, 75, 23))
        self.tabWidget_2.addTab(self.tab_7, "")

        self.retranslateUi(Form)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Criar Usu\u00e1rio no SAP", None))
        self.pbCheckALLUser.setText(QCoreApplication.translate("Form", u"Check All Incompatibility per User", None))
        self.pbInserirTexto.setText(QCoreApplication.translate("Form", u"Autom\u00e1tico", None))
        self.pbLoadingData.setText(QCoreApplication.translate("Form", u"01-Carregar Dados", None))
        self.pbDownloadSAPUsers.setText(QCoreApplication.translate("Form", u"Download SAP Users", None))
        self.pbValidateRecord.setText(QCoreApplication.translate("Form", u"Validar Registro", None))
        self.pbCreateUser.setText(QCoreApplication.translate("Form", u"Criar usu\u00e1rio no SAP", None))
        self.cbUserExisted.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio j\u00e1 existiu?", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Role 01", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Role 02", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Role 03", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Role 04", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Role 05", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Role 06", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Role 07", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Role 08", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Role 09", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Role 10", None))
        self.pbCK01.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK02.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK03.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK04.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK05.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK06.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK07.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK08.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK09.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK10.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbNumber.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Role 11", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Role 12", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Role 13", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"Role 14", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Role 15", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"Role 16", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"Role 17", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"Role 18", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"Role 19", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"Role 20", None))
        self.pbCK12.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK13.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK14.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK15.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbCK11.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"CK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"Role 21", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"Role 22", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"Role 23", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"Role 24", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"Role 25", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"Role 26", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"Role 27", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"Role 28", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"Role 29", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"Role 30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Tab 3", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Role 31", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"Role 32", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"Role 33", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Role 34", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"Role 35", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"Role 36", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"Role 37", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"Role 38", None))
        self.label_65.setText(QCoreApplication.translate("Form", u"Role 39", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"Role 40", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tab 4", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Role 41", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Role 42", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Role 43", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Role 44", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Role 45", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Role 46", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Role 47", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Role 48", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Role 49", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Role 50", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Tab 5", None))
        self.pbExceptional2.setText(QCoreApplication.translate("Form", u"C3", None))
        self.label_67.setText(QCoreApplication.translate("Form", u"ROLE Exceptional:", None))
        self.pbExceptional1.setText(QCoreApplication.translate("Form", u"CK", None))
        self.pbExceptional.setText(QCoreApplication.translate("Form", u"CK", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.rbN1.setText(QCoreApplication.translate("Form", u"N1", None))
        self.rbN2.setText(QCoreApplication.translate("Form", u"N2", None))
        self.rbN3.setText(QCoreApplication.translate("Form", u"N3", None))
        self.rbN4.setText(QCoreApplication.translate("Form", u"N4", None))
        self.rbN5.setText(QCoreApplication.translate("Form", u"N5", None))
        self.label.setText(QCoreApplication.translate("Form", u"Request ID:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"System Type:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"System Env:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Group:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"SNC Name:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Language:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Plant:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Login:", None))
        self.lblExiste.setText("")
        self.pbLast.setText(QCoreApplication.translate("Form", u"Last", None))
        self.pbNext.setText(QCoreApplication.translate("Form", u"Next", None))
        self.pbBack.setText(QCoreApplication.translate("Form", u"Back", None))
        self.pbFirst.setText(QCoreApplication.translate("Form", u"First", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Sobrenome:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Fun\u00e7\u00e3o:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Sexo:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Department:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Alias user:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"ED Departure:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Nome:", None))
        self.pbUserExisted.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio Existiu?", None))
        self.gbox2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.rbNew.setText(QCoreApplication.translate("Form", u"NEW", None))
        self.rbUnlockUser.setText(QCoreApplication.translate("Form", u"Unlock User", None))
        self.rbReplaceProfile.setText(QCoreApplication.translate("Form", u"Replace Profile", None))
        self.rbExceptionalRequest.setText(QCoreApplication.translate("Form", u"Exceptional Request", None))
        self.rbDeleteUser.setText(QCoreApplication.translate("Form", u"Delete User", None))
        self.pbUserExist.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio Existe?", None))
        self.cbTrip.setText(QCoreApplication.translate("Form", u"TRIP ??", None))
        self.label_68.setText(QCoreApplication.translate("Form", u"Ticket:", None))
        self.pbProcurar.setText(QCoreApplication.translate("Form", u"Procurar", None))
        self.pbLoadScreen.setText(QCoreApplication.translate("Form", u"02-Load Screen", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Tab 1", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"Query 01", None))
        self.label_69.setText(QCoreApplication.translate("Form", u"Query 02", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"Query 03", None))
        self.pBQuery01.setText(QCoreApplication.translate("Form", u"Standard", None))
        self.pBQuery02.setText(QCoreApplication.translate("Form", u"Standard", None))
        self.pBQuery03.setText(QCoreApplication.translate("Form", u"Standard", None))
        self.pBQuery01_2.setText(QCoreApplication.translate("Form", u"Global", None))
        self.pBQuery02_2.setText(QCoreApplication.translate("Form", u"Global", None))
        self.pBQuery03_2.setText(QCoreApplication.translate("Form", u"Global", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

