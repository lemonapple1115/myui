# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dynamic_Layer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Addlayer(object):

    Num_Layer = 0

    def Add_Pushbutton(self):
        print('Add Layer is clicked')
        newBtn = QtWidgets.QPushButton('New Button', self) 
        self.scrollArea_Layer.setWidgetResizable(True)
        
        
            
            
        

        
    def setupUi(self, Dialog_Addlayer):
        Dialog_Addlayer.setObjectName("Dialog_Addlayer")
        Dialog_Addlayer.resize(751, 528)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Addlayer)
        self.buttonBox.setGeometry(QtCore.QRect(400, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.scrollArea_Layer = QtWidgets.QScrollArea(Dialog_Addlayer)
        self.scrollArea_Layer.setGeometry(QtCore.QRect(20, 100, 221, 331))
        self.scrollArea_Layer.setWidgetResizable(True)
        self.scrollArea_Layer.setObjectName("scrollArea_Layer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_Layer.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_addlayer = QtWidgets.QPushButton(Dialog_Addlayer)
        self.pushButton_addlayer.setGeometry(QtCore.QRect(20, 50, 221, 31))
        self.pushButton_addlayer.setObjectName("pushButton_addlayer")
        self.pushButton_addlayer.clicked.connect(self.Add_Pushbutton)

        self.retranslateUi(Dialog_Addlayer)
        self.buttonBox.accepted.connect(Dialog_Addlayer.accept)
        self.buttonBox.rejected.connect(Dialog_Addlayer.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Addlayer)

    def retranslateUi(self, Dialog_Addlayer):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Addlayer.setWindowTitle(_translate("Dialog_Addlayer", "Dialog"))
        self.pushButton_addlayer.setText(_translate("Dialog_Addlayer", "Add Layer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Addlayer = QtWidgets.QDialog()
    ui = Ui_Dialog_Addlayer()
    ui.setupUi(Dialog_Addlayer)
    Dialog_Addlayer.show()
    sys.exit(app.exec_())
