# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1126, 576)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget_fiteo = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_fiteo.setObjectName("tabWidget_fiteo")
        self.tab_modelo = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_modelo.sizePolicy().hasHeightForWidth())
        self.tab_modelo.setSizePolicy(sizePolicy)
        self.tab_modelo.setObjectName("tab_modelo")
        self.label_cdc = QtWidgets.QLabel(self.tab_modelo)
        self.label_cdc.setGeometry(QtCore.QRect(10, 10, 57, 15))
        self.label_cdc.setObjectName("label_cdc")
        self.plainTextEdit_cdc = QtWidgets.QPlainTextEdit(self.tab_modelo)
        self.plainTextEdit_cdc.setGeometry(QtCore.QRect(60, 10, 191, 21))
        self.plainTextEdit_cdc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_cdc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_cdc.setObjectName("plainTextEdit_cdc")
        self.layoutWidget = QtWidgets.QWidget(self.tab_modelo)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 335, 17))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_parametros = QtWidgets.QLabel(self.layoutWidget)
        self.label_parametros.setObjectName("label_parametros")
        self.horizontalLayout.addWidget(self.label_parametros)
        self.label_fijar = QtWidgets.QLabel(self.layoutWidget)
        self.label_fijar.setObjectName("label_fijar")
        self.horizontalLayout.addWidget(self.label_fijar)
        self.label_limiteinferior = QtWidgets.QLabel(self.layoutWidget)
        self.label_limiteinferior.setObjectName("label_limiteinferior")
        self.horizontalLayout.addWidget(self.label_limiteinferior)
        self.label_limitesuperior = QtWidgets.QLabel(self.layoutWidget)
        self.label_limitesuperior.setObjectName("label_limitesuperior")
        self.horizontalLayout.addWidget(self.label_limitesuperior)
        self.label_ajuste = QtWidgets.QLabel(self.layoutWidget)
        self.label_ajuste.setObjectName("label_ajuste")
        self.horizontalLayout.addWidget(self.label_ajuste)
        self.tabWidget_fiteo.addTab(self.tab_modelo, "")
        self.tab_ajuste = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_ajuste.sizePolicy().hasHeightForWidth())
        self.tab_ajuste.setSizePolicy(sizePolicy)
        self.tab_ajuste.setObjectName("tab_ajuste")
        self.groupBox = QtWidgets.QGroupBox(self.tab_ajuste)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 171, 91))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_levenberg = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_levenberg.setGeometry(QtCore.QRect(10, 30, 155, 21))
        self.radioButton_levenberg.setObjectName("radioButton_levenberg")
        self.radioButton_simplex = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_simplex.setGeometry(QtCore.QRect(10, 60, 155, 21))
        self.radioButton_simplex.setObjectName("radioButton_simplex")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_ajuste)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 20, 171, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_simplex_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_simplex_4.setGeometry(QtCore.QRect(10, 77, 109, 21))
        self.radioButton_simplex_4.setObjectName("radioButton_simplex_4")
        self.radioButton_simplex_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_simplex_2.setGeometry(QtCore.QRect(10, 23, 109, 21))
        self.radioButton_simplex_2.setObjectName("radioButton_simplex_2")
        self.radioButton_simplex_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_simplex_3.setGeometry(QtCore.QRect(10, 50, 109, 21))
        self.radioButton_simplex_3.setObjectName("radioButton_simplex_3")
        self.tabWidget_fiteo.addTab(self.tab_ajuste, "")
        self.tab_simulacion = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_simulacion.sizePolicy().hasHeightForWidth())
        self.tab_simulacion.setSizePolicy(sizePolicy)
        self.tab_simulacion.setObjectName("tab_simulacion")
        self.tabWidget_fiteo.addTab(self.tab_simulacion, "")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_bode = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_bode.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_bode.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_bode.setObjectName("verticalLayout_bode")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_nyquist = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_nyquist.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_nyquist.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_nyquist.setObjectName("verticalLayout_nyquist")
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 20))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionImportar = QtWidgets.QAction(MainWindow)
        self.actionImportar.setObjectName("actionImportar")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionAbrir)
        self.menu_Archivo.addAction(self.actionImportar)
        self.menu_Archivo.addAction(self.actionGuardar)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionExit)
        self.menubar.addAction(self.menu_Archivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_fiteo.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CorrosionEIS - versión 0.1"))
        self.label_cdc.setText(_translate("MainWindow", "CDC:"))
        self.label_parametros.setText(_translate("MainWindow", "Parámetros"))
        self.label_fijar.setText(_translate("MainWindow", "Fijar"))
        self.label_limiteinferior.setText(_translate("MainWindow", "Límite Inferior"))
        self.label_limitesuperior.setText(_translate("MainWindow", "Límite Superior"))
        self.label_ajuste.setText(_translate("MainWindow", "Ajuste"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_modelo), _translate("MainWindow", "Modelo"))
        self.groupBox.setTitle(_translate("MainWindow", "Método de ajuste"))
        self.radioButton_levenberg.setText(_translate("MainWindow", "Levenberg-Marquardt"))
        self.radioButton_simplex.setText(_translate("MainWindow", "Simplex"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ponderación"))
        self.radioButton_simplex_4.setText(_translate("MainWindow", "Módulo Z"))
        self.radioButton_simplex_2.setText(_translate("MainWindow", "Unitario"))
        self.radioButton_simplex_3.setText(_translate("MainWindow", "Proporcional"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_ajuste), _translate("MainWindow", "Ajuste"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_simulacion), _translate("MainWindow", "Simulación"))
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionImportar.setText(_translate("MainWindow", "Importar"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

