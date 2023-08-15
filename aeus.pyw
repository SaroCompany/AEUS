from PyQt5 import QtWidgets
import sys
from scripts.main import VentanaPrincipalAEUS


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = VentanaPrincipalAEUS()
    main.show()
    sys.exit(app.exec_())