# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewsubjects.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cx_Oracle
import config

class Ui_ViewSubjects(object):

    def loadData(self):
        """ Function that loads initial data to the qtable widget """
        self.tblwidget_subview.setRowCount(0);
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        sql="""select * from subject_tbl where sem='S1'"""
        #cur.execute(SQL, {'a' : 1}).fetchall()
        #[('X',)]
        cur.execute(sql)
        res=cur.fetchall()
        #print(res)
        self.tblwidget_subview.setRowCount(len(res))
        for i in range (0,len(res)):
            for j in range(0,len(res[i])):
                item=QtWidgets.QTableWidgetItem(res[i][j])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblwidget_subview.setItem(i, j, item)
        #print (res)
        #print(res[0][0])
        header = self.tblwidget_subview.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        #con.commit()
        cur.close()
        con.close()



    def initialLoading_sem(self):
        """ Function to put initial values to the smester combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select cd_val_desc from system_codes where code_type=201""")
        res=cur.fetchall()
        sem=[]
        for i in range(0,cur.rowcount,1):
            sem.append(str(res[i][0]))
        cur.close()
        con.close()
        return sem

    def showSubjects(self):
        """ Function that display the subjects in a particular semester """
        semester=self.combo_sem.currentText()
        self.tblwidget_subview.setRowCount(0);
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        #sql="""select * from subject_tbl where sem='S1'"""
        #cur.execute(SQL, {'a' : 1}).fetchall()
        #[('X',)]
        cur.execute("""select * from subject_tbl where sem=:semester""",semester=semester)
        res=cur.fetchall()
        #print(res)
        self.tblwidget_subview.setRowCount(len(res))
        for i in range (0,len(res)):
            for j in range(0,len(res[i])):
                item=QtWidgets.QTableWidgetItem(res[i][j])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblwidget_subview.setItem(i, j, item)
        #print (res)
        #print(res[0][0])
        header = self.tblwidget_subview.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        #con.commit()
        cur.close()
        con.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(600, 467)
        Dialog.setFixedSize(600,467)
        self.tblwidget_subview = QtWidgets.QTableWidget(Dialog)
        self.tblwidget_subview.setGeometry(QtCore.QRect(60, 150, 481, 271))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tblwidget_subview.setFont(font)
        self.tblwidget_subview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwidget_subview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblwidget_subview.setRowCount(6)
        self.tblwidget_subview.setColumnCount(2)
        self.tblwidget_subview.setObjectName("tblwidget_subview")
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_subview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_subview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_subview.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_subview.setItem(0, 1, item)
        self.tblwidget_subview.horizontalHeader().setMinimumSectionSize(35)
        self.tblwidget_subview.verticalHeader().setDefaultSectionSize(40)
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(200, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(280, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        #########################################################
        self.combo_sem.addItems(self.initialLoading_sem())
        self.combo_sem.currentIndexChanged.connect(self.showSubjects)
        #############################################################
        #self.combo_sem.addItem("")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(170, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")
        self.loadData()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Subjects"))
        item = self.tblwidget_subview.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Subject Code"))
        item = self.tblwidget_subview.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Subject Name"))
        __sortingEnabled = self.tblwidget_subview.isSortingEnabled()
        self.tblwidget_subview.setSortingEnabled(False)
        self.tblwidget_subview.setSortingEnabled(__sortingEnabled)
        self.lbl_head.setText(_translate("Dialog", "Subject List"))
        #self.combo_sem.setItemText(0, _translate("Dialog", "S1"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ViewSubjects()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("View Subjects")
    Dialog.show()
    sys.exit(app.exec_())

