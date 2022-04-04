from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.parse import urlparse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 138)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(135, 100, 140, 30))
        qPushButtonStyleSheet = """
        QPushButton {
		    background-color: white;
		    color: black;
		    border: 2px solid #8A2BE2;
		    transition-duration: 0.4s
        }
        QPushButton:hover:!pressed {
 		    background-color: #8A2BE2;
		    color: white;
        }"""
        self.generateButton.setStyleSheet(qPushButtonStyleSheet)
        self.generateButton.setObjectName("generateButton")
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(90, 70, 300, 20))
        self.linePassword.setObjectName("linePassword")
        self.lineURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineURL.setGeometry(QtCore.QRect(90, 40, 300, 20))
        self.lineURL.setObjectName("lineURL")
        self.lineURL.setText("https://google.com/")
        self.linePasswordMask = QtWidgets.QLineEdit(self.centralwidget)
        self.linePasswordMask.setGeometry(QtCore.QRect(90, 10, 300, 20))
        self.linePasswordMask.setObjectName("linePasswordMask")
        self.linePasswordMask.setText("!@dts_")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "giveMePassword"))
        self.generateButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.label_2.setText(_translate("MainWindow", "URL"))
        self.label.setText(_translate("MainWindow", "Маска пароля"))
        self.generateButton.clicked.connect(self.generatePassword)

    def deleteVowels(self, domainString):
        for i in "aeiouAEIOU.":
            domainString = domainString.replace(i, "")
        return domainString

    def generatePassword(self):
        stringURL = self.lineURL.text()
        passwordMask = self.linePasswordMask.text()
        errorMessageLines = ['Для продолжения необходимо заполнить:']
        if not stringURL:
            errorMessageLines.append("URL")
        if not passwordMask:
            errorMessageLines.append("Маска пароля")
        errorMessage = '\n'.join(errorMessageLines)
        errorMessageRowsCount = errorMessage.count('\n')
        if errorMessageRowsCount > 0:
            print(errorMessage)
        else:
            domain = urlparse(stringURL).netloc
            domainEdited = self.deleteVowels(domain)
            passwordTemplate = "{0}_{1}{2}{3}".format(len(domainEdited), passwordMask, len(domain), domainEdited.upper())
            self.linePassword.setText(passwordTemplate)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())