from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tampilan.ui", self)  

        self.textNim.setText("F1D022142")

        self.aturSize.valueChanged.connect(self.ubahUkuranFont)
        self.latarWarna.valueChanged.connect(self.ubahLatarBelakang)
        self.fontWarna.valueChanged.connect(self.ubahWarnaFont)

        self.ubahUkuranFont()
        self.ubahLatarBelakang()
        self.ubahWarnaFont()

    def ubahUkuranFont(self):
        value = self.aturSize.value()
        size = 20 + (value / 100) * 40  
        self.perbaruiStyleSheet(font_size=int(size))

    def ubahLatarBelakang(self):
        value = self.latarWarna.value()
        gray = int((value / 100) * 255)
        bg_color = QColor(gray, gray, gray).name()
        self.perbaruiStyleSheet(background=bg_color)

    def ubahWarnaFont(self):
        value = self.fontWarna.value()
        gray = int((value / 100) * 255)
        font_color = QColor(gray, gray, gray).name()
        self.perbaruiStyleSheet(font_color=font_color)

    def perbaruiStyleSheet(self, font_size=None, background=None, font_color=None):
        style = ""

        if font_size is None:
            font_size = 20 + (self.aturSize.value() / 100) * 40
        if background is None:
            gray = int((self.latarWarna.value() / 100) * 255)
            background = QColor(gray, gray, gray).name()
        if font_color is None:
            gray = int((self.fontWarna.value() / 100) * 255)
            font_color = QColor(gray, gray, gray).name()

        style += f"font-size: {int(font_size)}pt;"
        style += f"background-color: {background};"
        style += f"color: {font_color};"

        self.textNim.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
