import typing
import mysql.connector
import sys
import re
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate



class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi("main2.ui", self)
        
        self.add.clicked.connect(self.gotoadd)
        self.delete_2.clicked.connect(self.gotodelete)
        self.update2.clicked.connect(self.gotomodifier)
        self.search.clicked.connect(self.gotosearch)
        self.viewall.clicked.connect(self.gotodisplay)
        
    def gotoadd(self):
        add2=add()
        widget.addWidget(add2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotodelete(self):
        delete2=delete()
        widget.addWidget(delete2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotosearch(self):
        display2=search()
        widget.addWidget(display2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotomodifier(self):
        display2=modifier()
        widget.addWidget(display2)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotodisplay(self):
        window5=displayall3()
        widget.addWidget(window5)
        widget.setCurrentIndex(widget.currentIndex()+1)
class main2(QDialog):
    def __init__(self):
        super(main2, self).__init__()
        loadUi("mainclient.ui",self)
        self.displayall2.clicked.connect(self.displayall)
        self.search2.clicked.connect(self.gotosearch)
    def displayall(self):
        window5=displayall4()
        widget.addWidget(window5)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotosearch(self):
        window5=search()
        widget.addWidget(window5)
        widget.setCurrentIndex(widget.currentIndex()+1)
class search(QDialog):
    def __init__(self):
        super(search, self).__init__()
        loadUi("searchadmin.ui",self)
        self.return3.clicked.connect(self.gotomain2)
        self.search2.clicked.connect(self.searchp)
    def gotomain2(self):
        gtm=main2()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def searchp(self):
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        pattern = r'^[a-zA-Z]+$'
        name=self.name.text()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Error", "fill all the fields.")
            return
        if not re.match(pattern, name):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nom sans numero et sans caracteres.")
            return 
        def check_name(username,connection2):
                
                query = "SELECT * FROM product WHERE name = %s"
                cursor = connection2.cursor()  
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                
                if result:
                    
                    return True
                else:
                    return False
        name_exists = check_name(username=name,connection2=connection,)
        if  not name_exists:
            QtWidgets.QMessageBox.warning(self, "Error", "Le nom n'existe pas.")
            self.name.setText("")
            return
        else:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
            
        query = "SELECT * FROM product WHERE name=%s"
        val = (name,)
        cursor = connection.cursor()  
        cursor.execute(query, val)
        resultat = cursor.fetchall()
        print(resultat[0])
        self.test.setText(resultat[0][0])
        self.test_2.setText(resultat[0][1])
        self.test_3.setText(str(resultat[0][2]))
        self.test_4.setText(str(resultat[0][3]))
        self.test_5.setText(str(resultat[0][4]))
        self.test_6.setText(str(resultat[0][5]))
        self.test_7.setText(str(resultat[0][6]))
        return
    
    

        connection.close()

    



        
    
class displayall4(QDialog):
    def __init__(self):
        super(displayall4, self).__init__()
        loadUi("displayall2.ui",self)
        self.return2.clicked.connect(self.gotomain2)
        self.displayproduct2()
    def gotomain2(self):
        gtm=main2()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def displayproduct2(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        query = "SELECT * FROM product "
        cursor = connection.cursor()  
        cursor.execute(query)
        results = cursor.fetchall()
        num_rows = len(results)
        num_columns = len(results[0])
        tablewidget=self.tablewidget
        tablewidget.setRowCount(num_rows)
        tablewidget.setColumnCount(num_columns)
        

    # Add the data to the table widget
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(results[i][j]))
                tablewidget.setItem(i, j, item)
    






class displayall3(QDialog):
    def __init__(self):
        super(displayall3, self).__init__()
        loadUi("displayall.ui", self)
        self.return_2.clicked.connect(self.gotomain)
        self.displayproduct4()
    def gotomain(self):
        gtm=main()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def displayproduct4(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        query = "SELECT * FROM product "
        cursor = connection.cursor()  
        cursor.execute(query)
        results = cursor.fetchall()
        num_rows = len(results)
        num_columns = len(results[0])
        tablewidget=self.tablewidget
        tablewidget.setRowCount(num_rows)
        tablewidget.setColumnCount(num_columns)
        

    # Add the data to the table widget
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(results[i][j]))
                tablewidget.setItem(i, j, item)

        
class modifier(QDialog):
    def __init__(self):
        super(modifier, self).__init__()
        loadUi("modifier.ui", self)
        self.return_4.clicked.connect(self.gotomain2)
        self.modifier.clicked.connect(self.edit)
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,150)
        self.displayproduct()
        self.tableWidget.itemClicked.connect(self.onItemClicked)

    selected_row = -1
    def displayproduct(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        query = "SELECT * FROM product "
        cursor = connection.cursor()  
        cursor.execute(query)
        results = cursor.fetchall()
        num_rows = len(results)
        num_columns = len(results[0])
        tablewidget=self.tableWidget
        tablewidget.setRowCount(num_rows)
        tablewidget.setColumnCount(num_columns)
        

    # Add the data to the table widget
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(results[i][j]))
                tablewidget.setItem(i, j, item)
    def gotomain2(self):
        gtm=main()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    
    def onItemClicked(self, it):
        self.selected_row = it.row()
        # print(self.tableWidget.item(it.row(), 0).text())
        self.name.setText(self.tableWidget.item(it.row(), 0).text())
        self.description.setText(self.tableWidget.item(it.row(), 1).text())
        self.unitprice.setText(self.tableWidget.item(it.row(), 2).text())
        self.quantity.setText(self.tableWidget.item(it.row(), 3).text())
        self.threshold.setText(self.tableWidget.item(it.row(), 4).text())
        
    def edit(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        name = self.name.text()
        oldname = self.name.text()
        description = self.description.text()
        unitprice = self.unitprice.text()
        quantity = self.quantity.text()
        threshold = self.threshold.text()
        
        datein = self.datein.date().toString("yyyy-MM-dd")
        dateout = self.dateout.date().toString("yyyy-MM-dd")
        
        cursor = connection.cursor()
        sql="UPDATE product SET name=%s, description=%s, unitprice=%s, quantity=%s, threshold=%s, datein=%s, dateout=%s WHERE name=%s"
        val = (name, description, unitprice, quantity, threshold, datein, dateout,oldname)
            
        cursor.execute(sql, val)
        
           
        connection.commit()
        self.tableWidget.setItem(self.selected_row,0,QtWidgets.QTableWidgetItem(name))
        self.tableWidget.setItem(self.selected_row,1,QtWidgets.QTableWidgetItem(description))
        self.tableWidget.setItem(self.selected_row,2,QtWidgets.QTableWidgetItem(unitprice))
        self.tableWidget.setItem(self.selected_row,3,QtWidgets.QTableWidgetItem(quantity))
        self.tableWidget.setItem(self.selected_row,4,QtWidgets.QTableWidgetItem(threshold))
        self.tableWidget.setItem(self.selected_row,5,QtWidgets.QTableWidgetItem(datein))
        self.tableWidget.setItem(self.selected_row,6,QtWidgets.QTableWidgetItem(dateout))
        return


    

        

        

class delete(QDialog):
    def __init__(self):
        super(delete, self).__init__()
        loadUi("display.ui", self)
        self.return_2.clicked.connect(self.gotomain)
        self.delete_2.clicked.connect(self.deleteproduct)

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,150)
        self.displayproduct()
    def gotomain(self):
        gtm=main()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def displayproduct(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        query = "SELECT * FROM product "
        cursor = connection.cursor()  
        cursor.execute(query)
        results = cursor.fetchall()
        num_rows = len(results)
        num_columns = len(results[0])
        tablewidget=self.tableWidget
        tablewidget.setRowCount(num_rows)
        tablewidget.setColumnCount(num_columns)
        

    # Add the data to the table widget
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(results[i][j]))
                tablewidget.setItem(i, j, item)
    def deleteproduct(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        pattern = r'^[a-zA-Z]+$'
        name=self.name.text()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Error", "fill all the fields.")
            return
        if not re.match(pattern, name):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nom sans numero et sans caracteres.")
            return 
        def check_name(username,connection2):
                
                query = "SELECT * FROM product WHERE name = %s"
                cursor = connection2.cursor()  
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                
                if result:
                    
                    return True
                else:
                    return False
        name_exists = check_name(username=name,connection2=connection,)
        if  name_exists:
            
            cursor = connection.cursor()
            sql = "DELETE FROM product WHERE name = %s"
            value = (name,)
            cursor.execute(sql, value)
            self.name.setText("")
            model = self.tableWidget.model()
            for row in range(model.rowCount()):
                index = model.index(row,1)
                if index.data() == name:
                    model.removeRow(row)
                    break
            QMessageBox.information(self, "Success", "Product deleted successfully.")
            self.name.setText("")
            model = self.tableWidget.model()
            for row in range(model.rowCount()):
                index = model.index(row,0)
                if index.data() == name:
                    model.removeRow(row)
                    break
            
            connection.commit()
            cursor.close()

            return 
        
                
                
        else:
            
            QtWidgets.QMessageBox.warning(self, "Error", "name doesn't exist")
            self.name.setText("")
        
             
        
        
    
    

     
class add(QDialog):
    #constructor
    def __init__(self):
        super(add, self).__init__()
        loadUi("form.ui", self)
        self.return_3.clicked.connect(self.gotomain)
        self.add.clicked.connect(self.addproduct)
        self.display2()
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,150)
        
    def gotomain(self):
        gtm=main()
        widget.addWidget(gtm)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def display2(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        query = "SELECT * FROM product "
        cursor = connection.cursor()  
        cursor.execute(query)
        results = cursor.fetchall()
        row = len(results)
        num_columns = len(results[0])
        tablewidget=self.tableWidget
        tablewidget.setRowCount(row)
        tablewidget.setColumnCount(num_columns)
        

            # Add the data to the table widget
        for i in range(row):
            for j in range(num_columns):
                item = QTableWidgetItem(str(results[i][j]))
                tablewidget.setItem(i, j, item)  
                
                 
    def addproduct(self):
        
        name = self.name.text()
        description = self.description.text()
        unitprice = self.unitprice.text()
        quantity = self.quantity.text()
        threshold = self.threshold.text()
        
        datein = self.datein.date().toString("yyyy-MM-dd")
        dateout = self.dateout.date().toString("yyyy-MM-dd")

         
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gds",
        )
        pattern = r'^[a-zA-Z]+$'
        pattern2=r'^[0-9]*\.?[0-9]+$'
        if not name or not description  or not unitprice or not quantity or not threshold:
            QtWidgets.QMessageBox.warning(self, "Error", "fill all the fields.")
            return
        

        if not re.match(pattern, name):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nom sans numero et sans caracteres.")
            return 
        
        if not re.match(pattern2, unitprice):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nombre positif pour le prix.")
            return
        if not re.match(pattern2, quantity):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nombre positif pour la quantite.")
            return
        if not re.match(pattern2, threshold):
            QtWidgets.QMessageBox.warning(self, "Error", "Entrer un nombre positif pour le seuil de stock.")
            return
        #elif not name or not description or not unitprice or not quantity or not threshold:
            #QtWidgets.QMessageBox.warning(self, "Error", "fill all the field.")
        
        
        def check_name(username,connection2):
                
                query = "SELECT * FROM product WHERE name = %s"
                cursor = connection2.cursor()  
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                
                if result:
                    return True
                else:
                    return False
        name_exists = check_name(connection2=connection,username=name)
        if name_exists:
                
                QtWidgets.QMessageBox.warning(self, "Error", "name already exists")
        else:
            cursor = connection.cursor()
            sql = "INSERT INTO  product (name,description,unitprice,quantity,threshold,datein,dateout) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            
            val = (name, description, unitprice, quantity, threshold, datein, dateout)
            
            cursor.execute(sql, val)
            connection.commit()
            QMessageBox.information(self, "Success", "Product added successfully.")
            
            row=self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(description))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(unitprice))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(quantity))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(threshold))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(datein))
            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(dateout))
            
            
            return

            


        
        

app = QApplication(sys.argv)

mainwindow=main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
mainwindow.setFixedSize(650,500)
widget.show()
sys.exit(app.exec_())
