import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
import requests

class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Chatbot")
        self.setGeometry(100,100,400, 300)

        # Set up the layout
        self.layout = QVBoxLayout()

        # Set up the input box
        self.input_box = QTextEdit(self)
        self.input_box.setPlaceholderText("Type your question here...")
        self.layout.addWidget(self.input_box)

        # Set up the submit button
        self.submit_button = QPushButton("Ask", self)
        self.submit_button.clicked.connect(self.get_response)
        self.layout.addWidget(self.submit_button)

        # Set up the output area
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.layout.addWidget(self.output_area)


        # Set layout
        self.setLayout(self.layout)

    def get_response(self):
        user_input = self.input_box.toPlainText()

        # Simulate a response (replace with actual API to your Flask app)
        response = requests.post('http://127.0.0.1:5000/chatbot', json={"message": user_input})

        response_data = response.json().get("response", "No response")

        # Display the response
        self.output_area.setText(response_data)

# Run the application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = ChatbotGUI()
    chatbot.show()
    sys.exit(app.exec_())
    

