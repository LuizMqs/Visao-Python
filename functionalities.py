import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from interface import *
import model
import cv2


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = model.run(source=0, weights='runs/train/exp/weights/best.pt', conf_thres=0.8)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showVideo)
        self.timer.start(1)

        self.ui.securityAlertButton.clicked.connect(self.functionSecurtityAlarm)
        self.ui.schoolAlertButton.clicked.connect(self.functionSecurtitySchool)
        self.ui.PoliceAlertButton.clicked.connect(self.functionSecurtityPolice)
        self.ui.alertFinishButton.clicked.connect(self.functionFinish)
        self.ui.closedButton.clicked.connect(self.functionExit)
        self.ui.statusbar.children

        self.textInformAlert = ''
        self.gunDetection(False)

    @staticmethod
    def _convert_img_to_pixmap(img: QImage) -> QPixmap:
        """
        Static method that converts a QImage image to QPixmap.

        Args:
            img: QImage - Image to be converted.

        Returns:
            QPixmap: The converted image to QPixmap.
        """

        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_image.shape
        bytes_per_line = channel * width
        return QPixmap(QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888))

    @QtCore.pyqtSlot()
    def showVideo(self) -> None:
        """
        Method that displays the video on the application window.
        """

        pistol, frame = next(self.model)
        converted_frame = Tela._convert_img_to_pixmap(frame)
        if (len(pistol)):
            self.gunDetection(True)
        self.ui.labelVideo.setScaledContents(True)
        self.ui.labelVideo.setPixmap(converted_frame)

    # Botão de alarme da segurança
    @QtCore.pyqtSlot()
    def functionSecurtityAlarm(self) -> None:
        """
        Method that is called when the security alarm button is pressed.
        Disables the button and adds a message to the status bar.
        """

        # self.ui.activeAlarmWarning.setText('Alerta dos seguranças')
        self.ui.securityAlertButton.setEnabled(False)  # desabilitando o botão
        if self.textInformAlert == '':
            self.textInformAlert = 'Alerta enviado aos seguranças'
        else:
            self.textInformAlert += '\nAlerta enviado aos seguranças'
        return self.ui.activeAlarmWarning.setText(self.textInformAlert)

    # Botão de alarme da escola
    @QtCore.pyqtSlot()
    def functionSecurtitySchool(self) -> None:
        """
        Method that is called when the school alarm button is pressed.
        Disables the button and adds a message to the status bar.
        """

        # self.ui.activeAlarmWarning.setText('Alerta escolar')
        self.ui.schoolAlertButton.setEnabled(False)
        if self.textInformAlert == '':
            self.textInformAlert = 'Alerta escolar tocando'
        else:
            self.textInformAlert += '\nAlerta escolar tocando'
        return self.ui.activeAlarmWarning.setText(self.textInformAlert)

    # Botão de alarme da policia
    @QtCore.pyqtSlot()
    def functionSecurtityPolice(self) -> None:
        """
        Method that is called when the police alarm button is pressed.
        Disables the button and adds a message to the status bar.
        """

        # self.ui.activeAlarmWarning.setText('Alerta enviado a polícia')
        self.ui.PoliceAlertButton.setEnabled(False)
        if self.textInformAlert == '':
            self.textInformAlert = 'Alerta enviado a polícia'
        else:
            self.textInformAlert += '\nAlerta enviado a polícia'
        return self.ui.activeAlarmWarning.setText(self.textInformAlert)

    # Barra de informação sobre detecção
    @QtCore.pyqtSlot()
    def gunDetection(self, detectGun: bool) -> None:
        """
        Sets the display and style of the gun detection information bar based on the detection status.

        Args:
            detectGun (bool): A boolean indicating whether a gun has been detected or not.

        Returns:
            None
        """

        if detectGun == True:
            self.ui.detectArma.setText('ARMA DETECTADA!!!')
            self.ui.detectArma.setStyleSheet("font: 30pt \"MS Reference Sans Serif\";\n"
                                             "background-color: transparent;\n"
                                             "color: rgb(227, 0, 0);")
            self.ui.labelDetectArma.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                                  "border-color: rgba(170, 255, 255, 70);\n"
                                                  "border-style: solid;\n"
                                                  "border-width: 1px;")
        else:
            self.ui.detectArma.setText('Não foram encontrados sinais de armas')
            self.ui.detectArma.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";\n"
                                             "background-color: transparent;\n"
                                             "color: rgb(255, 255, 255);")
            self.ui.labelDetectArma.setStyleSheet("background-color: rgba(170, 255, 255, 20);\n"
                                                  "border-color: rgba(170, 255, 255, 70);\n"
                                                  "border-style: solid;\n"
                                                  "border-width: 1px;")

    # Botão que encerra os alarmes encaminhados
    @QtCore.pyqtSlot()
    def functionFinish(self) -> None:
        """
        Resets the warning information and enables the alarm buttons.

        Returns:
            None
        """

        self.ui.securityAlertButton.setEnabled(True)  # habilitando o botão
        self.ui.schoolAlertButton.setEnabled(True)
        self.ui.PoliceAlertButton.setEnabled(True)
        self.gunDetection(False)
        self.textInformAlert = ''
        return self.ui.activeAlarmWarning.setText(self.textInformAlert)

    # Botão de saida da aplicação
    @QtCore.pyqtSlot()
    def functionExit(self) -> None:
        """
        Closes the application.

        Returns:
            None
        """

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    istance = Tela()
    istance.show()
    sys.exit(app.exec_())
