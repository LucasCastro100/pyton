# filepath: main.py
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("JANELA")  # Define o título da janela
window.setStyleSheet("background-color: rgba(0, 255, 0, 0.5);")  # Define a cor de fundo para verde

layout = QVBoxLayout()

label = QLabel("Hello, PySide6!")
button = QPushButton("Click me")

def on_button_clicked():
    label.setText("Button clicked!")

button.clicked.connect(on_button_clicked)

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()

app.exec()