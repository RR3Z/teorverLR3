# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 508)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#bernuliFormulaType{\n"
"	font-size:17px;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 0px;\n"
"	border-radius: 7px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	background: #ffbf00;\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffbf00,  stop:1 #fa9f17);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 0px;\n"
"	border-radius: 7px;\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	background: #d9a407;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #e55e5c,  stop:1 #e01e1b);\n"
"}\n"
"\n"
"#choiceMenu, #mainBody{\n"
"	opacity: 1;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: #fff;\n"
"	border: 1px solid;\n"
"	border-radius: 9px;\n"
"	border-color: #4a4343;\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.choiceMenu = QWidget(self.centralwidget)
        self.choiceMenu.setObjectName(u"choiceMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choiceMenu.sizePolicy().hasHeightForWidth())
        self.choiceMenu.setSizePolicy(sizePolicy)
        self.choiceMenu.setMinimumSize(QSize(250, 0))
        self.choiceMenu.setMaximumSize(QSize(16777215, 16777215))
        self.choiceMenu.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.choiceMenu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.choiceMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.choiceLabel = QLabel(self.frame)
        self.choiceLabel.setObjectName(u"choiceLabel")
        self.choiceLabel.setLayoutDirection(Qt.LeftToRight)
        self.choiceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.choiceLabel)

        self.bernuliBtn = QPushButton(self.frame)
        self.bernuliBtn.setObjectName(u"bernuliBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bernuliBtn.sizePolicy().hasHeightForWidth())
        self.bernuliBtn.setSizePolicy(sizePolicy1)
        self.bernuliBtn.setMinimumSize(QSize(180, 0))
        self.bernuliBtn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.bernuliBtn)

        self.polynomBtn = QPushButton(self.frame)
        self.polynomBtn.setObjectName(u"polynomBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.polynomBtn.sizePolicy().hasHeightForWidth())
        self.polynomBtn.setSizePolicy(sizePolicy2)
        self.polynomBtn.setMinimumSize(QSize(230, 0))
        self.polynomBtn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.polynomBtn)

        self.integralBtn = QPushButton(self.frame)
        self.integralBtn.setObjectName(u"integralBtn")
        self.integralBtn.setMinimumSize(QSize(180, 0))
        self.integralBtn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.integralBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.choiceMenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.choiceMenu, 0, 0, 1, 1)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.mainBody)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mainWidget = QStackedWidget(self.mainBody)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy3)
        self.mainWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.mainWidget.setStyleSheet(u"")
        self.polynomPage = QWidget()
        self.polynomPage.setObjectName(u"polynomPage")
        self.gridLayout_5 = QGridLayout(self.polynomPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.polynomLabel = QLabel(self.polynomPage)
        self.polynomLabel.setObjectName(u"polynomLabel")
        self.polynomLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.polynomLabel, 0, 0, 1, 1)

        self.photoPolynomFormula = QLabel(self.polynomPage)
        self.photoPolynomFormula.setObjectName(u"photoPolynomFormula")
        self.photoPolynomFormula.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.photoPolynomFormula, 5, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pParamsLabel = QLabel(self.polynomPage)
        self.pParamsLabel.setObjectName(u"pParamsLabel")
        self.pParamsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.pParamsLabel)

        self.pParamsLine = QLineEdit(self.polynomPage)
        self.pParamsLine.setObjectName(u"pParamsLine")

        self.horizontalLayout_4.addWidget(self.pParamsLine)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.polynomAnswerLabel = QLabel(self.polynomPage)
        self.polynomAnswerLabel.setObjectName(u"polynomAnswerLabel")
        self.polynomAnswerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.polynomAnswerLabel)

        self.polynomAnswerLine = QLineEdit(self.polynomPage)
        self.polynomAnswerLine.setObjectName(u"polynomAnswerLine")
        self.polynomAnswerLine.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.polynomAnswerLine)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nParamLabel = QLabel(self.polynomPage)
        self.nParamLabel.setObjectName(u"nParamLabel")
        self.nParamLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.nParamLabel)

        self.nParamLine = QLineEdit(self.polynomPage)
        self.nParamLine.setObjectName(u"nParamLine")

        self.horizontalLayout.addWidget(self.nParamLine)


        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mParamsLabel = QLabel(self.polynomPage)
        self.mParamsLabel.setObjectName(u"mParamsLabel")
        self.mParamsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.mParamsLabel)

        self.mParamsLine = QLineEdit(self.polynomPage)
        self.mParamsLine.setObjectName(u"mParamsLine")

        self.horizontalLayout_3.addWidget(self.mParamsLine)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.calculatePolynomBtn = QPushButton(self.polynomPage)
        self.calculatePolynomBtn.setObjectName(u"calculatePolynomBtn")
        self.calculatePolynomBtn.setMinimumSize(QSize(150, 0))
        self.calculatePolynomBtn.setStyleSheet(u"calculatePolynomBtn\n"
"{\n"
"font-weight:bold;\n"
"font-size: 16px;\n"
"}")

        self.gridLayout_5.addWidget(self.calculatePolynomBtn, 8, 0, 1, 1)

        self.polynomDescription = QLabel(self.polynomPage)
        self.polynomDescription.setObjectName(u"polynomDescription")
        self.polynomDescription.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.polynomDescription, 6, 0, 1, 1)

        self.mainWidget.addWidget(self.polynomPage)
        self.integralPage = QWidget()
        self.integralPage.setObjectName(u"integralPage")
        self.gridLayout_6 = QGridLayout(self.integralPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.photoIntegralFormula1 = QLabel(self.integralPage)
        self.photoIntegralFormula1.setObjectName(u"photoIntegralFormula1")
        self.photoIntegralFormula1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.photoIntegralFormula1)

        self.photoIntegralFormula2 = QLabel(self.integralPage)
        self.photoIntegralFormula2.setObjectName(u"photoIntegralFormula2")
        self.photoIntegralFormula2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.photoIntegralFormula2)

        self.photoIntegralFormula3 = QLabel(self.integralPage)
        self.photoIntegralFormula3.setObjectName(u"photoIntegralFormula3")
        self.photoIntegralFormula3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.photoIntegralFormula3)

        self.description = QLabel(self.integralPage)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.description)


        self.gridLayout_6.addLayout(self.verticalLayout_8, 3, 0, 1, 1)

        self.label = QLabel(self.integralPage)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nNumberLabel = QLabel(self.integralPage)
        self.nNumberLabel.setObjectName(u"nNumberLabel")
        self.nNumberLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.nNumberLabel)

        self.nNumberLine = QLineEdit(self.integralPage)
        self.nNumberLine.setObjectName(u"nNumberLine")

        self.horizontalLayout_6.addWidget(self.nNumberLine)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.integralPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.x1ResultLabel = QLabel(self.integralPage)
        self.x1ResultLabel.setObjectName(u"x1ResultLabel")

        self.horizontalLayout_5.addWidget(self.x1ResultLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.x2TextLabel = QLabel(self.integralPage)
        self.x2TextLabel.setObjectName(u"x2TextLabel")
        self.x2TextLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.x2TextLabel)

        self.x2ResultLabel = QLabel(self.integralPage)
        self.x2ResultLabel.setObjectName(u"x2ResultLabel")

        self.horizontalLayout_9.addWidget(self.x2ResultLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.integralAnswerLabel = QLabel(self.integralPage)
        self.integralAnswerLabel.setObjectName(u"integralAnswerLabel")
        self.integralAnswerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.integralAnswerLabel)

        self.integralAnswerLine = QLineEdit(self.integralPage)
        self.integralAnswerLine.setObjectName(u"integralAnswerLine")
        self.integralAnswerLine.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.integralAnswerLine)

        self.calculateIntegralBtn = QPushButton(self.integralPage)
        self.calculateIntegralBtn.setObjectName(u"calculateIntegralBtn")

        self.verticalLayout_9.addWidget(self.calculateIntegralBtn)


        self.gridLayout_6.addLayout(self.verticalLayout_9, 4, 0, 1, 1)

        self.mainWidget.addWidget(self.integralPage)
        self.bernuliPage = QWidget()
        self.bernuliPage.setObjectName(u"bernuliPage")
        self.gridLayout_4 = QGridLayout(self.bernuliPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.calculateBernuliBtn = QPushButton(self.bernuliPage)
        self.calculateBernuliBtn.setObjectName(u"calculateBernuliBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calculateBernuliBtn.sizePolicy().hasHeightForWidth())
        self.calculateBernuliBtn.setSizePolicy(sizePolicy4)
        self.calculateBernuliBtn.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setBold(True)
        self.calculateBernuliBtn.setFont(font)

        self.gridLayout_4.addWidget(self.calculateBernuliBtn, 2, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.bernuliParamsLabel = QLabel(self.bernuliPage)
        self.bernuliParamsLabel.setObjectName(u"bernuliParamsLabel")
        self.bernuliParamsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.bernuliParamsLabel)

        self.bernuliParamsLine = QLineEdit(self.bernuliPage)
        self.bernuliParamsLine.setObjectName(u"bernuliParamsLine")

        self.verticalLayout_6.addWidget(self.bernuliParamsLine)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.choiceTypeLabel = QLabel(self.bernuliPage)
        self.choiceTypeLabel.setObjectName(u"choiceTypeLabel")

        self.verticalLayout_3.addWidget(self.choiceTypeLabel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bernuliFormulaType = QListWidget(self.bernuliPage)
        QListWidgetItem(self.bernuliFormulaType)
        QListWidgetItem(self.bernuliFormulaType)
        QListWidgetItem(self.bernuliFormulaType)
        QListWidgetItem(self.bernuliFormulaType)
        self.bernuliFormulaType.setObjectName(u"bernuliFormulaType")

        self.verticalLayout_2.addWidget(self.bernuliFormulaType)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.photoBernuliFirstFormulaType1 = QLabel(self.bernuliPage)
        self.photoBernuliFirstFormulaType1.setObjectName(u"photoBernuliFirstFormulaType1")
        self.photoBernuliFirstFormulaType1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.photoBernuliFirstFormulaType1)

        self.bernuliDescription = QLabel(self.bernuliPage)
        self.bernuliDescription.setObjectName(u"bernuliDescription")
        self.bernuliDescription.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.bernuliDescription)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.bernuliAnswerLabel = QLabel(self.bernuliPage)
        self.bernuliAnswerLabel.setObjectName(u"bernuliAnswerLabel")
        self.bernuliAnswerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.bernuliAnswerLabel)

        self.bernuliAnswerLine = QLineEdit(self.bernuliPage)
        self.bernuliAnswerLine.setObjectName(u"bernuliAnswerLine")
        self.bernuliAnswerLine.setAlignment(Qt.AlignCenter)
        self.bernuliAnswerLine.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.bernuliAnswerLine)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.bernuliLabel = QLabel(self.bernuliPage)
        self.bernuliLabel.setObjectName(u"bernuliLabel")
        self.bernuliLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.bernuliLabel, 0, 0, 1, 1)

        self.mainWidget.addWidget(self.bernuliPage)

        self.gridLayout_3.addWidget(self.mainWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.mainBody, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0435\u0439 - \u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21163", None))
        self.choiceLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u043e\u0440\u043c\u0443\u043b\u044b:", None))
        self.bernuliBtn.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0443\u043b\u0430 \u0411\u0435\u0440\u043d\u0443\u043b\u043b\u0438", None))
        self.polynomBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0438\u043d\u043e\u043c\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None))
        self.integralBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043e\u0440\u0435\u043c\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21163", None))
        self.polynomLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u043c\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u0430", None))
        self.photoPolynomFormula.setText(QCoreApplication.translate("MainWindow", u"photoPolynomFormula", None))
        self.pParamsLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u0438 p:", None))
        self.polynomAnswerLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.nParamLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 n:", None))
        self.mParamsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435 m:", None))
        self.calculatePolynomBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.polynomDescription.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.photoIntegralFormula1.setText(QCoreApplication.translate("MainWindow", u"photoIntegralFormula1", None))
        self.photoIntegralFormula2.setText(QCoreApplication.translate("MainWindow", u"photoIntegralFormula2", None))
        self.photoIntegralFormula3.setText(QCoreApplication.translate("MainWindow", u"photoIntegralFormula3", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0433\u0440\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043e\u0440\u0435\u043c\u0430 \u041c\u0443\u0430\u0432\u0440\u0430-\u041b\u0430\u043f\u043b\u0430\u0441\u0430", None))
        self.nNumberLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b (p, n, m1, m2)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 x1 =", None))
        self.x1ResultLabel.setText("")
        self.x2TextLabel.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 x2 = ", None))
        self.x2ResultLabel.setText("")
        self.integralAnswerLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.calculateIntegralBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
        self.calculateBernuliBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.bernuliParamsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b (p, n, m1, m2)", None))
        self.choiceTypeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u043e\u0431\u044b\u0442\u0438\u044f:", None))

        __sortingEnabled = self.bernuliFormulaType.isSortingEnabled()
        self.bernuliFormulaType.setSortingEnabled(False)
        ___qlistwidgetitem = self.bernuliFormulaType.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"k = m1", None));
        ___qlistwidgetitem1 = self.bernuliFormulaType.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"k<m1", None));
        ___qlistwidgetitem2 = self.bernuliFormulaType.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"k >=m1", None));
        ___qlistwidgetitem3 = self.bernuliFormulaType.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"m1<=k<=m2", None));
        self.bernuliFormulaType.setSortingEnabled(__sortingEnabled)

        self.photoBernuliFirstFormulaType1.setText(QCoreApplication.translate("MainWindow", u"photoBernuliFormulaType1", None))
        self.bernuliDescription.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bernuliAnswerLabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.bernuliAnswerLine.setInputMask("")
        self.bernuliLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0443\u043b\u0430 \u0411\u0435\u0440\u043d\u0443\u043b\u043b\u0438", None))
    # retranslateUi

