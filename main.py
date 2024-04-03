from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from explanationComponent import ExplanationComponent
from inferenceEngine import InferenceEngine
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.explanationComponent = ExplanationComponent()
        self.again()
        self.pushButton.clicked.connect(self.further)
        self.pushButton_2.clicked.connect(self.again)

    def again(self):
        self.comboBox.clear()
        self.label.setText('')
        self.inferenceEngine = InferenceEngine()
        self.forward()
        self.textBrowser.clear()

    def dataRecording(self):
        userValue =  self.comboBox.currentText()
        self.inferenceEngine.set_user_answer(userValue)

    def forward(self):
        self.label.setText(self.inferenceEngine.question)
        self.comboBox.addItems(self.inferenceEngine.answers)

    def log(self):
        log = self.inferenceEngine.get_logs()
        self.textBrowser.clear()
        self.textBrowser.append(log)

    def further(self):#кнопка ДАЛЕЕ
        self.dataRecording()
        self.inferenceEngine.get_answer_question()
        self.comboBox.clear()
        self.log()
        if self.inferenceEngine.isAnswer: #если питомец найден
            print("Питомец найден")
            self.label.setText('')
            self.textBrowser.append(self.inferenceEngine.question)
        else:#если питомец еще не найден
            print("Питомец еще не найден")
            self.label.setText(self.inferenceEngine.question)
            self.forward()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 181, 701, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 120, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Следующий вопрос"))
        self.pushButton_2.setText(_translate("MainWindow", "Заново"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())