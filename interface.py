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
        MainWindow.resize(650, 509)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(130, 380, 127, 80))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(30, 30, 521, 331))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget_fiteo = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_fiteo.setObjectName("tabWidget_fiteo")
        self.tab_modelo = QtWidgets.QWidget()
        self.tab_modelo.setObjectName("tab_modelo")
        self.label_cdc = QtWidgets.QLabel(self.tab_modelo)
        self.label_cdc.setGeometry(QtCore.QRect(10, 10, 57, 15))
        self.label_cdc.setObjectName("label_cdc")
        self.plainTextEdit_cdc = QtWidgets.QPlainTextEdit(self.tab_modelo)
        self.plainTextEdit_cdc.setGeometry(QtCore.QRect(60, 10, 191, 21))
        self.plainTextEdit_cdc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_cdc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_cdc.setObjectName("plainTextEdit_cdc")
        self.widget = QtWidgets.QWidget(self.tab_modelo)
        self.widget.setGeometry(QtCore.QRect(10, 40, 335, 17))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2_parametros = QtWidgets.QLabel(self.widget)
        self.label_2_parametros.setObjectName("label_2_parametros")
        self.horizontalLayout.addWidget(self.label_2_parametros)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.tabWidget_fiteo.addTab(self.tab_modelo, "")
        self.tab_2_ajuste = QtWidgets.QWidget()
        self.tab_2_ajuste.setObjectName("tab_2_ajuste")
        self.tabWidget_fiteo.addTab(self.tab_2_ajuste, "")
        self.tab_3_simulacion = QtWidgets.QWidget()
        self.tab_3_simulacion.setObjectName("tab_3_simulacion")
        self.tabWidget_fiteo.addTab(self.tab_3_simulacion, "")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_bode = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_bode.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_bode.setObjectName("verticalLayout_bode")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2_nyquist = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2_nyquist.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2_nyquist.setObjectName("verticalLayout_2_nyquist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 20))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionImportar = QtWidgets.QAction(MainWindow)
        self.actionImportar.setObjectName("actionImportar")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMaximizar = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Descargas/maximizar-la-opcion-de-tamano.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionMaximizar.setIcon(icon)
        self.actionMaximizar.setObjectName("actionMaximizar")
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionAbrir)
        self.menu_Archivo.addAction(self.actionImportar)
        self.menu_Archivo.addAction(self.actionGuardar)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionExit)
        self.menubar.addAction(self.menu_Archivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_fiteo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_cdc.setText(_translate("MainWindow", "CDC:"))
        self.label_2_parametros.setText(_translate("MainWindow", "Parámetros"))
        self.label_3.setText(_translate("MainWindow", "Fijar"))
        self.label_4.setText(_translate("MainWindow", "Límite Inferior"))
        self.label_5.setText(_translate("MainWindow", "Límite Superior"))
        self.label_6.setText(_translate("MainWindow", "Ajuste"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_modelo), _translate("MainWindow", "Modelo"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_2_ajuste), _translate("MainWindow", "Ajuste"))
        self.tabWidget_fiteo.setTabText(self.tabWidget_fiteo.indexOf(self.tab_3_simulacion), _translate("MainWindow", "Simulación"))
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionImportar.setText(_translate("MainWindow", "Importar"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))
        self.actionMaximizar.setText(_translate("MainWindow", "Maximizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
