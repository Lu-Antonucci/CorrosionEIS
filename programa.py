from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from interface import Ui_MainWindow
from matplotlib.figure import Figure
import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Genero grafica con Matplotlib

        seno = WidgetPlot(self)
        PlotCanvas()
        self.ui.verticalLayout_nyquist.addWidget(seno)

        coseno = WidgetPlot(self)
        self.ui.verticalLayout_bode.addWidget(coseno)


class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = PlotCanvas(self, width=10, height=8)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = np.linspace(0, 10, 501)
        ax = self.figure.add_subplot(111)
        ax.plot(data, np.sin(data), ".")
        ax.set_title('Función Seno')
        self.draw()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
