import sys
import os
import string
from random import choice
from helper import Paths

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
    QDialog,
    QDialogButtonBox,
    QTextEdit
)

# global variables
FONT_FAMILY = "Courier"

# showing icon on the taskbar for windows
try:
    from ctypes import windll

    appId = "karnesdevelopment.kdpasswordgenerator.version-1"
    windll.shell32.SetCurrentProcessExplitAppUserModelId(appId)
except ImportError:
    pass


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("KD Password Generator Help")

        button = QDialogButtonBox.StandardButton.Ok
        self.btn_box = QDialogButtonBox(button)
        self.btn_box.accepted.connect(self.accept)

        self.header_lbl = QLabel("How to use the Generator:")
        font = self.header_lbl.font()
        font.setPointSize(14)
        font.setFamily(FONT_FAMILY)
        self.header_lbl.setFont(font)
        self.header_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_step_img = QLabel()
        img = QPixmap(Paths.image("step_one.png"))
        self.first_step_img.setPixmap(img)
        self.first_step_img.resize(img.width(), img.height())
        self.first_step_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_step_lbl = QLabel("1. Select a number in the Dropdown.")
        font = self.first_step_lbl.font()
        font.setPointSize(10)
        font.setFamily(FONT_FAMILY)
        self.first_step_lbl.setFont(font)

        self.sec_step_img = QLabel()
        img = QPixmap(Paths.image("step_two.png"))
        self.sec_step_img.setPixmap(img)
        self.sec_step_img.resize(img.width(), img.height())
        self.sec_step_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sec_step_lbl = QLabel(
            "2. Click the \"Generate\" button to generate the password."
        )
        font = self.sec_step_lbl.font()
        font.setPointSize(10)
        font.setFamily(FONT_FAMILY)
        self.sec_step_lbl.setFont(font)

        self.third_step_img = QLabel()
        img = QPixmap(Paths.image("step_three.png"))
        self.third_step_img.setPixmap(img)
        self.third_step_img.resize(img.width(), img.height())
        self.third_step_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.third_step_lbl = QLabel(
            "3. Now click the \"Copy\" button to copy the password into your clipboard."
        )
        font = self.third_step_lbl.font()
        font.setPointSize(10)
        font.setFamily(FONT_FAMILY)
        self.third_step_lbl.setFont(font)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.header_lbl)
        self.layout.addWidget(self.first_step_lbl)
        self.layout.addWidget(self.first_step_img)
        self.layout.addWidget(self.sec_step_lbl)
        self.layout.addWidget(self.sec_step_img)
        self.layout.addWidget(self.third_step_lbl)
        self.layout.addWidget(self.third_step_img)
        self.layout.addWidget(self.btn_box)

        self.setLayout(self.layout)


class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("KD Password Generator Info")

        button = QDialogButtonBox.StandardButton.Ok
        self.btn_box = QDialogButtonBox(button)
        self.btn_box.accepted.connect(self.accept)

        self.header_lbl = QLabel("KD Password Generator")
        font = self.header_lbl.font()
        font.setPointSize(14)
        font.setFamily(FONT_FAMILY)
        self.header_lbl.setFont(font)
        self.header_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.desc_field = QTextEdit()
        self.desc_field.setText(
            "The KD Password Generator is a simple desktop application to generate a random password between 8 and 20 characters."
        )
        self.desc_field.setReadOnly(True)

        self.footer_lbl = QLabel(
            "Version: 1.0.0 | Developed by Patrick Hähnel")
        font = self.footer_lbl.font()
        font.setPointSize(10)
        font.setFamily(FONT_FAMILY)
        self.footer_lbl.setFont(font)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.header_lbl)
        self.main_layout.addWidget(self.desc_field)
        self.main_layout.addWidget(self.footer_lbl)
        self.main_layout.addWidget(self.btn_box)

        self.setLayout(self.main_layout)


class MessageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        button = QDialogButtonBox.StandardButton.Ok
        self.btn_box = QDialogButtonBox(button)
        self.btn_box.accepted.connect(self.accept)

        self.message_lbl = QLabel()
        font = self.message_lbl.font()
        font.setPointSize(12)
        font.setFamily(FONT_FAMILY)
        self.message_lbl.setFont(font)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message_lbl)
        self.layout.addWidget(self.btn_box)

        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        """Initialize the main window"""
        super().__init__()

        self.setWindowTitle("KD Password Generator")
        self.setFixedSize(QSize(300, 200))

        # variables
        self.pass_len_list = [
            "-- Select a password length --",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
        ]
        self.pass_len = 0

        # info label
        self.info_lbl = QLabel("Generate a random password")
        font = self.info_lbl.font()
        font.setPointSize(12)
        self.info_lbl.setFont(font)
        self.info_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # dropdown menu for the password length
        self.dropdown_cb = QComboBox()
        self.dropdown_cb.addItems(self.pass_len_list)
        self.dropdown_cb.activated.connect(self.activated)

        # generate button to generate the password
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.generate_password)

        # copy button to copy the generated password to the clipboard
        self.copy_btn = QPushButton("Copy")
        self.copy_btn.clicked.connect(self.copy_password)

        # output field to showing the generated password
        self.output_field = QLineEdit()
        font = self.output_field.font()
        font.setPointSize(16)
        self.output_field.setFont(font)
        self.output_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_field.setReadOnly(True)

        # exit button to exit the program
        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(self.exit_program)

        # horizontal button layout
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.generate_btn)
        self.btn_layout.addWidget(self.copy_btn)

        # vertical widget layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.info_lbl)
        self.layout.addWidget(self.dropdown_cb)
        self.layout.addLayout(self.btn_layout)
        self.layout.addWidget(self.output_field)
        self.layout.addWidget(self.exit_btn)

        # container for vertical layout
        self.container = QWidget()
        self.container.setLayout(self.layout)

        # help action button
        help_action = QAction("Help", self)
        help_action.setStatusTip("&Help")
        help_action.triggered.connect(self.onHelpActionBtnClick)

        # info action button
        info_action = QAction("About", self)
        info_action.setStatusTip("&About")
        info_action.triggered.connect(self.onInfoActionBtnClick)

        # menu bar
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("&Help")
        help_menu.addAction(help_action)
        help_menu.addAction(info_action)

        # center the container in the main window
        self.setCentralWidget(self.container)

    def activated(self, idx):
        """Sets the value selected in the dropdown as password length."""
        if idx > 0:
            self.pass_len = self.pass_len_list[idx]

    def generate_password(self):
        """Generate the password."""
        if self.dropdown_cb.currentText() == self.pass_len_list[0]:
            dlg = MessageDialog(self)
            dlg.setWindowTitle("Please select a number...")
            dlg.message_lbl.setText(
                "Please select a number to generate a password."
            )
            dlg.exec()
        else:
            chars = string.ascii_letters + string.digits + string.punctuation
            password = "".join(choice(chars)
                               for i in range(int(self.pass_len)))
            self.output_field.setText(password)

    def copy_password(self):
        """Copy the generated password to the clipboard"""
        QApplication.clipboard().setText(self.output_field.text())

    def exit_program(self):
        """Exit program"""
        btn = QMessageBox.question(
            self,
            "Exit program",
            "Do you want to exit program?"
        )

        if btn == QMessageBox.StandardButton.Yes:
            sys.exit(0)

    def onHelpActionBtnClick(self):
        """Shows a Dialog with helping text"""
        dlg = HelpDialog(self)
        dlg.exec()

    def onInfoActionBtnClick(self):
        dlg = InfoDialog(self)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(Paths.icon("logo.svg")))
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
