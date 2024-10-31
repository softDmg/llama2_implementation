# gui_functions.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from llama_gui import Ui_MainWindow
from Files.main import generate_response  # Import the function

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

        # Connect buttons to functions
        self.sendButton.clicked.connect(self.handle_send_button_click)

    def handle_send_button_click(self):
        user_input = self.input_field.text()
        if user_input:
            try:
                response = generate_response(user_input)
                if "error" in response:
                    raise ValueError(response["error"])
                # gui_functions.py
                self.responseField.append(f"<b><font color='blue'>Question:</font></b> {user_input}")
                self.responseField.append(f"<font face='Tahoma'>Response: {response['generated_text']}</font>")
                print("")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a question.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())