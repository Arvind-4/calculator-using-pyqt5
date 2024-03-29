import sys
import math
import pathlib
from PyQt5 import QtCore, QtGui, QtWidgets

BASE_DIR = pathlib.Path(__file__).parent
ICON_DIR = BASE_DIR / "icons"
ICON_FILE = ICON_DIR / "logo.png"

class UiDialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 417)
        Dialog.setMaximumSize(QtCore.QSize(391, 417))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(ICON_FILE)))
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 61))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 127);\n"
                                    "font: 75 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 80, 371, 321))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonOpenBrackets = QtWidgets.QPushButton(self.widget)
        self.pushButtonOpenBrackets.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonOpenBrackets.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                  "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonOpenBrackets.setObjectName("pushButtonOpenBrackets")
        self.gridLayout_2.addWidget(self.pushButtonOpenBrackets, 4, 2, 1, 1)
        self.pushButtonCloseBracket = QtWidgets.QPushButton(self.widget)
        self.pushButtonCloseBracket.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCloseBracket.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                  "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCloseBracket.setObjectName("pushButtonCloseBracket")
        self.gridLayout_2.addWidget(self.pushButtonCloseBracket, 5, 2, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.widget)
        self.pushButton9.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton9.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout_2.addWidget(self.pushButton9, 2, 2, 1, 1)
        self.pushButtonSquareroot = QtWidgets.QPushButton(self.widget)
        self.pushButtonSquareroot.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonSquareroot.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonSquareroot.setObjectName("pushButtonSquareroot")
        self.gridLayout_2.addWidget(self.pushButtonSquareroot, 2, 5, 1, 1)
        self.pushButtonXPowerY = QtWidgets.QPushButton(self.widget)
        self.pushButtonXPowerY.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonXPowerY.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                             "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonXPowerY.setObjectName("pushButtonXPowerY")
        self.gridLayout_2.addWidget(self.pushButtonXPowerY, 4, 5, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.widget)
        self.pushButton4.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton4.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout_2.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButtonAdddition = QtWidgets.QPushButton(self.widget)
        self.pushButtonAdddition.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonAdddition.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                               "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonAdddition.setObjectName("pushButtonAdddition")
        self.gridLayout_2.addWidget(self.pushButtonAdddition, 0, 3, 1, 1)
        self.pushButtonCube = QtWidgets.QPushButton(self.widget)
        self.pushButtonCube.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCube.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                          "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCube.setObjectName("pushButtonCube")
        self.gridLayout_2.addWidget(self.pushButtonCube, 1, 5, 1, 1)
        self.pushButtonClear = QtWidgets.QPushButton(self.widget)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonClear.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                           "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout_2.addWidget(self.pushButtonClear, 3, 0, 1, 1)
        self.pushButtonSquare = QtWidgets.QPushButton(self.widget)
        self.pushButtonSquare.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonSquare.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                            "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonSquare.setObjectName("pushButtonSquare")
        self.gridLayout_2.addWidget(self.pushButtonSquare, 0, 5, 1, 1)
        self.pushButtonDecimal = QtWidgets.QPushButton(self.widget)
        self.pushButtonDecimal.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonDecimal.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                             "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonDecimal.setObjectName("pushButtonDecimal")
        self.gridLayout_2.addWidget(self.pushButtonDecimal, 3, 2, 1, 1)
        self.pushButtonEulervalue = QtWidgets.QPushButton(self.widget)
        self.pushButtonEulervalue.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonEulervalue.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonEulervalue.setObjectName("pushButtonEulervalue")
        self.gridLayout_2.addWidget(self.pushButtonEulervalue, 3, 4, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.widget)
        self.pushButton0.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton0.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout_2.addWidget(self.pushButton0, 3, 1, 1, 1)
        self.pushButtonDivision = QtWidgets.QPushButton(self.widget)
        self.pushButtonDivision.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonDivision.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                              "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonDivision.setObjectName("pushButtonDivision")
        self.gridLayout_2.addWidget(self.pushButtonDivision, 3, 3, 1, 1)
        self.pushButtonCuberoot = QtWidgets.QPushButton(self.widget)
        self.pushButtonCuberoot.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCuberoot.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                              "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCuberoot.setObjectName("pushButtonCuberoot")
        self.gridLayout_2.addWidget(self.pushButtonCuberoot, 3, 5, 1, 1)
        self.pushButtonFactorial = QtWidgets.QPushButton(self.widget)
        self.pushButtonFactorial.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonFactorial.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                               "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonFactorial.setObjectName("pushButtonFactorial")
        self.gridLayout_2.addWidget(self.pushButtonFactorial, 1, 4, 1, 1)
        self.pushButtonSubtract = QtWidgets.QPushButton(self.widget)
        self.pushButtonSubtract.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonSubtract.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                              "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.gridLayout_2.addWidget(self.pushButtonSubtract, 1, 3, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.widget)
        self.pushButton6.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton6.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout_2.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.widget)
        self.pushButton5.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton5.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout_2.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.widget)
        self.pushButton1.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton1.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout_2.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.pushButtonModulus = QtWidgets.QPushButton(self.widget)
        self.pushButtonModulus.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonModulus.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                             "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonModulus.setObjectName("pushButtonModulus")
        self.gridLayout_2.addWidget(self.pushButtonModulus, 0, 4, 1, 1)
        self.pushButton2 = QtWidgets.QPushButton(self.widget)
        self.pushButton2.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton2.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout_2.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.widget)
        self.pushButton3.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton3.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout_2.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.pushButton10PowerX = QtWidgets.QPushButton(self.widget)
        self.pushButton10PowerX.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton10PowerX.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                              "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton10PowerX.setObjectName("pushButton10PowerX")
        self.gridLayout_2.addWidget(self.pushButton10PowerX, 4, 4, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.widget)
        self.pushButton7.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton7.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout_2.addWidget(self.pushButton7, 2, 0, 1, 1)
        self.pushButtonSin = QtWidgets.QPushButton(self.widget)
        self.pushButtonSin.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonSin.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonSin.setObjectName("pushButtonSin")
        self.gridLayout_2.addWidget(self.pushButtonSin, 5, 3, 1, 1)
        self.pushButtonTan = QtWidgets.QPushButton(self.widget)
        self.pushButtonTan.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonTan.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonTan.setObjectName("pushButtonTan")
        self.gridLayout_2.addWidget(self.pushButtonTan, 5, 5, 1, 1)
        self.pushButtonCos = QtWidgets.QPushButton(self.widget)
        self.pushButtonCos.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCos.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCos.setObjectName("pushButtonCos")
        self.gridLayout_2.addWidget(self.pushButtonCos, 5, 4, 1, 1)
        self.pushButtonCot = QtWidgets.QPushButton(self.widget)
        self.pushButtonCot.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCot.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCot.setObjectName("pushButtonCot")
        self.gridLayout_2.addWidget(self.pushButtonCot, 6, 5, 1, 1)
        self.pushButtonMultiplication = QtWidgets.QPushButton(self.widget)
        self.pushButtonMultiplication.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonMultiplication.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                    "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonMultiplication.setObjectName("pushButtonMultiplication")
        self.gridLayout_2.addWidget(self.pushButtonMultiplication, 2, 3, 1, 1)
        self.pushButtonEulerPowerX = QtWidgets.QPushButton(self.widget)
        self.pushButtonEulerPowerX.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonEulerPowerX.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                                 "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonEulerPowerX.setObjectName("pushButtonEulerPowerX")
        self.gridLayout_2.addWidget(self.pushButtonEulerPowerX, 4, 3, 1, 1)
        self.pushButtonCosec = QtWidgets.QPushButton(self.widget)
        self.pushButtonCosec.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonCosec.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                           "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonCosec.setObjectName("pushButtonCosec")
        self.gridLayout_2.addWidget(self.pushButtonCosec, 6, 3, 1, 1)
        self.pushButton00 = QtWidgets.QPushButton(self.widget)
        self.pushButton00.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton00.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton00.setObjectName("pushButton00")
        self.gridLayout_2.addWidget(self.pushButton00, 4, 0, 1, 1)
        self.pushButtonBackspace = QtWidgets.QPushButton(self.widget)
        self.pushButtonBackspace.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonBackspace.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                               "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonBackspace.setObjectName("pushButtonBackspace")
        self.gridLayout_2.addWidget(self.pushButtonBackspace, 4, 1, 1, 1)
        self.pushButtonLog = QtWidgets.QPushButton(self.widget)
        self.pushButtonLog.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonLog.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonLog.setObjectName("pushButtonLog")
        self.gridLayout_2.addWidget(self.pushButtonLog, 6, 2, 1, 1)
        self.pushButtonPi = QtWidgets.QPushButton(self.widget)
        self.pushButtonPi.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonPi.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonPi.setObjectName("pushButtonPi")
        self.gridLayout_2.addWidget(self.pushButtonPi, 2, 4, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.widget)
        self.pushButton8.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButton8.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                       "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout_2.addWidget(self.pushButton8, 2, 1, 1, 1)
        self.pushButtonSec = QtWidgets.QPushButton(self.widget)
        self.pushButtonSec.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonSec.setStyleSheet("background-color:rgb(255, 170, 0);\n"
                                         "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonSec.setObjectName("pushButtonSec")
        self.gridLayout_2.addWidget(self.pushButtonSec, 6, 4, 1, 1)
        self.pushButtonEqual = QtWidgets.QPushButton(self.widget)
        self.pushButtonEqual.setMaximumSize(QtCore.QSize(123, 51))
        self.pushButtonEqual.setStyleSheet("background-color:rgb(85, 255, 127);\n"
                                           "font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonEqual.setObjectName("pushButtonEqual")
        self.gridLayout_2.addWidget(self.pushButtonEqual, 5, 0, 2, 2)
        self.pushButtonEqual.raise_()
        self.pushButton4.raise_()
        self.pushButton5.raise_()
        self.pushButton6.raise_()
        self.pushButtonSubtract.raise_()
        self.pushButtonFactorial.raise_()
        self.pushButtonCube.raise_()
        self.pushButton7.raise_()
        self.pushButton8.raise_()
        self.pushButton9.raise_()
        self.pushButtonMultiplication.raise_()
        self.pushButtonPi.raise_()
        self.pushButtonSquareroot.raise_()
        self.pushButtonOpenBrackets.raise_()
        self.pushButtonCloseBracket.raise_()
        self.pushButton00.raise_()
        self.pushButtonBackspace.raise_()
        self.pushButtonCosec.raise_()
        self.pushButtonSec.raise_()
        self.pushButtonCot.raise_()
        self.pushButtonEulerPowerX.raise_()
        self.pushButton10PowerX.raise_()
        self.pushButtonXPowerY.raise_()
        self.pushButtonTan.raise_()
        self.pushButtonSin.raise_()
        self.pushButtonCos.raise_()
        self.pushButtonLog.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton1.clicked.connect(self.Method1)
        self.pushButton2.clicked.connect(self.Method2)
        self.pushButton3.clicked.connect(self.Method3)
        self.pushButton4.clicked.connect(self.Method4)
        self.pushButton5.clicked.connect(self.Method5)
        self.pushButton6.clicked.connect(self.Method6)
        self.pushButton7.clicked.connect(self.Method7)
        self.pushButton8.clicked.connect(self.Method8)
        self.pushButton9.clicked.connect(self.Method9)
        self.pushButton0.clicked.connect(self.Method0)
        self.pushButton00.clicked.connect(self.Method00)
        self.pushButtonAdddition.clicked.connect(self.MethodAddition)
        self.pushButtonSubtract.clicked.connect(self.MethodSubtraction)
        self.pushButtonMultiplication.clicked.connect(self.MethodMultiplication)
        self.pushButtonDivision.clicked.connect(self.MethodDivision)
        self.pushButtonModulus.clicked.connect(self.MethodModule)
        self.pushButtonFactorial.clicked.connect(self.MethodFactorial)
        self.pushButtonPi.clicked.connect(self.MethodPi)
        self.pushButtonEulervalue.clicked.connect(self.MethodE)
        self.pushButtonEulerPowerX.clicked.connect(self.MethodEPowerX)
        self.pushButton10PowerX.clicked.connect(self.Method10PowerX)
        self.pushButtonSquare.clicked.connect(self.MethodSquare)
        self.pushButtonCube.clicked.connect(self.MethodCube)
        self.pushButtonCuberoot.clicked.connect(self.MethodCubeRoot)
        self.pushButtonSquareroot.clicked.connect(self.MethodSquareRoot)
        self.pushButtonSin.clicked.connect(self.MethodSin)
        self.pushButtonCos.clicked.connect(self.MethodCos)
        self.pushButtonTan.clicked.connect(self.MethodTan)
        self.pushButtonCosec.clicked.connect(self.MethodCosec)
        self.pushButtonSec.clicked.connect(self.MethodSec)
        self.pushButtonCot.clicked.connect(self.MethodCot)
        self.pushButtonDecimal.clicked.connect(self.MethodDot)
        self.pushButtonCloseBracket.clicked.connect(self.MethodCloseBracket)
        self.pushButtonOpenBrackets.clicked.connect(self.MethodOpenBracket)
        self.pushButtonBackspace.clicked.connect(self.MethodBackSpace)
        self.pushButtonClear.clicked.connect(self.MethodAllClear)
        self.pushButtonLog.clicked.connect(self.MethodLog)
        self.pushButtonXPowerY.clicked.connect(self.MethodXPowerY)
        self.pushButtonEqual.clicked.connect(self.MethodEqual)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.pushButtonOpenBrackets.setText(_translate("Dialog", "("))
        self.pushButtonCloseBracket.setText(_translate("Dialog", ")"))
        self.pushButton9.setText(_translate("Dialog", "9"))
        self.pushButtonSquareroot.setText(_translate("Dialog", "√"))
        self.pushButtonXPowerY.setText(_translate("Dialog", "x^y"))
        self.pushButton4.setText(_translate("Dialog", "4"))
        self.pushButtonAdddition.setText(_translate("Dialog", "+"))
        self.pushButtonCube.setText(_translate("Dialog", "x³"))
        self.pushButtonClear.setText(_translate("Dialog", "AC"))
        self.pushButtonSquare.setText(_translate("Dialog", "x²"))
        self.pushButtonDecimal.setText(_translate("Dialog", "."))
        self.pushButtonEulervalue.setText(_translate("Dialog", "e"))
        self.pushButton0.setText(_translate("Dialog", "0"))
        self.pushButtonDivision.setText(_translate("Dialog", "÷"))
        self.pushButtonCuberoot.setText(_translate("Dialog", "∛"))
        self.pushButtonFactorial.setText(_translate("Dialog", "x!"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButton6.setText(_translate("Dialog", "6"))
        self.pushButton5.setText(_translate("Dialog", "5"))
        self.pushButton1.setText(_translate("Dialog", "1"))
        self.pushButtonModulus.setText(_translate("Dialog", "%"))
        self.pushButton2.setText(_translate("Dialog", "2"))
        self.pushButton3.setText(_translate("Dialog", "3"))
        self.pushButton10PowerX.setText(_translate("Dialog", "10^x"))
        self.pushButton7.setText(_translate("Dialog", "7"))
        self.pushButtonSin.setText(_translate("Dialog", "sin"))
        self.pushButtonTan.setText(_translate("Dialog", "tan"))
        self.pushButtonCos.setText(_translate("Dialog", "cos"))
        self.pushButtonCot.setText(_translate("Dialog", "cot"))
        self.pushButtonMultiplication.setText(_translate("Dialog", "×"))
        self.pushButtonEulerPowerX.setText(_translate("Dialog", "e^x"))
        self.pushButtonCosec.setText(_translate("Dialog", "cosec"))
        self.pushButton00.setText(_translate("Dialog", "00"))
        self.pushButtonBackspace.setText(_translate("Dialog", "←"))
        self.pushButtonLog.setText(_translate("Dialog", "log"))
        self.pushButtonPi.setText(_translate("Dialog", "π"))
        self.pushButton8.setText(_translate("Dialog", "8"))
        self.pushButtonSec.setText(_translate("Dialog", "sec"))
        self.pushButtonEqual.setText(_translate("Dialog", "="))

    def Method1(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '1')

    def Method2(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '2')

    def Method3(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '3')

    def Method4(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '4')

    def Method5(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '5')

    def Method6(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '6')

    def Method7(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '7')

    def Method8(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '8')

    def Method9(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '9')

    def Method0(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '0')

    def Method00(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '00')

    def MethodAddition(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '+')

    def MethodSubtraction(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '-')

    def MethodMultiplication(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '*')

    def MethodDivision(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '/')

    def MethodModule(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '%')

    def MethodFactorial(self):
        text = self.lineEdit.text()
        Answer = math.gamma(float(text) + 1)
        self.lineEdit.setText(str(Answer))

    def MethodPi(self):
        text = self.lineEdit.text()
        Answer = math.pi
        self.lineEdit.setText(text + str(Answer))

    def MethodE(self):
        text = self.lineEdit.text()
        Answer = math.e
        self.lineEdit.setText(text + str(Answer))

    def MethodEPowerX(self):
        text = self.lineEdit.text()
        Answer = math.pow(math.e, float(text))
        self.lineEdit.setText(str(Answer))

    def Method10PowerX(self):
        text = self.lineEdit.text()
        Answer = math.pow(10, float(text))
        self.lineEdit.setText(str(Answer))

    def MethodSquare(self):
        text = self.lineEdit.text()
        Answer = math.pow(float(text), 2)
        self.lineEdit.setText(str(Answer))

    def MethodCube(self):
        text = self.lineEdit.text()
        Answer = math.pow(float(text), 3)
        self.lineEdit.setText(str(Answer))

    def MethodSquareRoot(self):
        text = self.lineEdit.text()
        Answer = math.sqrt(float(text))
        self.lineEdit.setText(str(Answer))

    def MethodCubeRoot(self):
        text = self.lineEdit.text()
        Answer = math.pow(float(text), 1 / 3)
        self.lineEdit.setText(str(Answer))

    def MethodXPowerY(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '**')

    def MethodSin(self):
        text = self.lineEdit.text()
        Answer = math.sin(float(text))
        self.lineEdit.setText(str(Answer))

    def MethodCos(self):
        text = self.lineEdit.text()
        Answer = math.cos(float(text))
        self.lineEdit.setText(str(Answer))

    def MethodTan(self):
        text = self.lineEdit.text()
        Answer = math.tan(float(text))
        self.lineEdit.setText(str(Answer))

    def MethodCosec(self):
        text = self.lineEdit.text()
        Answer = 1 / (math.sin(float(text)))
        self.lineEdit.setText(str(Answer))

    def MethodSec(self):
        text = self.lineEdit.text()
        Answer = 1 / (math.cos(float(text)))
        self.lineEdit.setText(str(Answer))

    def MethodCot(self):
        text = self.lineEdit.text()
        Answer = 1 / (math.tan(float(text)))
        self.lineEdit.setText(str(Answer))

    def MethodLog(self):
        text = self.lineEdit.text()
        Answer = math.log(float(text))
        self.lineEdit.setText(str(Answer))

    def MethodOpenBracket(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '(')

    def MethodCloseBracket(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + ')')

    def MethodDot(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '.')

    def MethodAllClear(self):
        self.lineEdit.setText('')

    def MethodBackSpace(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text[:len(text) - 1])

    def MethodEqual(self):
        text = self.lineEdit.text()
        self.Ans = eval(text)
        try:
            self.lineEdit.setText(str(self.Ans))
        except:
            self.lineEdit.setText("Error")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    