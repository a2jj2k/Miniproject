# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registeration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import config
import emailInterface

class Ui_Registration(object):

    def showMessageBox(self,title,message):
        """ Function that displays warnings & info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def insertRegData(self):
        """ Function that enters registration data to the data base"""
        fname = self.txt_fname.text()
        mname = self.txt_mname.text()
        lname = self.txt_lname.text()
        emailid = self.txt_emailid.text()
        pswd = self.txt_pswd.text()
        cnfpswd = self.txt_cnfmpswd.text()
        usrtyp = self.combo_usrtyp.currentText()
        checker_flg=0
        if fname == "" or lname == "" or emailid == "" or pswd == "" or cnfpswd =="":
            self.showMessageBox('Warning','All Fields Except Middle Name Are Mandatory')
        else:
            mailid=emailid
            if "@" in mailid:
                if "." in mailid:
                    checker_flg=1
                else:
                    checker_flg=0
            else:
                checker_flg=0

            if checker_flg == 1:


                if (usrtyp == "Admin"):
                    flg=1
                else:
                    flg=0
                if(pswd==cnfpswd):
                    con=cx_Oracle.connect(config.connection)
                    cur=con.cursor()
                    cur.execute("""select * from user_tbl where email_id=:mid""",mid=emailid)
                    cur.fetchall()
                    if cur.rowcount > 0:
                        self.showMessageBox('Warning','User With The Entered Email Id Already Exist')
                        self.txt_emailid.setText('')
                    else:
                        pass
                        try:
                            #con=cx_Oracle.connect('blooms/oracle@localhost:1521/xe')
                            cur=con.cursor()
                            cur.execute("""insert into user_tbl values (:1,:2,:3,:4,:5,:6)""", (fname,mname,lname,emailid,pswd,flg))
                            #except DatabaseError:
                            #self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
                        except cx_Oracle.DatabaseError:
                            self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
                        else:
                            #cur.execute("""update id set id_val=(select (id_val+1) from id where id_desc='qn_code') where id_desc='qn_code'""")
                            con.commit()
                            con.close()
                            self.showMessageBox('Warning','User Added Successfully')
                            self.txt_fname.setText('')
                            self.txt_mname.setText('')
                            self.txt_lname.setText('')
                            self.txt_emailid.setText('')
                            self.txt_pswd.setText('')
                            self.txt_cnfmpswd.setText('')
                            emailInterface.welcomeEmailSndr(emailid,fname,mname,lname,pswd)

                else:
                    self.showMessageBox('Warning','Password Missmatch...Please Check')
            else:
                self.showMessageBox('Warning','Invalid Email Id')


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(752, 622)
        Dialog.setFixedSize(752,622)
        self.lb_fname = QtWidgets.QLabel(Dialog)
        self.lb_fname.setGeometry(QtCore.QRect(140, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_fname.setFont(font)
        self.lb_fname.setObjectName("lb_fname")
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(210, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.txt_fname = QtWidgets.QLineEdit(Dialog)
        self.txt_fname.setGeometry(QtCore.QRect(340, 130, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_fname.setFont(font)
        self.txt_fname.setObjectName("txt_fname")
        self.lb_mname = QtWidgets.QLabel(Dialog)
        self.lb_mname.setGeometry(QtCore.QRect(140, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_mname.setFont(font)
        self.lb_mname.setObjectName("lb_mname")
        self.txt_mname = QtWidgets.QLineEdit(Dialog)
        self.txt_mname.setGeometry(QtCore.QRect(340, 190, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_mname.setFont(font)
        self.txt_mname.setObjectName("txt_mname")
        self.lb_lname = QtWidgets.QLabel(Dialog)
        self.lb_lname.setGeometry(QtCore.QRect(140, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_lname.setFont(font)
        self.lb_lname.setObjectName("lb_lname")
        self.txt_lname = QtWidgets.QLineEdit(Dialog)
        self.txt_lname.setGeometry(QtCore.QRect(340, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_lname.setFont(font)
        self.txt_lname.setObjectName("txt_lname")
        self.lb_emailid = QtWidgets.QLabel(Dialog)
        self.lb_emailid.setGeometry(QtCore.QRect(140, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_emailid.setFont(font)
        self.lb_emailid.setObjectName("lb_emailid")
        self.txt_emailid = QtWidgets.QLineEdit(Dialog)
        self.txt_emailid.setGeometry(QtCore.QRect(340, 310, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_emailid.setFont(font)
        self.txt_emailid.setObjectName("txt_emailid")
        self.lb_pswd = QtWidgets.QLabel(Dialog)
        self.lb_pswd.setGeometry(QtCore.QRect(140, 370, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_pswd.setFont(font)
        self.lb_pswd.setObjectName("lb_pswd")
        self.lb_cnfmpswd = QtWidgets.QLabel(Dialog)
        self.lb_cnfmpswd.setGeometry(QtCore.QRect(140, 430, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_cnfmpswd.setFont(font)
        self.lb_cnfmpswd.setObjectName("lb_cnfmpswd")
        self.txt_pswd = QtWidgets.QLineEdit(Dialog)
        self.txt_pswd.setGeometry(QtCore.QRect(340, 370, 271, 31))
        self.txt_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pswd.setObjectName("txt_pswd")
        self.txt_cnfmpswd = QtWidgets.QLineEdit(Dialog)
        self.txt_cnfmpswd.setGeometry(QtCore.QRect(340, 430, 271, 31))
        self.txt_cnfmpswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_cnfmpswd.setObjectName("txt_cnfmpswd")
        self.btn_register = QtWidgets.QPushButton(Dialog)
        self.btn_register.setGeometry(QtCore.QRect(310, 560, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register.setFont(font)
        self.btn_register.setObjectName("btn_register")
        ###################
        self.btn_register.clicked.connect(self.insertRegData)
        ######################
        self.lb_usrtyp = QtWidgets.QLabel(Dialog)
        self.lb_usrtyp.setGeometry(QtCore.QRect(140, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_usrtyp.setFont(font)
        self.lb_usrtyp.setObjectName("lb_usrtyp")
        self.combo_usrtyp = QtWidgets.QComboBox(Dialog)
        self.combo_usrtyp.setGeometry(QtCore.QRect(340, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_usrtyp.setFont(font)
        self.combo_usrtyp.setObjectName("combo_usrtyp")
        self.combo_usrtyp.addItem("")
        self.combo_usrtyp.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Registration"))
        self.lb_fname.setText(_translate("Dialog", "First Name"))
        self.lbl_head.setText(_translate("Dialog", "Register Yourself Here"))
        self.lb_mname.setText(_translate("Dialog", "Middle Name"))
        self.lb_lname.setText(_translate("Dialog", "Last Name"))
        self.lb_emailid.setText(_translate("Dialog", "Email Id"))
        self.lb_pswd.setText(_translate("Dialog", "Password"))
        self.lb_cnfmpswd.setText(_translate("Dialog", "Confirm Password"))
        self.btn_register.setText(_translate("Dialog", "Register"))
        self.lb_usrtyp.setText(_translate("Dialog", "User Type"))
        self.combo_usrtyp.setItemText(0, _translate("Dialog", "Admin"))
        self.combo_usrtyp.setItemText(1, _translate("Dialog", "Default User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Dialog)
    #######################################################
    Dialog.setWindowTitle("User Registration")
    ##########################################################
    Dialog.show()
    sys.exit(app.exec_())

