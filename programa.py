from PyQt5 import QtWidgets, QtCore
import sys
from interface import Ui_MainWindow
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Genero grafica con Matplotlib
        grafica_bode = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.verticalLayout_nyquist.addStretch()
        self.ui.verticalLayout_nyquist.addWidget(grafica_bode)
        self.addToolBar(NavigationToolbar(grafica_bode, self))
        self._bode_ax = grafica_bode.figure.subplots()

        grafica_nyquist = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.verticalLayout_bode.addWidget(grafica_nyquist)
        self.addToolBar(NavigationToolbar(grafica_nyquist, self))
        self._nyquist_ax = grafica_nyquist.figure.subplots()

        t = np.linspace(0, 10, 501)
        self._bode_ax.plot(t, np.tan(t), ".")
        self._nyquist_ax.plot(t, np.sin(t), ".")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
