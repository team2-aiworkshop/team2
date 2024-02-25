from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self, app, load_file_callback, generate_answer_callback):
        super(window, self).__init__(None)
        self.app = app

        # Create the window's layout
        self.win_layout = QVBoxLayout()

        # Create the question and answer text boxes
        self.question_text_box = QTextEdit()
        self.answer_text_box = QTextEdit()

        # Set the text boxes' info
        self.question_text_box.setPlaceholderText('Enter your question here')
        self.answer_text_box.setPlaceholderText('Your answer will appear here')
        self.answer_text_box.setReadOnly(True)

        # Create the generate answer button
        self.generate_answer_button = QPushButton('Generate')
        
        # Create the input file path text box and button
        self.file_layout = QHBoxLayout()
        self.path_select_button = QPushButton('...')
        self.path_text_box = QLineEdit()
        self.load_file_button = QPushButton('Load')

        # Set the button callbacks
        self.path_select_button.clicked.connect(lambda: self.path_text_box.setText(QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'Text files (*.txt)')[0]))
        self.generate_answer_button.clicked.connect(generate_answer_callback)
        self.load_file_button.clicked.connect(load_file_callback)

        # Add every component to its layout
        self.file_layout.addWidget(self.path_select_button)
        self.file_layout.addWidget(self.path_text_box)
        self.file_layout.addWidget(self.load_file_button)

        self.win_layout.addWidget(self.question_text_box)
        self.win_layout.addWidget(self.answer_text_box)
        self.win_layout.addWidget(self.generate_answer_button)
        self.win_layout.addSpacing(30)
        self.win_layout.addLayout(self.file_layout)

        # Set the window's layout and title
        self.setLayout(self.win_layout)
        self.setWindowTitle('EduPill Prototype')
    
    def get_question(self):
        return self.question_text_box.toPlainText()
    def set_answer(self, answer):
        self.answer_text_box.setText(answer)
    def set_load_button_loading(self):
        self.load_file_button.setText('Loading')
        self.load_file_button.setEnabled(False)
    def set_load_button_loaded(self):
        self.load_file_button.setText('Load')
        self.load_file_button.setEnabled(True)
    def get_file_path(self):
        return self.path_text_box.text()

class application:
    def __init__(self, args, load_file_callback, generate_answer_callback):
        # Create the Qt5 application and window
        self.app = QApplication(args)
        self.window = window(self.app, load_file_callback, generate_answer_callback)
    
    def get_window(self) -> window:
        return self.window
    def run(self):
        # Display the window and run the program
        self.window.show()
        return self.app.exec()
