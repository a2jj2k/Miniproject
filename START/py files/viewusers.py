# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewusers.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cx_Oracle
import config

class Ui_ViewUsers(object):

    def loadData(self):
        """ Function that loads initial data to the qtable widget """
        self.tableWidget.setRowCount(0);
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        sql=""" select first_name||' '||middle_name||' '||last_name,
            email_id,
            case adm_flg when 1 Then 'Yes'
            else 'No' end
            from user_tbl"""
        #cur.execute(SQL, {'a' : 1}).fetchall()
        #[('X',)]
        cur.execute(sql)
        res=cur.fetchall()
        #print(res)
        self.tableWidget.setRowCount(len(res))
        for i in range (0,len(res)):
            for j in range(0,len(res[i])):
                item=QtWidgets.QTableWidgetItem(res[i][j])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        #print (res)
        #print(res[0][0])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents )
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        cur.close()
        con.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(673, 392)
        Dialog.setFixedSize(673,392)
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(250, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 611, 241))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.loadData()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Users"))
        self.lbl_head.setText(_translate("Dialog", "User\'s List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Email Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Admin Privilege"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ViewUsers()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("View Users")
    Dialog.show()
    sys.exit(app.exec_())

