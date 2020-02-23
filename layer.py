# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Layer(object):
    def setupUi(self, Dialog_Layer):
        Dialog_Layer.setObjectName("Dialog_Layer")
        Dialog_Layer.resize(606, 383)
        self.buttonBox_Layers = QtWidgets.QDialogButtonBox(Dialog_Layer)
        self.buttonBox_Layers.setGeometry(QtCore.QRect(190, 290, 171, 81))
        self.buttonBox_Layers.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Layers.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_Layers.setObjectName("buttonBox_Layers")
        self.pushButton_LayerNo = QtWidgets.QPushButton(Dialog_Layer)
        self.pushButton_LayerNo.setGeometry(QtCore.QRect(40, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.pushButton_LayerNo.setFont(font)
        self.pushButton_LayerNo.setObjectName("pushButton_LayerNo")
        self.lineEdit_LayerNo = QtWidgets.QLineEdit(Dialog_Layer)
        self.lineEdit_LayerNo.setGeometry(QtCore.QRect(180, 60, 91, 31))
        self.lineEdit_LayerNo.setText("")
        self.lineEdit_LayerNo.setObjectName("lineEdit_LayerNo")
        self.pushButton_ACFN = QtWidgets.QPushButton(Dialog_Layer)
        self.pushButton_ACFN.setGeometry(QtCore.QRect(40, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_ACFN.setFont(font)
        self.pushButton_ACFN.setObjectName("pushButton_ACFN")
        self.spinBox_LayerNo = QtWidgets.QSpinBox(Dialog_Layer)
        self.spinBox_LayerNo.setGeometry(QtCore.QRect(290, 60, 51, 31))
        self.spinBox_LayerNo.setObjectName("spinBox_LayerNo")
        self.lineEdit_ACFN = QtWidgets.QLineEdit(Dialog_Layer)
        self.lineEdit_ACFN.setGeometry(QtCore.QRect(180, 120, 121, 31))
        self.lineEdit_ACFN.setObjectName("lineEdit_ACFN")
        self.pushButton_SHUFFED = QtWidgets.QPushButton(Dialog_Layer)
        self.pushButton_SHUFFED.setGeometry(QtCore.QRect(40, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_SHUFFED.setFont(font)
        self.pushButton_SHUFFED.setObjectName("pushButton_SHUFFED")
        self.checkBox_Shuffer = QtWidgets.QCheckBox(Dialog_Layer)
        self.checkBox_Shuffer.setGeometry(QtCore.QRect(180, 180, 51, 21))
        self.checkBox_Shuffer.setText("")
        self.checkBox_Shuffer.setObjectName("checkBox_Shuffer")
        self.pushButton_Epochs = QtWidgets.QPushButton(Dialog_Layer)
        self.pushButton_Epochs.setGeometry(QtCore.QRect(40, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_Epochs.setFont(font)
        self.pushButton_Epochs.setObjectName("pushButton_Epochs")
        self.lineEdit_EPOCHS = QtWidgets.QLineEdit(Dialog_Layer)
        self.lineEdit_EPOCHS.setGeometry(QtCore.QRect(180, 230, 91, 31))
        self.lineEdit_EPOCHS.setText("")
        self.lineEdit_EPOCHS.setObjectName("lineEdit_EPOCHS")

        self.retranslateUi(Dialog_Layer)
        self.buttonBox_Layers.accepted.connect(Dialog_Layer.accept)
        self.buttonBox_Layers.rejected.connect(Dialog_Layer.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Layer)

    def retranslateUi(self, Dialog_Layer):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Layer.setWindowTitle(_translate("Dialog_Layer", "Dialog"))
        self.pushButton_LayerNo.setText(_translate("Dialog_Layer", "Layer Numbers"))
        self.pushButton_ACFN.setText(_translate("Dialog_Layer", "Activation Function"))
        self.pushButton_SHUFFED.setText(_translate("Dialog_Layer", "SHUFFED"))
        self.pushButton_Epochs.setText(_translate("Dialog_Layer", "EPOCHS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Layer = QtWidgets.QDialog()
    ui = Ui_Dialog_Layer()
    ui.setupUi(Dialog_Layer)
    Dialog_Layer.show()
    sys.exit(app.exec_())
