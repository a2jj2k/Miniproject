# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import cx_Oracle
import config
import userdetails

from addblooms import Ui_AddBloomsvrb
from addquestions import Ui_AddQuestions
from addsubject import Ui_AddSubject
from generateqnpaper import Ui_Generateqnpaper
from registration import Ui_Registration
from viewquestions import Ui_ViewQuestions
from viewsubjects import Ui_ViewSubjects
from viewusers import Ui_ViewUsers
from changepassword import Ui_ChangePswd

class Ui_HomePage(object):

    def logInWindowShow(self,Dialog):
        """ Function that loads log in window """
        Dialog.hide()
        from login import Ui_LogIn
        self.window=QtWidgets.QDialog()
        self.ui=Ui_LogIn()
        self.ui.setupUi(self.window)
        self.window.show()

    def addBlmsWindowShow(self,Dialog):
        """ Function that loads the add blooms verb window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_AddBloomsvrb()
        self.ui.setupUi(self.window)
        self.window.show()

    def addQnsWindowShow(self,Dialog):
        """ Function that loads the add question window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_AddQuestions()
        self.ui.setupUi(self.window)
        self.window.show()

    def addSbjtWindowShow(self,Dialog):
        """ Function that loads the add subject window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_AddSubject()
        self.ui.setupUi(self.window)
        self.window.show()

    def gnrtQnPprWindowShow(self,Dialog):
        """ Function that loads the generate qn paper window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Generateqnpaper()
        self.ui.setupUi(self.window)
        self.window.show()

    def regstrtnWindowShow(self,Dialog):
        """ Function that loads the user registration window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()

    def viewQnsWindowShow(self,Dialog):
        """ Function that loads the view qns window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ViewQuestions()
        self.ui.setupUi(self.window)
        self.window.show()

    def viewSbjtsWindowShow(self,Dialog):
        """ Function that loads the view subject window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ViewSubjects()
        self.ui.setupUi(self.window)
        self.window.show()

    def viewUsrsWindowShow(self,Dialog):
        """ Function that loads the view user window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ViewUsers()
        self.ui.setupUi(self.window)
        self.window.show()

    def chngPswdWindowShow(self,Dialog):
        """ Function that loads the change password window """
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ChangePswd()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(761, 546)
        Dialog.setFixedSize(761,546)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        self.frame_user = QtWidgets.QFrame(Dialog)
        self.frame_user.setGeometry(QtCore.QRect(40, 150, 321, 141))
        self.frame_user.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user.setLineWidth(1)
        self.frame_user.setMidLineWidth(0)
        self.frame_user.setObjectName("frame_user")
        self.label = QtWidgets.QLabel(self.frame_user)
        self.label.setGeometry(QtCore.QRect(140, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmdlnkbtn_user_add = QtWidgets.QCommandLinkButton(self.frame_user)
        self.cmdlnkbtn_user_add.setGeometry(QtCore.QRect(10, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_user_add.setFont(font)
        self.cmdlnkbtn_user_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_user_add.setObjectName("cmdlnkbtn_user_add")
        ###################################################################
        self.cmdlnkbtn_user_add.clicked.connect(partial(self.regstrtnWindowShow,Dialog))
        #################################################################
        self.cmdlnkbtn_user_view = QtWidgets.QCommandLinkButton(self.frame_user)
        self.cmdlnkbtn_user_view.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_user_view.setFont(font)
        self.cmdlnkbtn_user_view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_user_view.setObjectName("cmdlnkbtn_user_view")
        ###################################################################
        self.cmdlnkbtn_user_view.clicked.connect(partial(self.viewUsrsWindowShow,Dialog))
        #################################################################
        self.frame_quest = QtWidgets.QFrame(Dialog)
        self.frame_quest.setGeometry(QtCore.QRect(410, 150, 321, 141))
        self.frame_quest.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_quest.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_quest.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_quest.setLineWidth(1)
        self.frame_quest.setMidLineWidth(0)
        self.frame_quest.setObjectName("frame_quest")
        self.label_2 = QtWidgets.QLabel(self.frame_quest)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmdlnkbtn_qn_add = QtWidgets.QCommandLinkButton(self.frame_quest)
        self.cmdlnkbtn_qn_add.setGeometry(QtCore.QRect(10, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_qn_add.setFont(font)
        self.cmdlnkbtn_qn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_qn_add.setObjectName("cmdlnkbtn_qn_add")
         ###################################################################
        self.cmdlnkbtn_qn_add.clicked.connect(partial(self.addQnsWindowShow,Dialog))
        #################################################################
        self.cmdlnkbtn_qn_view = QtWidgets.QCommandLinkButton(self.frame_quest)
        self.cmdlnkbtn_qn_view.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_qn_view.setFont(font)
        self.cmdlnkbtn_qn_view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_qn_view.setObjectName("cmdlnkbtn_qn_view")
        ###################################################################
        self.cmdlnkbtn_qn_view.clicked.connect(partial(self.viewQnsWindowShow,Dialog))
        #################################################################
        self.frame_user_2 = QtWidgets.QFrame(Dialog)
        self.frame_user_2.setGeometry(QtCore.QRect(410, 310, 321, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_user_2.setFont(font)
        self.frame_user_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_user_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user_2.setObjectName("frame_user_2")
        self.label_3 = QtWidgets.QLabel(self.frame_user_2)
        self.label_3.setGeometry(QtCore.QRect(130, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cmdlnkbtn_chng_pswd = QtWidgets.QCommandLinkButton(self.frame_user_2)
        self.cmdlnkbtn_chng_pswd.setGeometry(QtCore.QRect(10, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_chng_pswd.setFont(font)
        self.cmdlnkbtn_chng_pswd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_chng_pswd.setObjectName("cmdlnkbtn_chng_pswd")
        ###################################################################
        self.cmdlnkbtn_chng_pswd.clicked.connect(partial(self.chngPswdWindowShow,Dialog))
        #################################################################
        self.cmdlnkbtn_add_blm_vrb = QtWidgets.QCommandLinkButton(self.frame_user_2)
        self.cmdlnkbtn_add_blm_vrb.setGeometry(QtCore.QRect(10, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_add_blm_vrb.setFont(font)
        self.cmdlnkbtn_add_blm_vrb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_add_blm_vrb.setObjectName("cmdlnkbtn_add_blm_vrb")
        ###################################################################
        self.cmdlnkbtn_add_blm_vrb.clicked.connect(partial(self.addBlmsWindowShow,Dialog))
        #################################################################
        self.frame_user_3 = QtWidgets.QFrame(Dialog)
        self.frame_user_3.setGeometry(QtCore.QRect(40, 310, 321, 141))
        self.frame_user_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_user_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user_3.setObjectName("frame_user_3")
        self.label_4 = QtWidgets.QLabel(self.frame_user_3)
        self.label_4.setGeometry(QtCore.QRect(130, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cmdlnkbtn_sub_add = QtWidgets.QCommandLinkButton(self.frame_user_3)
        self.cmdlnkbtn_sub_add.setGeometry(QtCore.QRect(10, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_sub_add.setFont(font)
        self.cmdlnkbtn_sub_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_sub_add.setObjectName("cmdlnkbtn_sub_add")
        ###################################################################
        self.cmdlnkbtn_sub_add.clicked.connect(partial(self.addSbjtWindowShow,Dialog))
        #################################################################
        self.cmdlnkbtn_sub_view = QtWidgets.QCommandLinkButton(self.frame_user_3)
        self.cmdlnkbtn_sub_view.setGeometry(QtCore.QRect(10, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_sub_view.setFont(font)
        self.cmdlnkbtn_sub_view.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_sub_view.setObjectName("cmdlnkbtn_sub_view")
        ###################################################################
        self.cmdlnkbtn_sub_view.clicked.connect(partial(self.viewSbjtsWindowShow,Dialog))
        #################################################################
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cmdlnkbtn_logout = QtWidgets.QCommandLinkButton(Dialog)
        self.cmdlnkbtn_logout.setGeometry(QtCore.QRect(640, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_logout.setFont(font)
        self.cmdlnkbtn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(config.image_fldr_path+"logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdlnkbtn_logout.setIcon(icon)
        self.cmdlnkbtn_logout.setObjectName("cmdlnkbtn_logout")
        ######################################################################
        self.cmdlnkbtn_logout.clicked.connect(partial(self.logInWindowShow,Dialog))
        #######################################################################
        self.cmdlnkbtn_gnrt_qn_ppr = QtWidgets.QCommandLinkButton(Dialog)
        self.cmdlnkbtn_gnrt_qn_ppr.setGeometry(QtCore.QRect(190, 480, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cmdlnkbtn_gnrt_qn_ppr.setFont(font)
        self.cmdlnkbtn_gnrt_qn_ppr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmdlnkbtn_gnrt_qn_ppr.setAutoFillBackground(False)
        self.cmdlnkbtn_gnrt_qn_ppr.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(config.image_fldr_path+"generate.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmdlnkbtn_gnrt_qn_ppr.setIcon(icon1)
        self.cmdlnkbtn_gnrt_qn_ppr.setCheckable(False)
        self.cmdlnkbtn_gnrt_qn_ppr.setObjectName("cmdlnkbtn_gnrt_qn_ppr")
        ###################################################################
        self.cmdlnkbtn_gnrt_qn_ppr.clicked.connect(partial(self.gnrtQnPprWindowShow,Dialog))
        #################################################################
        self.lbl_welcome = QtWidgets.QLabel(Dialog)
        self.lbl_welcome.setGeometry(QtCore.QRect(40, 70, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_welcome.setFont(font)
        self.lbl_welcome.setObjectName("lbl_welcome")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(280, 530, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:maroon")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home Page"))
        self.label.setText(_translate("Dialog", "USER"))
        self.cmdlnkbtn_user_add.setText(_translate("Dialog", "ADD"))
        self.cmdlnkbtn_user_view.setText(_translate("Dialog", "VIEW"))
        self.label_2.setText(_translate("Dialog", "QUESTION"))
        self.cmdlnkbtn_qn_add.setText(_translate("Dialog", "ADD"))
        self.cmdlnkbtn_qn_view.setText(_translate("Dialog", "VIEW"))
        self.label_3.setText(_translate("Dialog", "OTHERS"))
        self.cmdlnkbtn_chng_pswd.setText(_translate("Dialog", "CHANGE PASSWORD"))
        self.cmdlnkbtn_add_blm_vrb.setText(_translate("Dialog", "ADD BLOOMS VERB"))
        self.label_4.setText(_translate("Dialog", "SUBJECT"))
        self.cmdlnkbtn_sub_add.setText(_translate("Dialog", "ADD"))
        self.cmdlnkbtn_sub_view.setText(_translate("Dialog", "VIEW"))
        self.label_5.setText(_translate("Dialog", "QBManager"))
        self.cmdlnkbtn_logout.setText(_translate("Dialog", "LOG OUT"))
        self.cmdlnkbtn_gnrt_qn_ppr.setText(_translate("Dialog", "GENERATE QUESTION PAPER"))
        if userdetails.mname == None:
            disp_name=str(userdetails.fname)+" "+str(userdetails.lname)
        else:
            disp_name=str(userdetails.fname)+" "+str(userdetails.mname)+" "+str(userdetails.lname)
        self.lbl_welcome.setText(_translate("Dialog", "Welcome, "+disp_name))
        self.label_7.setText(_translate("Dialog", "©  R A V Technologies All Rights Reserved"))
        print(userdetails.adm_flg)
        if userdetails.adm_flg == 0:
            self.cmdlnkbtn_user_add.setEnabled(False)
            self.cmdlnkbtn_user_view.setEnabled(False)
            self.cmdlnkbtn_sub_add.setEnabled(False)
            self.cmdlnkbtn_add_blm_vrb.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_HomePage()
    ui.setupUi(Dialog)
    #Dialog.setWindowTitle("Home Page")
    Dialog.show()
    sys.exit(app.exec_())

