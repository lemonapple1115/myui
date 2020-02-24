# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Py_Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets

matplotlib.use('QT5Agg')

from test import MyApp


class Ui_MainWindow(object):

    def Show_Layer_Window(self):
        self.exPopup = MyApp()
        self.exPopup.setGeometry(100, 200, 100, 100)
        self.exPopup.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 591)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 151, 51))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Layer_Config = QtWidgets.QPushButton(self.centralwidget)
        self.Layer_Config.setGeometry(QtCore.QRect(20, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)

        # ADD CODE FOR THE FIGURE

        # We want the axes cleared every time plot() is called
        # self.im = QPixmap("./nn_diagram.png")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(200, 50, 500, 500))
        self.photo.setText("layout")
        self.photo.setPixmap(QtGui.QPixmap('resources/nn_diagram.png'))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("Photo")

        # self.canvas = FigureCanvas(self.figure)
        # self.canvas.draw()

        # Connect the Layer Config buttom with the Main functional Window
        self.Layer_Config.setFont(font)
        self.Layer_Config.setObjectName("Layer_Config")
        self.Layer_Config.clicked.connect(self.Show_Layer_Window)

        self.Activation_Fn = QtWidgets.QPushButton(self.centralwidget)
        self.Activation_Fn.setGeometry(QtCore.QRect(20, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Activation_Fn.setFont(font)
        self.Activation_Fn.setObjectName("Activation_Fn")
        self.Batch_Size = QtWidgets.QPushButton(self.centralwidget)
        self.Batch_Size.setGeometry(QtCore.QRect(20, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Batch_Size.setFont(font)
        self.Batch_Size.setObjectName("Batch_Size")
        self.Neuron_Config = QtWidgets.QPushButton(self.centralwidget)
        self.Neuron_Config.setGeometry(QtCore.QRect(20, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Neuron_Config.setFont(font)
        self.Neuron_Config.setObjectName("Neuron_Config")
        self.Import_Data = QtWidgets.QPushButton(self.centralwidget)
        self.Import_Data.setGeometry(QtCore.QRect(20, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Import_Data.setFont(font)
        self.Import_Data.setObjectName("Import_Data")
        self.Settings = QtWidgets.QPushButton(self.centralwidget)
        self.Settings.setGeometry(QtCore.QRect(20, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Settings.setFont(font)
        self.Settings.setObjectName("Settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 22))
        self.menubar.setObjectName("menubar")
        self.menuInput_Panel = QtWidgets.QMenu(self.menubar)
        self.menuInput_Panel.setObjectName("menuInput_Panel")
        self.menuProcessing_Panel = QtWidgets.QMenu(self.menubar)
        self.menuProcessing_Panel.setObjectName("menuProcessing_Panel")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOPEN)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput_Panel.menuAction())
        self.menubar.addAction(self.menuProcessing_Panel.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # Just some button connected to `plot` method
        self.plot_view = QtWidgets.QPushButton(self.centralwidget)
        self.plot_view.setGeometry(QtCore.QRect(20, 430, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plot_view.setFont(font)
        self.plot_view.setObjectName("View Plot")

        # set the layout

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Neural Network Console"))
        self.Layer_Config.setText(_translate("MainWindow", "Layer Config"))
        self.plot_view.setText(_translate("MainWindow", "Activation Fn "))
        self.Activation_Fn.setText(_translate("MainWindow", "Activation Fn "))
        self.Batch_Size.setText(_translate("MainWindow", "View Plot"))
        self.Neuron_Config.setText(_translate("MainWindow", "Neuron Config"))
        self.Import_Data.setText(_translate("MainWindow", "Import Data"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
        self.menuInput_Panel.setTitle(_translate("MainWindow", "Input Panel"))
        self.menuProcessing_Panel.setTitle(_translate("MainWindow", "Neural Network View"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOPEN.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
