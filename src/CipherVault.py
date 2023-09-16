# This is a program to encrypt/decrypt a message using several ciphers.

import morse_code
import file_operations
import email_operations
import vigenere_cipher
import rail_fence
import caeser_cipher
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

def run_program(FirstTime):
    if FirstTime :
        print("Hi, this is CipherVault! \nI can help you encrypt/decrypt any message you want.")
        print("First, use how do you want to enter your message?")

    message = enter_text()
    while True:
        programType = input("Encrypt or Decrypt?(E or D): ")
        if programType == 'E' or programType == 'D':
            break
        else:
            print("Invalid input, please try again.")
    while True:
        cipherType = input("Enter which cipher you want to code into:(C,V,R,M) ")
        if cipherType == 'C' or cipherType == 'V' or cipherType == 'R' or cipherType == 'M':
            break
        else:
            print("Invalid input, please try again.")
    if cipherType == 'C':
        result = caeser_cipher.caeserCipher(message,programType)
        print("Your possible shifts are: ", result)
        if input("Save it to a file?(Y or N): ") == 'Y':
            file_operations.save_message_to_file(result,'Caeser Cipher.txt')
        FirstTime = False
        run_program(FirstTime)
        
    elif cipherType == 'V':
        if programType == 'E':
            while True:
                if input("Use a random key?(Y or N): ") == 'Y':
                    key = vigenere_cipher.generate_random_key(4,8)
                    print("Your key is: ",key)
                    break
                elif input("Use a random key?(Y or N): ") == 'N':
                    key = input("Enter the keyword: ")
                    break
                else:
                    print("Error!, try again.")
                
            result = vigenere_cipher.vigenere_encrypt(message, key)
            print("Your message is: ", result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Vigenere Cipher.txt')
        else:
            while True:
                key = input("Enter the keyword: ")
                if key == '':
                    print("Empty can't be a key, Please try again.")
                else:
                    break
            result = vigenere_cipher.vigenere_decrypt(message, key)
            print('Your message is: ', result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Vigenere Cipher.txt')
        FirstTime = False
        run_program(FirstTime)
    elif cipherType == 'R':
        while True:
            try:
                key = int(input("Please enter the number of lines (Only integer): "))
                break
            except ValueError:
                print("That is not an integer. Please try again.")
        if programType == 'E':
            result = rail_fence.Railfencecipher(message, key)
            print('Your message is: ', result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Rail-Fence Cipher.txt')
        else:
            result = rail_fence.Rail_fence_decipher(message, key)
            print('Your message is: ', result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Rail-Fence Cipher.txt')
        FirstTime = False
        run_program(FirstTime)
    elif cipherType == 'M':
        if programType == 'E':
            result = morse_code.morse_code_cipher(message)
            print('Your message is: ', result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Morse code.txt')
        else:
            result = morse_code.morse_code_decipher(message)
            print('Your message is: ', result)
            if input("Save it to a file?(Y or N): ") == 'Y':
                file_operations.save_message_to_file(result,'Morse code.txt')
        FirstTime = False
        run_program(FirstTime)


def enter_text():
    # Make sure the input is always 1 or 2
    while True:
        method = input("Enter '1' for typing directly through the program, Enter '2' for loading it from a file: ")
        if method != '1' and method != '2':
            print("Invalid Input!")
        else:
            break
    if method == '1':     # Type input directly into the program
        message = input("Enter the message: ")
    elif method == '2':
        message = file_operations.read_message_from_file()

    if message == '':
        print("Your message is empty, Please try again.")
        enter_text()
    else:
        return message


def shift_text(message, shiftVal):
    shiftedMessage = ''
    for i in range(len(message)):
        if message[i].isupper():
            shiftedMessage += chr((ord(message[i]) - 65 + shiftVal)%26 + 65)
        elif message[i].islower():
            shiftedMessage += chr((ord(message[i]) - 97 + shiftVal)%26 + 97)
        else:
            shiftedMessage += message[i]
    return shiftedMessage


def show_error_message(message):
    error_dialog = QtWidgets.QMessageBox()
    error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
    error_dialog.setWindowTitle("Error")
    error_dialog.setText(message)
    error_dialog.exec_()


FirstTime = True
# run_program(FirstTime)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    def encrypt_button_clicked():
        selected_item = ui.comboBox.currentText()
        message_text = ui.message.toPlainText()
        if not message_text:
            QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Please enter a message to encrypt.")
            return
        if selected_item == "Caeser":
            ui.caeserDecryptButton.setVisible(True)
            shift_value = ui.lineEdit.text()
            if not shift_value or not shift_value.isdigit():
                QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Shift value must be an integer.")
                return
            shift_value = int(shift_value)
            encrypted_message = shift_text(message_text, shift_value)
            ui.result.setPlainText(encrypted_message)
        elif selected_item == "Vigenere":
            ui.caeserDecryptButton.setVisible(False)
            if ui.radioButton.isChecked():
                # key_length = int(ui.lineEdit_2.text())  # Get the length of the random key
                key_text = vigenere_cipher.generate_random_key(4, 8)  # Generate random key
                ui.randomKeyLabel.setText("Random Key: " + key_text)  # Set the text of the randomKeyLabel
                email = ui.emailLineEdit.text()
                
                if not email_operations.is_valid_email(email):
                    show_error_message("Invalid email address!")
                    return
                else:
                    email_operations.send_email(email, key_text)

            else:
                key_text = ui.lineEdit_2.text()  # Use the user-provided key
                if not key_text:
                    QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Please enter a key to use for encryption.")
                    return
                ui.randomKeyLabel.setText("")  # Clear the text of the randomKeyLabel

            encrypted_message = vigenere_cipher.vigenere_encrypt(message_text, key_text)
            ui.result.setPlainText(encrypted_message)
        elif selected_item == "Rail Fence":
            ui.caeserDecryptButton.setVisible(False)
            rail_fence_key = ui.lineEdit_3.text()
            if not rail_fence_key or not rail_fence_key.isdigit():
                QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Rails must be an integer.")
                return
            rail_fence_key = int(rail_fence_key)
            encrypted_message = rail_fence.Railfencecipher(message_text, rail_fence_key)
            ui.result.setPlainText(encrypted_message)
        elif selected_item == "Morse":
            ui.caeserDecryptButton.setVisible(False)
            encrypted_message = morse_code.morse_code_cipher(message_text)
            ui.result.setPlainText(encrypted_message)
    
    
    def decrypt_button_clicked():
        selected_item = ui.comboBox.currentText()
        message_text = ui.message.toPlainText()
        if not message_text:
            QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Please enter a message to decrypt.")
            return
        ui.caeserDecryptButton.setVisible(False)

        if selected_item == "Caeser":
            shift_value = ui.lineEdit.text()
            if not shift_value or not shift_value.isdigit():
                QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Shift value must be an integer.")
                return
            shift_value = int(shift_value)
            decrypted_message = shift_text(message_text, (shift_value*-1))
            ui.result.setPlainText(decrypted_message)
        elif selected_item == "Vigenere":
            key_text = ui.lineEdit_2.text()
            if not key_text:
                    QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Please enter a key to use for encryption.")
                    return
            ui.radioButton.setChecked(False)
            decrypted_message = vigenere_cipher.vigenere_decrypt(message_text, key_text)
            ui.result.setPlainText(decrypted_message)
        elif selected_item == "Rail Fence":
            rail_fence_key = ui.lineEdit_3.text()
            if not rail_fence_key or not rail_fence_key.isdigit():
                QtWidgets.QMessageBox.warning(MainWindow, "Invalid Input", "Rails must be an integer.")
                return
            rail_fence_key = int(rail_fence_key)
            decrypted_message = rail_fence.Rail_fence_decipher(message_text, rail_fence_key)
            ui.result.setPlainText(decrypted_message)
        elif selected_item == "Morse":
            decrypted_message = morse_code.morse_code_decipher(message_text)
            ui.result.setPlainText(decrypted_message)
    

    def handle_caeser_decrypt():
        message_text = ui.message.toPlainText()
        decrypted_message = ', '.join(caeser_cipher.automatic_caeser_decipher(message_text))
        ui.result.setPlainText(decrypted_message)

    ui.pushButton_3.clicked.connect(encrypt_button_clicked)
    ui.pushButton_4.clicked.connect(decrypt_button_clicked)
    ui.caeserDecryptButton.clicked.connect(handle_caeser_decrypt)
    MainWindow.show()
    sys.exit(app.exec_())