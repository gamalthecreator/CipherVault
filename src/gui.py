from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.import_file)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.handle_export_file)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.copy_to_clipboard)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.frame, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 0, 1, 1, 1)
        self.result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.caeserPage = QtWidgets.QWidget()
        self.caeserPage.setObjectName("caeserPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.caeserPage)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.caeserPage)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.caeserPage)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.stackedWidget.addWidget(self.caeserPage)
        self.vigenerePage = QtWidgets.QWidget()
        self.vigenerePage.setObjectName("vigenerePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.vigenerePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.vigenerePage)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.vigenerePage)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.randomKeyLabel = QtWidgets.QLabel(self.vigenerePage)
        self.randomKeyLabel.setObjectName("randomKeyLabel")
        self.verticalLayout_2.addWidget(self.randomKeyLabel)
        self.radioButton = QtWidgets.QRadioButton(self.vigenerePage)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(False)
        self.radioButton.toggled.connect(self.handle_random_key_toggle)
        self.verticalLayout_2.addWidget(self.radioButton)
        
        # Add the new email label and text box
        self.emailLabel = QtWidgets.QLabel(self.vigenerePage)
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout_2.addWidget(self.emailLabel)
        self.emailLineEdit = QtWidgets.QLineEdit(self.vigenerePage)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.verticalLayout_2.addWidget(self.emailLineEdit)
        self.emailLabel.setVisible(False)
        self.emailLineEdit.setVisible(False)

        self.caeserDecryptButton = QtWidgets.QPushButton(self.vigenerePage)
        self.caeserDecryptButton.setObjectName("caeserDecryptButton")
        self.horizontalLayout_2.addWidget(self.caeserDecryptButton)
        self.caeserDecryptButton.setVisible(True)
        self.stackedWidget.addWidget(self.vigenerePage)
        self.railFencePage = QtWidgets.QWidget()
        self.railFencePage.setObjectName("railFencePage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.railFencePage)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.railFencePage)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.railFencePage)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.stackedWidget.addWidget(self.railFencePage)
        self.morsePage = QtWidgets.QWidget()
        self.morsePage.setObjectName("morsePage")
        self.stackedWidget.addWidget(self.morsePage)
        self.gridLayout.addWidget(self.stackedWidget, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.comboBox.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def handle_random_key_toggle(self, checked):
        if checked:
            self.randomKeyLabel.setVisible(True)
            self.caeserDecryptButton.setVisible(True)
        else:
            self.randomKeyLabel.setVisible(False)
            self.caeserDecryptButton.setVisible(True)
        
        # Show/hide the email label and text box based on the radio button state
        self.emailLabel.setVisible(checked)
        self.emailLineEdit.setVisible(checked)

    def copy_to_clipboard(self):
        result_text = self.result.toPlainText()  # Get the text from the result text box
        clipboard = QtWidgets.QApplication.clipboard()  # Get the clipboard
        clipboard.setText(result_text)  # Set the text to the clipboard


    def import_file(self):
        file_dialog = QtWidgets.QFileDialog()  # Create a file dialog instance
        file_path, _ = file_dialog.getOpenFileName(None, "Select File")  # Open the file dialog to select a file

        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.message.setPlainText(file_contents)  # Set the contents of the selected file in the message text field
    
    def handle_export_file(self):
        result_text = self.result.toPlainText()

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            "Save Result File",
            "",
            "Text Files (*.txt)",
            options=options
        )

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(result_text)
                QtWidgets.QMessageBox.information(
                    self.centralwidget,
                    "File Saved",
                    "The result file has been saved successfully."
                )
            except Exception as e:
                QtWidgets.QMessageBox.critical(
                    self.centralwidget,
                    "Error",
                    f"An error occurred while saving the file:\n{str(e)}"
                )



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CipherVault"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Caeser"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vigenere"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Rail Fence"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Morse"))
        self.pushButton_3.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_4.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton.setText(_translate("MainWindow", "Import file"))
        self.pushButton_5.setText(_translate("MainWindow", "Export file"))
        self.pushButton_2.setText(_translate("MainWindow", "Copy to Clipboard"))
        self.label.setText(_translate("MainWindow", "Message"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.label_3.setText(_translate("MainWindow", "Shift Value"))
        self.randomKeyLabel.setText(_translate("MainWindow", "Random Key"))
        self.radioButton.setText(_translate("MainWindow", "Use Random Key"))
        
        # Set the label and text for the email fields
        self.emailLabel.setText(_translate("MainWindow", "Your Email:"))
        self.caeserDecryptButton.setText(_translate("MainWindow", "Decrypt Automatically"))
        self.label_5.setText(_translate("MainWindow", "Rails"))
