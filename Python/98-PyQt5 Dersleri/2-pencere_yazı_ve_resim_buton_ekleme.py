import sys
from PyQt5 import QtGui, QtWidgets


def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 ders 2")
    # nerden baslanacagı x ve ye kordinatları sırasıyla ve sonra boyutu
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Pyton yazı yazma")
    etiket1.move(800, 150)
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Buton")
    buton.move(80, 600)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("p.png"))

    pencere.setGeometry(100, 300, 640, 480)
    pencere.show()
    sys.exit(app.exec_())


pencere()
