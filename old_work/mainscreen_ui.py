# Form implementation generated from reading ui file '/opt/programming/openemis_minus_gui/old_work/mainscreen.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 500)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Arabic, QtCore.QLocale.Country.Egypt))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 131, 41))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 310, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 310, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 250, 239, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.edit_1.setObjectName("edit_1")
        self.horizontalLayout_2.addWidget(self.edit_1)
        self.remove_1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.remove_1.setObjectName("remove_1")
        self.horizontalLayout_2.addWidget(self.remove_1)
        self.add_1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.add_1.setObjectName("add_1")
        self.horizontalLayout_2.addWidget(self.add_1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(55, 10, 131, 41))
        self.label_2.setObjectName("label_2")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 250, 239, 25))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_2 = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.edit_2.setObjectName("edit_2")
        self.horizontalLayout_3.addWidget(self.edit_2)
        self.remove_2 = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.remove_2.setObjectName("remove_2")
        self.horizontalLayout_3.addWidget(self.remove_2)
        self.add_2 = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        self.add_2.setObjectName("add_2")
        self.horizontalLayout_3.addWidget(self.add_2)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 310, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_1 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_1.setGeometry(QtCore.QRect(300, 50, 191, 192))
        self.listWidget_1.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.listWidget_1.setObjectName("listWidget_1")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 50, 191, 192))
        self.listWidget_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.layoutWidget_3.raise_()
        self.pushButton_6.raise_()
        self.listWidget_1.raise_()
        self.listWidget_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">المعلمون</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "حسنا"))
        self.pushButton_5.setText(_translate("MainWindow", "الغاء"))
        self.edit_1.setText(_translate("MainWindow", "تعديل"))
        self.remove_1.setText(_translate("MainWindow", "-"))
        self.add_1.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">الصفوف</span></p></body></html>"))
        self.edit_2.setText(_translate("MainWindow", "تعديل"))
        self.remove_2.setText(_translate("MainWindow", "-"))
        self.add_2.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "طباعة"))
        self.listWidget_1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.listWidget_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
