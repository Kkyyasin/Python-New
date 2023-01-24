
import sys
from PyQt5 import QtWidgets


def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 3")
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    """ h_box = QtWidgets.QHBoxLayout()  # yatay yonde dengelemk için hbox olustururzu
    h_box.addWidget(okay) #?yatay yonde tam ortalayacak sekilde hizlalar
    h_box.addWidget(cancel)"""
    """v_box = QtWidgets.QVBoxLayout()#?dikey yonde hizlar
    v_box.addWidget(okay)
    v_box.addWidget(cancel)"""
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()  # soldan bosluk olusturur
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()  # ussten bosluk olusturur
    v_box.addLayout(h_box)
    pencere.setGeometry(100, 100, 640, 480)
    pencere.setLayout(v_box)
    pencere.show()
    sys.exit(app.exec_())


Pencere()
