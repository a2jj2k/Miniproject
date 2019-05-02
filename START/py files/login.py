#Original

# Form implementation generated from reading ui file 'logi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from homepage import Ui_HomePage
from functools import partial
import cx_Oracle
import config
import userdetails

class Ui_LogIn(object):

    def showMessageBox(self,title,message):
        """ Function that displays warnings & info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck(self,Dialog):
        """ Function that handles the log in """
        username = self.txt_id.text()
        password = self.txt_pwd.text()
        #print(username)
        #print(password)
        if username == "" and password == "":
            self.showMessageBox('Warning','Please Enter Username & Password')
        elif username == "" and password != "":
            self.showMessageBox('Warning','Please Enter Username')
        elif username != "" and password == "":
            self.showMessageBox('Warning','Please Enter Password')
        else:

            try:
                con=cx_Oracle.connect(config.connection)
                cur=con.cursor()
                cur.execute('select * from user_tbl where email_id=:1 and pswd=:2', (username, password))
                #cur.execute('select * from user_tbl')
                res=cur.fetchall()
            except cx_Oracle.DatabaseError:
                self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
            else:
                if(cur.rowcount > 0):
                    #print("User Found ! ")
                    userdetails.fname=res[0][0]
                    userdetails.mname=res[0][1]
                    userdetails.lname=res[0][2]
                    userdetails.emailid=res[0][3]
                    userdetails.paswd=res[0][4]
                    userdetails.adm_flg=res[0][5]
                    #self.showMessageBox('Warning','User Found !')
                    Dialog.close()
                    self.welcomeWindowShow()
                else:
                    #print("User Not Found !")
                #self.showMessageBox()
                    self.showMessageBox('Warning','Invalid Username And Password')
                    self.txt_id.setText('')
                    self.txt_pwd.setText('')
                    #self.welcomeWindowShow()
            con.close()

    def welcomeWindowShow(self):
        """ Function that loads the home page window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_HomePage()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(910, 522)
        Dialog.setFixedSize(910,522)
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(590, 410, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        ######################################
        #self.btn_login.clicked.connect(self.loginCheck)
        self.btn_login.clicked.connect(partial(self.loginCheck,Dialog))
        ######################################
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(400, 150, 20, 371))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 140, 911, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_id = QtWidgets.QLineEdit(Dialog)
        self.txt_id.setGeometry(QtCore.QRect(610, 230, 271, 31))
        ###############################################
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_id.setFont(font)
        ##############################################
        self.txt_id.setObjectName("txt_id")
        self.lbl_id = QtWidgets.QLabel(Dialog)
        self.lbl_id.setGeometry(QtCore.QRect(440, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_id.setFont(font)
        self.lbl_id.setObjectName("lbl_id")
        self.txt_pwd = QtWidgets.QLineEdit(Dialog)
        self.txt_pwd.setGeometry(QtCore.QRect(610, 330, 271, 31))
        self.txt_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        ############################################################3
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_id.setFont(font)
        ###########################################################
        self.txt_pwd.setObjectName("txt_pwd")
        self.lbl_pwd = QtWidgets.QLabel(Dialog)
        self.lbl_pwd.setGeometry(QtCore.QRect(440, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pwd.setFont(font)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.lbl_clg_name = QtWidgets.QLabel(Dialog)
        self.lbl_clg_name.setGeometry(QtCore.QRect(120, 20, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.lbl_clg_name.setFont(font)
        self.lbl_clg_name.setObjectName("lbl_clg_name")
        self.lbl_dpt_name = QtWidgets.QLabel(Dialog)
        self.lbl_dpt_name.setGeometry(QtCore.QRect(80, 70, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dpt_name.setFont(font)
        self.lbl_dpt_name.setObjectName("lbl_dpt_name")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 210, 401, 161))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: maroon")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 380, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Utsaah")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log In"))
        self.btn_login.setText(_translate("Dialog", "LOGIN"))
        self.lbl_id.setText(_translate("Dialog", "User Name"))
        self.lbl_pwd.setText(_translate("Dialog", "Password"))
        self.lbl_clg_name.setText(_translate("Dialog", "ST. JOSEPH\'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI"))
        self.lbl_dpt_name.setText(_translate("Dialog", "DEPARTMENT OF COMPUTER SCIENCE & APPLICATION"))
        self.label.setText(_translate("Dialog", "Everyone is a genius.\n"
"   But If you judge a fish\n"
"   on its ability to climb a tree,\n"
"   it will live its whole life believing it is stupid.\n"
"\n"
"Everyone has different, Abilities & Talents."))
        self.label_2.setText(_translate("Dialog", "- Albert Einstein"))

#import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LogIn()
    ui.setupUi(Dialog)
    #Dialog.setWindowTitle("Log In")
    Dialog.show()
    sys.exit(app.exec_())

