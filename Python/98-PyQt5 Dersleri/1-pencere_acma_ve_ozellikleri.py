import sys
from PyQt5 import QtWidgets  # pencere gibi dosya


def Pencere():
    # uygulama olusturur sysy.argv komut satırından birşey alınacaksa standart
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()  # pencere olusturur
    pencere.setWindowTitle("PyQt5 ders 1")  # pencereye baslık verdik
    pencere.show()  # pencereyi gosterdik

    sys.exit(app.exec())  # x tusuna basana kadar kapanmamasını saglar


Pencere()
