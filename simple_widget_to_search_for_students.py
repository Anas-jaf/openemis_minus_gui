import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout, QLabel, QPushButton, QDialog
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class QListStudentsWindow(QDialog):
    def __init__(self, students_data):
        super().__init__()
        self.students_data = students_data
        self.initUI()

    def initUI(self):
        self.resize(1600, 1200)  # Increase the size of the second widget
        mainLayout = QVBoxLayout()

        # companies = [('Apple', 'Technology'), ('Facebook', 'Social Media'), ('Google', 'Technology'), ('Amazon', 'E-commerce'),
        #              ('Walmart', 'Retail'), ('Dropbox', 'Cloud Storage'), ('Starbucks', 'Coffee'), ('eBay', 'E-commerce'), ('Canon', 'Electronics')]
        student_data = self.students_data
        model = QStandardItemModel(len(student_data), 2)
        model.setHorizontalHeaderLabels(['Company', 'Category'])  # Two columns: Company and Category

        for row, (company, category) in enumerate(student_data):
            item_company = QStandardItem(company)
            item_category = QStandardItem(category)
            model.setItem(row, 0, item_company)
            model.setItem(row, 1, item_category)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 35px; height: 60px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet('font-size: 35px;')
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        self.setLayout(mainLayout)

class AuthenticationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Authentication Widget")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        label_username = QLabel("Username:")
        self.edit_username = QLineEdit()

        label_password = QLabel("Password:")
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)  # To hide the password characters

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        layout.addWidget(label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def login(self):
        companies = [('Apple', 'Technology'), ('Facebook', 'Social Media'), ('Google', 'Technology'), ('Amazon', 'E-commerce'),
                     ('Walmart', 'Retail'), ('Dropbox', 'Cloud Storage'), ('Starbucks', 'Coffee'), ('eBay', 'E-commerce'), ('Canon', 'Electronics')]
        self.qListWindow = QListStudentsWindow(companies)
        self.qListWindow.exec_()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = AuthenticationWidget()
    window.show()
    sys.exit(app.exec_())
