import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QListWidgetItem, QDialog, QApplication, QFileDialog , QMainWindow , QInputDialog , QTableWidgetItem , QTableWidget , QAbstractItemView , QHeaderView , QMessageBox , QLineEdit 
from PyQt5.uic import loadUi
import json        


names ,classes = [] , []

class Mainscreen(QMainWindow):
    def __init__(self):
        super(Mainscreen,self).__init__()
        loadUi("mainscreen.ui",self)
        self.pushButton_4.clicked.connect(self.nextscreen)
        self.loadTeachers()
        self.add_1.clicked.connect(self.addTeacher)
        self.remove_1.clicked.connect(self.removeTeacher)
        self.edit_1.clicked.connect(self.editTeacher)
        self.loadGrade()
        self.add_2.clicked.connect(self.addGrade)
        self.remove_2.clicked.connect(self.removeGrade)
        self.edit_2.clicked.connect(self.editGrade)
        
    def loadGrade(self):
        for clas in classes:
            items = QListWidgetItem(clas)
            self.listWidget_2.addItem(items)
        # self.listWidget_1.addItems(['Adam','Axel','Washington','Gilbert'])
        # self.listWidget_1.setCurrentRow(1)

    def addGrade(self):
        currentIndex = self.listWidget_2.currentRow()
        text, ok = QInputDialog.getText(self,"صف جديد","اسم الصف")
        if ok and text is not None:
            # global names
            # names.append(text)
            # print(text)
            self.listWidget_2.insertItem(currentIndex,text)

    def editGrade(self):
        currentIndex = self.listWidget_2.currentRow()
        item = self.listWidget_2.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self,"تعديل اسم المعلم","اسم المعلم",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removeGrade(self):
        currentIndex = self.listWidget_2.currentRow()
        item = self.listWidget_2.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self,"حذف صف ",
                                        "؟ هل انت متاكد من حذف الصف" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.listWidget_2.takeItem(currentIndex)
            del item
# --------------------------------------        
    def loadTeachers(self):
        for name in names:
            items = QListWidgetItem(name)
            self.listWidget_1.addItem(items)
        # self.listWidget_1.addItems(['Adam','Axel','Washington','Gilbert'])
        # self.listWidget_1.setCurrentRow(1)

    def addTeacher(self):
        currentIndex = self.listWidget_1.currentRow()
        text, ok = QInputDialog.getText(self,"معلم جديد","اسم المعلم")
        if ok and text is not None:
            # global names
            # names.append(text)
            print(text)
            self.listWidget_1.insertItem(currentIndex,text)

    def editTeacher(self):
        currentIndex = self.listWidget_1.currentRow()
        item = self.listWidget_1.item(currentIndex)
        if item is not None:
            text, ok = QInputDialog.getText(self,"تعديل اسم المعلم","اسم المعلم",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)

    def removeTeacher(self):
        currentIndex = self.listWidget_1.currentRow()
        item = self.listWidget_1.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self,"حذف معلم ",
                                        "هل انت متاكد من حذف المعلم ؟" + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.listWidget_1.takeItem(currentIndex)
            del item
                    
    def nextscreen(self):
        # print(names)
        # print(self.listWidget_1.count())
        for i in range(self.listWidget_1.count()):
            global names , classes
            print(self.listWidget_1.item(i).text())
            names.append(self.listWidget_1.item(i).text())
        
        data = {"teachers" :[],"classes":[]}
        data['teachers'] += names
        data['teachers'] += classes
        # print data
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)            
        print(names)

        # for name in names:
        #     items = QListWidgetItem(name)
        #     print(items.text())
        # import time 
        # time.sleep(1)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen1(QDialog ):
    def __init__(self):
        super(Screen1,self).__init__()
        loadUi("1.ui",self)
        self.pushButton.clicked.connect(self.nextscreen)
        self.loadNames(names)
        # FIXME: fix the problem of adding names list to combobox  

        
    def loadNames(self , names):
        for name in names:
            self.comboBox.addItem(name)
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)        

class Screen2(QDialog):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("2.ui",self)        
        # for name in names:
        #     self.comboBox.addItem(str(name))
        self.pushButton.clicked.connect(self.nextscreen)
        
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)        

class Screen3(QDialog):
    def __init__(self):
        super(Screen3,self).__init__()
        loadUi("3.ui",self)
        self.pushButton.clicked.connect(self.nextscreen)
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen4(QDialog):
    def __init__(self):
        super(Screen4,self).__init__()
        loadUi("4.ui",self)
        self.pushButton.clicked.connect(self.nextscreen)
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen5(QDialog):
    def __init__(self):
        super(Screen5,self).__init__()
        loadUi("5.ui",self)
        self.pushButton.clicked.connect(self.nextscreen)
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen6(QDialog):
    def __init__(self):
        super(Screen6,self).__init__()
        loadUi("6.ui",self)
        self.pushButton.clicked.connect(self.nextscreen)
    def nextscreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen7(QDialog):
    def __init__(self):
        super(Screen7,self).__init__()
        loadUi("7.ui",self)
        self.pushButton.clicked.connect(self.firstscreen)
    def firstscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-6)
        # add code here check if grade table is empty or not 
        # if empty then show message
        # if not empty then change the grade and go to the first class screen 
        # TODO: add box to see the saved classes and grades in each class dialouge screen
        
    #     self.pushButton.clicked.connect(self.openScreen8)
    # def nextscreen(self):
    #     widget.setCurrentIndex(widget.currentIndex()+1)
        
app=QApplication(sys.argv)
mainwindow=Mainscreen()
screen1,screen2,screen3,screen4,screen5,screen6,screen7=Screen1(),Screen2(),Screen3(),Screen4(),Screen5(),Screen6(),Screen7()
# screen1= Screen1()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(screen1)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.addWidget(screen5)
widget.addWidget(screen6)
widget.addWidget(screen7)
    
widget.setFixedWidth(510)
widget.setFixedHeight(530)
widget.show()
sys.exit(app.exec_())        
        