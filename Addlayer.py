# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addlayer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog_Layer_Config(object):
    def setupUi(self, Dialog_Layer_Config):
        Dialog_Layer_Config.setObjectName("Dialog_Layer_Config")
        Dialog_Layer_Config.resize(521, 227)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Layer_Config)
        self.buttonBox.setGeometry(QtCore.QRect(170, 180, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(Dialog_Layer_Config)
        self.checkBox.setGeometry(QtCore.QRect(50, 140, 101, 18))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_Activate = QtWidgets.QLineEdit(Dialog_Layer_Config)
        self.lineEdit_Activate.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.lineEdit_Activate.setObjectName("lineEdit_Activate")
        self.label_Acfn = QtWidgets.QLabel(Dialog_Layer_Config)
        self.label_Acfn.setGeometry(QtCore.QRect(50, 50, 111, 21))
        self.label_Acfn.setObjectName("label_Acfn")

        self.retranslateUi(Dialog_Layer_Config)
        self.buttonBox.accepted.connect(Dialog_Layer_Config.accept)
        self.buttonBox.rejected.connect(Dialog_Layer_Config.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Layer_Config)

    def retranslateUi(self, Dialog_Layer_Config):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Layer_Config.setWindowTitle(_translate("Dialog_Layer_Config", "Dialog"))
        self.checkBox.setText(_translate("Dialog_Layer_Config", "Output Layer?"))
        self.label_Acfn.setText(_translate("Dialog_Layer_Config", "Activation Function"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_Layer_Config = QtWidgets.QDialog()
    ui = Ui_Dialog_Layer_Config()
    ui.setupUi(Dialog_Layer_Config)
    Dialog_Layer_Config.show()
    sys.exit(app.exec_())
