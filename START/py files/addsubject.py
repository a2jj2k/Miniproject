# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSubject.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import config

class Ui_AddSubject(object):

    def showMessageBox(self,title,message):
        """ Function to display warnings & info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def clearAll(self):
        """ Function to clear text fields """
        self.txt_subcode.setText('')
        self.txt_subname.setText('')


    def addSubjectDetails(self):
        """ Function to add subject to the data base """
        sub_code = self.txt_subcode.text()
        sub_name = self.txt_subname.text()
        sem_val = self.combo_sem.currentText()

        if sub_code != "" and sub_name != "":
            con=cx_Oracle.connect(config.connection)
            cur=con.cursor()
            cur.execute("""select * from subject_tbl where sub_code = :sub_cd""",sub_cd=sub_code)
            cur.fetchall()
            #print(cur.rowcount)
            if(cur.rowcount > 0):
                self.showMessageBox('Warning','Subject Already Exist With The Same Subject Code')
                self.txt_subcode.setText('')
            else:
                try:
                    cur.execute("""insert into subject_tbl values (:1,:2,:3)""", (sub_code,sub_name,sem_val))
                #except DatabaseError:
                #self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
                except cx_Oracle.DatabaseError:
                    self.showMessageBox('Warning','Data Base Error Occured :: Contact System Admin\n Try Again')
                    self.clearAll()
                else:
                    con.commit()
                    con.close()
                    self.showMessageBox('Warning','Subject Added Successfully')
                    self.clearAll()
        else:
            self.showMessageBox('Warning','Please Enter All The Details')

    def setupUi(self, Dialog):
        #####################
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute('select cd_val_desc from system_codes where code_type=201')
        res=cur.fetchall()
        #print(res[1][0])
        #ress= list(cur)
        sem=[]
        for i in range(0,cur.rowcount,1):
            sem.append(str(res[i][0]))
        cur.close()
        con.close()
        ##########################
        Dialog.setObjectName("Dialog")
        #Dialog.resize(578, 432)
        Dialog.setFixedSize(578,432)
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(160, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.lb_subcode = QtWidgets.QLabel(Dialog)
        self.lb_subcode.setGeometry(QtCore.QRect(70, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_subcode.setFont(font)
        self.lb_subcode.setObjectName("lb_subcode")
        self.txt_subcode = QtWidgets.QLineEdit(Dialog)
        self.txt_subcode.setGeometry(QtCore.QRect(220, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_subcode.setFont(font)
        self.txt_subcode.setObjectName("txt_subcode")
        self.lb_subname = QtWidgets.QLabel(Dialog)
        self.lb_subname.setGeometry(QtCore.QRect(70, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_subname.setFont(font)
        self.lb_subname.setObjectName("lb_subname")
        self.txt_subname = QtWidgets.QLineEdit(Dialog)
        self.txt_subname.setGeometry(QtCore.QRect(220, 160, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_subname.setFont(font)
        self.txt_subname.setObjectName("txt_subname")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(70, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(220, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        ####################
        self.combo_sem.addItems(sem)
        ##########################
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(220, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        ######################################
        self.btn_add.clicked.connect(self.addSubjectDetails)
        ######################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Subject"))
        self.lbl_head.setText(_translate("Dialog", "Add Subjects Here"))
        self.lb_subcode.setText(_translate("Dialog", "Subject Code"))
        self.lb_subname.setText(_translate("Dialog", "Subject Name"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))
        self.btn_add.setText(_translate("Dialog", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddSubject()
    ui.setupUi(Dialog)
    #######################################################
    Dialog.setWindowTitle("Add Subject")
    #######################################################
    Dialog.show()
    sys.exit(app.exec_())

