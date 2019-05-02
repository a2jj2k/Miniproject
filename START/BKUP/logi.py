# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import config

class Ui_Login(object):

    def showMessageBox(self,title,message):
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck(self):
        username = self.txt_id.text()
        password = self.txt_pwd.text()
        #print(username)
        #print(password)
        try:
            con=cx_Oracle.connect(config.connection)
            cur=con.cursor()
            cur.execute('select * from user_tbl where email_id=:1 and pswd=:2', (username, password))
            #cur.execute('select * from user_tbl')
            cur.fetchall()
        except cx_Oracle.DatabaseError:
            self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
        else:
            if(cur.rowcount > 0):
                #print("User Found ! ")
                self.showMessageBox('Warning','User Found !')
                #Dialog.hide()
                #self.welcomeWindowShow()
            else:
                #print("User Not Found !")
                #self.showMessageBox()
                self.showMessageBox('Warning','Invalid Username And Password')
                self.txt_id.setText('')
                self.txt_pwd.setText('')
                #self.welcomeWindowShow()
        con.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(910, 518)
        Dialog.setFixedSize(910,518)
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(590, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        ######################################
        self.btn_login.clicked.connect(self.loginCheck)
        ######################################
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(393, 120, 20, 401))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 110, 911, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_id = QtWidgets.QLineEdit(Dialog)
        self.txt_id.setGeometry(QtCore.QRect(610, 200, 271, 31))
        self.txt_id.setObjectName("txt_id")
        self.lbl_id = QtWidgets.QLabel(Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(440, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_id.setFont(font)
        self.lbl_id.setObjectName("lbl_id")
        self.txt_pwd = QtWidgets.QLineEdit(Dialog)
        self.txt_pwd.setGeometry(QtCore.QRect(610, 300, 271, 31))
        self.txt_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pwd.setObjectName("txt_pwd")
        self.lbl_pwd = QtWidgets.QLabel(Dialog)
        self.lbl_pwd.setGeometry(QtCore.QRect(440, 300, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pwd.setFont(font)
        self.lbl_pwd.setObjectName("lbl_pwd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_login.setText(_translate("Dialog", "LOGIN"))
        self.lbl_id.setText(_translate("Dialog", "User Name"))
        self.lbl_pwd.setText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    #######################################################
    Dialog.setWindowTitle("Login Form")
    ##########################################################
    Dialog.show()
    sys.exit(app.exec_())

