from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import html_gen

class Main(QWidget):

    def __init__(self):
        super().__init__()

        with open('Desktops/StyleSheets/Main.StyleSheet') as file:
            self.setStyleSheet(file.read())

        self.source = dict()

        self.Settings()
        self.initUi()
        self.show()
        
    def Settings(self):
        self.resize(500,300)
        self.setWindowTitle("Create HTML!")

    def initUi(self):
        self.instr = QLabel("Enter text in lines")
        self.Name_line = QLineEdit(placeholderText="Document Name")
        self.Title_line = QLineEdit(placeholderText="Title tag")
        self.H1_line = QLineEdit(placeholderText="H1 tag")
        self.p_line = QPlainTextEdit(placeholderText="Paragraf text")
        self.Btn_commit = QPushButton(text="CREATE")
        self.Btn_commit.clicked.connect(self.commit)

        vl = QVBoxLayout(self)

        vl.addWidget(self.instr)
        vl.addWidget(self.Name_line)
        vl.addWidget(self.Title_line)
        vl.addWidget(self.H1_line)
        vl.addWidget(self.p_line)

        vl.addWidget(self.Btn_commit, alignment=Qt.AlignCenter)
    
    def commit(self):
        try:
            Doc_name = self.Name_line.text().strip()
            new_word = list()
            for symbol in Doc_name:
                if symbol in (" ", "."):
                    symbol = '-'
                new_word.append(symbol)
            Doc_name = "".join(new_word)

            self.source["Doc_name"] = Doc_name
            self.source["Title"] = self.Title_line.text()
            self.source["h1"] = self.H1_line.text()
            self.source["p"] = self.p_line.toPlainText()

            html_gen.generate(self.source)

            self.surccesfully = Successfully(Doc_name)
        except FileNotFoundError as e:
            self.instr.setText("error")
            print(e)
    
class Successfully(QWidget):

    def __init__(self, doc_name : str):
        super().__init__()
        
        with open("Desktops/StyleSheets/Successfully.StyleSheet") as file:
            self.setStyleSheet(file.read())
        
        self.path = f"Results/{doc_name}.html"

        self.Settings()
        self.initUi()
        self.show()
    
    def Settings(self):
        self.resize(300, 200)

    def initUi(self):
        self.text = QLabel("Successfully!!!")
        self.href = QLabel(f'<a href="{self.path}" style="color: #008080"> Open to view!</a>')
        self.href.setOpenExternalLinks(True)

        lay = QVBoxLayout(self)

        lay.addWidget(self.text, alignment=Qt.AlignCenter)
        lay.addWidget(self.href, alignment=Qt.AlignCenter)


        
        
        
        