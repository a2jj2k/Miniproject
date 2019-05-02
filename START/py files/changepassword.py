# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import userdetails
import config

class Ui_ChangePswd(object):
    def showMessageBox(self,title,message):
        """ Function to display warnings & info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def changePassword(self):
        """ Function to update the password in db """
        crnt_pswd=self.txt_pwd_2.text()
        new_pswd=self.txt_pwd.text()
        cnfm_new_pswd=self.txt_pwd_3.text()
        if crnt_pswd == "" or new_pswd == "" or cnfm_new_pswd == "":
            self.showMessageBox('Warning','All Fields Are Mandatory')
        else:
            #self.showMessageBox('Warning','Ok')
            if userdetails.paswd == crnt_pswd:
                if new_pswd == cnfm_new_pswd:
                    try:
                        con=cx_Oracle.connect(config.connection)
                        cur=con.cursor()
                        cur.execute("""update user_tbl set pswd=:new_pswd where email_id=:mailid""",new_pswd=new_pswd,mailid=userdetails.emailid)
                    except cx_Oracle.DatabaseError:
                        self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
                    else:
                        con.commit()
                        con.close()
                        self.showMessageBox('Warning','Password Changed Successfully')
                        self.txt_pwd.setText('')
                        self.txt_pwd_2.setText('')
                        self.txt_pwd_3.setText('')
                else:
                    self.showMessageBox('Warning','Entered New Password Missmatch')
            else:
                self.showMessageBox('Warning','Current Password Is Wrong')


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(641, 394)
        Dialog.setFixedSize(641,394)
        self.lbl_newpswd = QtWidgets.QLabel(Dialog)
        self.lbl_newpswd.setGeometry(QtCore.QRect(60, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_newpswd.setFont(font)
        self.lbl_newpswd.setObjectName("lbl_newpswd")
        self.txt_pwd = QtWidgets.QLineEdit(Dialog)
        self.txt_pwd.setGeometry(QtCore.QRect(290, 160, 271, 31))
        self.txt_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pwd.setObjectName("txt_pwd")
        self.btn_chng_pswd = QtWidgets.QPushButton(Dialog)
        self.btn_chng_pswd.setGeometry(QtCore.QRect(240, 310, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_chng_pswd.setFont(font)
        self.btn_chng_pswd.setObjectName("btn_chng_pswd")
        #######################################################
        self.btn_chng_pswd.clicked.connect(self.changePassword)
        ##########################################################
        self.lbl_oldpswd = QtWidgets.QLabel(Dialog)
        self.lbl_oldpswd.setGeometry(QtCore.QRect(70, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_oldpswd.setFont(font)
        self.lbl_oldpswd.setObjectName("lbl_oldpswd")
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(140, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.txt_pwd_2 = QtWidgets.QLineEdit(Dialog)
        self.txt_pwd_2.setGeometry(QtCore.QRect(290, 100, 271, 31))
        self.txt_pwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pwd_2.setObjectName("txt_pwd_2")
        self.txt_pwd_3 = QtWidgets.QLineEdit(Dialog)
        self.txt_pwd_3.setGeometry(QtCore.QRect(290, 220, 271, 31))
        self.txt_pwd_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pwd_3.setObjectName("txt_pwd_3")
        self.lbl_pwd_2 = QtWidgets.QLabel(Dialog)
        self.lbl_pwd_2.setGeometry(QtCore.QRect(60, 220, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pwd_2.setFont(font)
        self.lbl_pwd_2.setObjectName("lbl_pwd_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txt_pwd_2, self.txt_pwd)
        Dialog.setTabOrder(self.txt_pwd, self.txt_pwd_3)
        Dialog.setTabOrder(self.txt_pwd_3, self.btn_chng_pswd)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Password"))
        self.lbl_newpswd.setText(_translate("Dialog", "New Password"))
        self.btn_chng_pswd.setText(_translate("Dialog", "Change Password"))
        self.lbl_oldpswd.setText(_translate("Dialog", "Old Password"))
        self.lbl_head.setText(_translate("Dialog", "Change Your Password Here"))
        self.lbl_pwd_2.setText(_translate("Dialog", "Confirm New Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ChangePswd()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Change Password")
    Dialog.show()
    sys.exit(app.exec_())

