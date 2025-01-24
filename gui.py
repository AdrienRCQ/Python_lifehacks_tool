"""
Author: Adrien RICQUE
Version: 2.2
Creation Date: 23/07/2024

Update Date: 29/07/2024
Actor: Adrien RICQUE
"""

import sys
from re import match
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar, QLineEdit, QVBoxLayout, QWidget, QDialogButtonBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from excel_tools import create_excel, read_xlsx_file

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Tool")
        width = 500
        height = 200
        self.setFixedSize(width,height)

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("icons/home.png"), "Home", self)
        button_action.setStatusTip("Go back to Home page")
        button_action.triggered.connect(self.show_homepage)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        self.setStatusBar(QStatusBar(self))

    def show_homepage(self, checked):
        self.w = HomePage()
        self.w.show()
        self.close()

    def onMyToolBarButtonClick(self, s):
        print("click", s)

# -----------------------------------------------------------------------

class HomePage(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python LifeHacks Tool")

        # Boutton pour accéder au cve checker
        self.cvecheckButton = QPushButton("Excel")
        self.cvecheckButton.clicked.connect(self.show_excel_page)       
        
        # Import des éléments dans la page
        layout = QVBoxLayout()
        layout.addWidget(self.cvecheckButton)
        layout.addWidget(self.reportButton)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def show_excel_page(self, checked):
        self.w = ExcelTools()
        self.w.show()
        self.close()


# ---------------------------------------------------------------------------

class ExcelTools(MainWindow):
    """
    L'objectif de cette classe est de regrouper les fonctionnalités liés 
    à la manipulation d'un fichier excel
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Page")

        # Boutton pour google chrome
        self.googleButton = QPushButton("Create an exel")
        self.googleButton.clicked.connect(create_excel)    

        # Import des éléments dans la page
        layout = QVBoxLayout()
        layout.addWidget(self.googleButton)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

# ---------------------------------------------------------------------------

app = QApplication(sys.argv)
w = HomePage()
w.show()
app.exec()
