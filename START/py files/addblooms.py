# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addblooms.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import config

class Ui_AddBloomsvrb(object):

    def showMessageBox(self,title,message):
        """ Function to display Warnings & Info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def initialLoading_klevel(self):
        """ Function to put initial values to the knowledge level combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select cd_val_desc from system_codes where code_type=203 order by cd_val_desc asc""")
        res=cur.fetchall()
        klevel=[]
        for i in range(0,cur.rowcount,1):
            klevel.append(str(res[i][0]))
        cur.close()
        con.close()
        return klevel

    def addBloomsVrb(self):
        """ Function to add blooms verb to the data base """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select id_val from id where id_desc='blm_code'""")
        res=cur.fetchall()
        bloomsm_code="blm"+str(res[0][0])
        blooms_verb=self.txt_bloomsvrb.text()
        klvl=self.combo_qlevel.currentText()
        """print(bloomsm_code)
        print(blooms_verb)
        print(klvl)"""
        if blooms_verb !="":
            try:
                con=cx_Oracle.connect(config.connection)
                cur=con.cursor()
                cur.execute("""insert into blooms_tbl values (:1,:2,:3)""",(bloomsm_code,blooms_verb,klvl))
            except cx_Oracle.DatabaseError:
                #except cx_Oracle.DatabaseError:
                self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
            else:
                cur.execute("""update id set id_val=(select (id_val+1) from id where id_desc='blm_code') where id_desc='blm_code'""")
                con.commit()
                con.close()
                self.showMessageBox('Warning','Blooms Verb Added Successfully')
                self.txt_bloomsvrb.setText('')
        else:
            self.showMessageBox('Warning','Please Enter A Blooms Verb')

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(499, 302)
        Dialog.setFixedSize(499,302)
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(60, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.txt_bloomsvrb = QtWidgets.QLineEdit(Dialog)
        self.txt_bloomsvrb.setGeometry(QtCore.QRect(240, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txt_bloomsvrb.setFont(font)
        self.txt_bloomsvrb.setObjectName("txt_bloomsvrb")
        self.lb_bloomsvrb = QtWidgets.QLabel(Dialog)
        self.lb_bloomsvrb.setGeometry(QtCore.QRect(60, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_bloomsvrb.setFont(font)
        self.lb_bloomsvrb.setObjectName("lb_bloomsvrb")
        self.combo_qlevel = QtWidgets.QComboBox(Dialog)
        self.combo_qlevel.setGeometry(QtCore.QRect(240, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_qlevel.setFont(font)
        self.combo_qlevel.setObjectName("combo_qlevel")
        #########################################################
        self.combo_qlevel.addItems(self.initialLoading_klevel())
        ########################################################
        self.lbl_desc = QtWidgets.QLabel(Dialog)
        self.lbl_desc.setGeometry(QtCore.QRect(60, 140, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc.setFont(font)
        self.lbl_desc.setObjectName("lbl_desc")
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(190, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        #####################################################
        self.btn_add.clicked.connect(self.addBloomsVrb)
        ###########################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Blooms Verb"))
        self.lbl_head.setText(_translate("Dialog", "Add Blooms Keywords Here"))
        self.lb_bloomsvrb.setText(_translate("Dialog", "Blooms Verb"))
        self.lbl_desc.setText(_translate("Dialog", "Knowledge Level"))
        self.btn_add.setText(_translate("Dialog", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddBloomsvrb()
    ui.setupUi(Dialog)
    #Dialog.setWindowTitle("Add Blooms Verb")
    Dialog.show()
    sys.exit(app.exec_())

