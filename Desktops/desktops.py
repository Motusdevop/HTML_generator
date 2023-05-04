from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os

import html_gen

class Main(QWidget):

    def __init__(self):
        super().__init__()

        with open('Desktops/StyleSheets/Main.StyleSheet') as file:
            self.setStyleSheet(file.read())

        self.source = dict()

        self.lines = list()

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
        self.lines.append(QLineEdit(placeholderText="H1 tag"))
        self.lines.append(QPlainTextEdit(placeholderText="Paragraf text"))

        self.Btn_add_h1 = QPushButton(text="Add <h1> tag")
        self.Btn_add_p = QPushButton(text="Add <p> tag")
        self.Btn_add_h1.clicked.connect(self.add_H1)
        self.Btn_add_p.clicked.connect(self.add_p)

        self.Btn_commit = QPushButton(text="CREATE")
        self.Btn_commit.clicked.connect(self.commit)

        hl = QHBoxLayout()
        hl.addWidget(self.Btn_add_h1)
        hl.addWidget(self.Btn_add_p)

        self.vl = QVBoxLayout(self)
        self.vl2 = QVBoxLayout(self)

        self.vl2.addWidget(self.instr, alignment= Qt.AlignTop)
        self.vl2.addWidget(self.Name_line, alignment= Qt.AlignTop)
        self.vl2.addWidget(self.Title_line, alignment= Qt.AlignTop)

        for line in self.lines:
            self.vl2.addWidget(line, alignment= Qt.AlignTop)
        
        self.vl.addLayout(self.vl2)
        self.vl.addLayout(hl)

        self.vl.addWidget(self.Btn_commit, alignment=Qt.AlignCenter)
    
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
            self.source["Lines"] = self.lines

            html_gen.generate(self.source)

            self.surccesfully = Successfully(Doc_name)
        except FileNotFoundError as e:
            self.instr.setText("error")
            print(e)
    
    def add_H1(self):
        new = QLineEdit(placeholderText="H1 tag")
        self.lines.append(new)
        self.vl2.addWidget(new, alignment= Qt.AlignTop)
    
    def add_p(self):
        new = QPlainTextEdit(placeholderText="Paragraf text")
        self.lines.append(new)
        self.vl2.addWidget(new, alignment= Qt.AlignTop)
    
class Successfully(QWidget):

    def __init__(self, doc_name : str):
        super().__init__()
        
        with open(r"Desktops/StyleSheets/Successfully.StyleSheet") as file:
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
        self.text2 = QLabel("Reveal in " + r"HTML_generator/Results")
        self.href.setOpenExternalLinks(True)

        lay = QVBoxLayout(self)

        lay.addWidget(self.text, alignment=Qt.AlignCenter)
        lay.addWidget(self.href, alignment=Qt.AlignCenter)
        lay.addWidget(self.text2, alignment=Qt.AlignCenter)

        os.system(f"open {self.path}")
        
        
        
        