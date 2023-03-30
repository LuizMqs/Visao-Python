# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Karol\Desktop\pyqt treining\testando3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 758)
        MainWindow.setStyleSheet("background-color: rgb(20, 20, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.alertFinishButton = QtWidgets.QPushButton(self.centralwidget)
        self.alertFinishButton.setGeometry(QtCore.QRect(700, 460, 141, 51))
        self.alertFinishButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgba(170, 0, 0, 75);\n"
                                             "border-color: rgba(170, 255, 255, 70);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-style: solid;\n"
                                             "border-width: 0.5px;")
        self.alertFinishButton.setCheckable(False)
        self.alertFinishButton.setAutoRepeat(False)
        self.alertFinishButton.setAutoExclusive(False)
        self.alertFinishButton.setAutoDefault(True)
        self.alertFinishButton.setObjectName("alertFinishButton")
        self.schoolAlertButton = QtWidgets.QPushButton(self.centralwidget)
        self.schoolAlertButton.setGeometry(QtCore.QRect(700, 110, 141, 61))
        self.schoolAlertButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgba(0, 0, 255, 75);\n"
                                             "border-color: rgba(170, 255, 255, 70);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-style: solid;\n"
                                             "border-width: 0.5px;")
        self.schoolAlertButton.setObjectName("schoolAlertButton")
        self.labelVideo = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo.setEnabled(True)
        self.labelVideo.setGeometry(QtCore.QRect(40, 30, 640, 480))
        self.labelVideo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-color: rgb(176, 176, 176);\n"
                                      "border-style: solid;\n"
                                      "border-width: 1px;")
        self.labelVideo.setObjectName("labelVideo")
        self.PoliceAlertButton = QtWidgets.QPushButton(self.centralwidget)
        self.PoliceAlertButton.setGeometry(QtCore.QRect(700, 190, 141, 61))
        self.PoliceAlertButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgba(0, 0, 255, 75);\n"
                                             "border-color: rgba(170, 255, 255, 70);\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "border-style: solid;\n"
                                             "border-width: 0.5px;")
        self.PoliceAlertButton.setObjectName("PoliceAlertButton")
        self.securityAlertButton = QtWidgets.QPushButton(self.centralwidget)
        self.securityAlertButton.setGeometry(QtCore.QRect(700, 30, 141, 61))
        self.securityAlertButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                               "background-color: rgba(0, 0, 255, 75);\n"
                                               "border-color: rgba(170, 255, 255, 70);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "border-style: solid;\n"
                                               "border-width: 0.5px;")
        self.securityAlertButton.setObjectName("securityAlertButton")
        self.labelDetectArma = QtWidgets.QLabel(self.centralwidget)
        self.labelDetectArma.setEnabled(False)
        self.labelDetectArma.setGeometry(QtCore.QRect(40, 530, 801, 81))
        self.labelDetectArma.setStyleSheet("background-color: rgba(170, 255, 255, 20);\n"
                                           "border-color: rgba(170, 255, 255, 70);\n"
                                           "border-style: solid;\n"
                                           "border-width: 1px;")
        self.labelDetectArma.setObjectName("labelDetectArma")
        self.detectArma = QtWidgets.QLabel(self.centralwidget)
        self.detectArma.setGeometry(QtCore.QRect(40, 529, 801, 81))
        self.detectArma.setStyleSheet("font: 22pt \"MS Reference Sans Serif\";\n"
                                      "background-color: transparent;\n"
                                      "color: rgb(255, 255, 255);")
        self.detectArma.setTextFormat(QtCore.Qt.AutoText)
        self.detectArma.setScaledContents(False)
        self.detectArma.setAlignment(QtCore.Qt.AlignCenter)
        self.detectArma.setWordWrap(False)
        self.detectArma.setIndent(8)
        self.detectArma.setOpenExternalLinks(False)
        self.detectArma.setObjectName("detectArma")
        self.alertActive = QtWidgets.QLabel(self.centralwidget)
        self.alertActive.setGeometry(QtCore.QRect(50, 630, 161, 31))
        self.alertActive.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";\n"
                                       "background-color: transparent;\n"
                                       "color: rgb(255, 255, 255);")
        self.alertActive.setObjectName("alertActive")
        self.activeAlarmWarning = QtWidgets.QLabel(self.centralwidget)
        self.activeAlarmWarning.setGeometry(QtCore.QRect(220, 630, 421, 71))
        self.activeAlarmWarning.setStyleSheet("font: 12pt \"MS Reference Sans Serif\";\n"
                                              "background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);")
        self.activeAlarmWarning.setText("")
        self.activeAlarmWarning.setObjectName("activeAlarmWarning")
        self.closedButton = QtWidgets.QPushButton(self.centralwidget)
        self.closedButton.setGeometry(QtCore.QRect(700, 650, 131, 51))
        self.closedButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgba(0, 0, 206, 25);\n"
                                        "border-color: rgba(170, 255, 255, 70);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: solid;\n"
                                        "border-width: 0.5px;")
        self.closedButton.setObjectName("closedButton")
        self.labelActiveAlarm = QtWidgets.QLabel(self.centralwidget)
        self.labelActiveAlarm.setEnabled(False)
        self.labelActiveAlarm.setGeometry(QtCore.QRect(40, 630, 631, 71))
        self.labelActiveAlarm.setStyleSheet("background-color: rgba(170, 255, 255, 20);\n"
                                            "border-color: rgba(170, 255, 255, 70);\n"
                                            "border-style: solid;\n"
                                            "border-width: 1px;")
        self.labelActiveAlarm.setObjectName("labelActiveAlarm")
        self.labelActiveAlarm.raise_()
        self.alertFinishButton.raise_()
        self.schoolAlertButton.raise_()
        self.labelVideo.raise_()
        self.PoliceAlertButton.raise_()
        self.securityAlertButton.raise_()
        self.labelDetectArma.raise_()
        self.detectArma.raise_()
        self.alertActive.raise_()
        self.activeAlarmWarning.raise_()
        self.closedButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.alertFinishButton.setText(_translate("MainWindow", "Encerrar alertas"))
        self.schoolAlertButton.setText(_translate("MainWindow", "Alerta - Escola"))
        self.labelVideo.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.PoliceAlertButton.setText(_translate("MainWindow", "Alerta - Polícia"))
        self.securityAlertButton.setText(_translate("MainWindow", "Alerta - Segurança"))
        self.labelDetectArma.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.detectArma.setText(_translate("MainWindow", "Nenhuma ameaça detectada"))
        self.alertActive.setText(_translate("MainWindow", "Alarmes ativos:"))
        self.closedButton.setText(_translate("MainWindow", "Fechar"))
        self.labelActiveAlarm.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
