# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewquestions.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cx_Oracle

class Ui_Dialog(object):

    def loadData(self):
        self.tblwidget_qnview.setRowCount(0);
        con=cx_Oracle.connect('blooms/oracle@localhost:1521/xe')
        cur=con.cursor()
        sql="""
        select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
        from qns_tbl qt
        left outer join subject_tbl st on qt.sub_code = st.sub_code
        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
        order by st.sem,st.sub_name,qt.mdl,qt.mrk
        """
        #cur.execute(SQL, {'a' : 1}).fetchall()
        #[('X',)]
        cur.execute(sql)
        res=cur.fetchall()
        #print(res)
        self.tblwidget_qnview.setRowCount(len(res))
        for i in range (0,len(res)):
            for j in range(0,len(res[i])):
                item=QtWidgets.QTableWidgetItem(res[i][j])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblwidget_qnview.setItem(i, j, item)
        #print (res)
        #print(res[0][0])
        header = self.tblwidget_qnview.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        con.commit()
        cur.close()
        con.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1338, 657)
        self.tblwidget_qnview = QtWidgets.QTableWidget(Dialog)
        self.tblwidget_qnview.setGeometry(QtCore.QRect(10, 90, 1311, 192))
        self.tblwidget_qnview.setMinimumSize(QtCore.QSize(1311, 0))
        self.tblwidget_qnview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblwidget_qnview.setLineWidth(3)
        self.tblwidget_qnview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwidget_qnview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblwidget_qnview.setWordWrap(True)
        self.tblwidget_qnview.setRowCount(5)
        self.tblwidget_qnview.setColumnCount(8)
        self.tblwidget_qnview.setObjectName("tblwidget_qnview")
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblwidget_qnview.setHorizontalHeaderItem(7, item)
        self.tblwidget_qnview.verticalHeader().setDefaultSectionSize(31)
        self.loadData()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tblwidget_qnview.setSortingEnabled(False)
        item = self.tblwidget_qnview.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Question"))
        item = self.tblwidget_qnview.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Semester"))
        item = self.tblwidget_qnview.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Subject"))
        item = self.tblwidget_qnview.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Module"))
        item = self.tblwidget_qnview.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Mark"))
        item = self.tblwidget_qnview.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "K Level"))
        item = self.tblwidget_qnview.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Faculty Name"))
        item = self.tblwidget_qnview.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Faculty Emaiid"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

