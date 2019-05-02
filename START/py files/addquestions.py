# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addquestions.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
import userdetails
import config

class Ui_AddQuestions(object):

    def showMessageBox(self,title,message):
        """ Function to display Warnings & Info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

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

    def initialLoading_sub(self):
        """ Function to put initial values to the subject combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select sub_name from subject_tbl where sem='S1'""")
        res=cur.fetchall()
        sub=[]
        for i in range(0,cur.rowcount,1):
            sub.append(str(res[i][0]))
        cur.close()
        con.close()
        return sub

    def initialLoading_mod(self):
        """ Function to put initial values to the module combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select cd_val_desc from system_codes where code_type=202 order by cd_val_desc asc""")
        res=cur.fetchall()
        mod=[]
        for i in range(0,cur.rowcount,1):
            mod.append(str(res[i][0]))
        cur.close()
        con.close()

        return mod

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

    def initialLoading_qnmark(self):
        """ Function to put initial values to the mark combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select cd_val_desc from system_codes where code_type=204 order by cd_val_desc asc""")
        res=cur.fetchall()
        qnmark=[]
        for i in range(0,cur.rowcount,1):
            qnmark.append(str(res[i][0]))
        cur.close()
        con.close()
        return qnmark

    def subjectLoading(self):
        """ Function to load values to the subject combo box on the change event of semester combo box """
        sem_val=self.combo_sem.currentText()
        #print(sem_val)
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select sub_name from subject_tbl where sem=:sem_val order by sub_code""",sem_val=sem_val)
        res=cur.fetchall()
        subjects=[]
        for i in range(0,cur.rowcount,1):
            subjects.append(str(res[i][0]))
        #print(subjects)
        cur.close()
        con.close()
        self.combo_sub.clear()
        self.combo_sub.addItems(subjects)

    def predictorFunction(self):
        """ Function to predicts the knowledge level """
        qns = self.txt_qdsc.toPlainText()
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        try:
            cur.execute("""select * from blooms_tbl""")
            res=cur.fetchall()
        except cx_Oracle.DatabaseError:
            pass
        sem=[]
        for i in range(0,cur.rowcount,1):
            #print(res[i][1])
            #sem.append(str(res[i][0]))
            temp=str(res[i][1])
            if temp.upper() in qns.upper():
                self.combo_qlevel.setCurrentText(res[i][2])
                break;
            else:
                pass
        cur.close()
        con.close()

    def addQuestion(self):
        """ Function to add question to the data base """
        qn_desc=self.txt_qdsc.toPlainText()

        if qn_desc != "":
            con=cx_Oracle.connect(config.connection)
            cur=con.cursor()
            cur.execute("""select id_val from id where id_desc='qn_code'""")
            res=cur.fetchall()
            qn_code="qn"+str(res[0][0])
            #txt_=self.txt_qdsc.toPlainText()
            subject_name=self.combo_sub.currentText()
            #qn_desc=self.txt_qdsc.toPlainText()
            cur.execute("""select sub_code from subject_tbl where sub_name=:subject_name""",subject_name=subject_name)
            res=cur.fetchall()
            sub_code=str(res[0][0])
            module=self.combo_module.currentText()
            mark=int(self.combo_mark.currentText())
            klvl=self.combo_qlevel.currentText()
            facmailid=userdetails.emailid
            #print(sub_code)
            #print(facmailid)
            #print(qn_code,qn_desc,sub_code,module,mark,klvl,facmailid)
            try:
                con=cx_Oracle.connect(config.connection)
                cur=con.cursor()
                cur.execute("""insert into qns_tbl values (:1,:2,:3,:4,:5,:6,:7)""",(qn_code,qn_desc,sub_code,module,mark,klvl,facmailid))
            except cx_Oracle.DatabaseError:
                #except cx_Oracle.DatabaseError:
                self.showMessageBox('Warning','Data Base Error Occured::Contact System Admin')
            else:
                cur.execute("""update id set id_val=(select (id_val+1) from id where id_desc='qn_code') where id_desc='qn_code'""")
                con.commit()
                con.close()
                self.showMessageBox('Warning','Question Added Successfully')
                self.txt_qdsc.setText('')
        else:
            self.showMessageBox('Warning','Please Enter A Question Description')

    def setupUi(self, Dialog):
        #self.initialLoading()
        #print(userdetails.emailid)
        Dialog.setObjectName("Dialog")
        #Dialog.resize(915, 636)
        Dialog.setFixedSize(915,636)
        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(300, 20, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(70, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(320, 110, 77, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        ####################################################
        self.combo_sem.addItems(self.initialLoading_sem())
        self.combo_sem.currentIndexChanged.connect(self.subjectLoading)
        ############################### #######################
        self.lbl_sub = QtWidgets.QLabel(Dialog)
        self.lbl_sub.setGeometry(QtCore.QRect(70, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sub.setFont(font)
        self.lbl_sub.setObjectName("lbl_sub")
        self.combo_sub = QtWidgets.QComboBox(Dialog)
        self.combo_sub.setGeometry(QtCore.QRect(320, 170, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sub.setFont(font)
        self.combo_sub.setObjectName("combo_sub")
         ####################################################
        self.combo_sub.addItems(self.initialLoading_sub())
        ############################### #######################
        self.lbl_module = QtWidgets.QLabel(Dialog)
        self.lbl_module.setGeometry(QtCore.QRect(70, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_module.setFont(font)
        self.lbl_module.setObjectName("lbl_module")
        self.combo_module = QtWidgets.QComboBox(Dialog)
        self.combo_module.setGeometry(QtCore.QRect(320, 230, 77, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_module.setFont(font)
        self.combo_module.setObjectName("combo_module")
        ####################################################
        self.combo_module.addItems(self.initialLoading_mod())
        ############################### #######################
        self.lbl_desc = QtWidgets.QLabel(Dialog)
        self.lbl_desc.setGeometry(QtCore.QRect(70, 280, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc.setFont(font)
        self.lbl_desc.setObjectName("lbl_desc")
        self.combo_qlevel = QtWidgets.QComboBox(Dialog)
        self.combo_qlevel.setGeometry(QtCore.QRect(320, 290, 77, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_qlevel.setFont(font)
        self.combo_qlevel.setObjectName("combo_qlevel")
        ####################################################
        self.combo_qlevel.addItems(self.initialLoading_klevel())
        ############################### #######################
        self.lbl_desc_2 = QtWidgets.QLabel(Dialog)
        self.lbl_desc_2.setGeometry(QtCore.QRect(70, 430, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_desc_2.setFont(font)
        self.lbl_desc_2.setObjectName("lbl_desc_2")
        self.txt_qdsc = QtWidgets.QTextEdit(Dialog)
        self.txt_qdsc.setGeometry(QtCore.QRect(320, 410, 531, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.txt_qdsc.setFont(font)
        self.txt_qdsc.setObjectName("txt_qdsc")
        ##############################################
        self.txt_qdsc.textChanged.connect(self.predictorFunction)
        #############################################
        self.lbl_qmark = QtWidgets.QLabel(Dialog)
        self.lbl_qmark.setGeometry(QtCore.QRect(70, 340, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qmark.setFont(font)
        self.lbl_qmark.setObjectName("lbl_qmark")
        self.combo_mark = QtWidgets.QComboBox(Dialog)
        self.combo_mark.setGeometry(QtCore.QRect(320, 350, 77, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mark.setFont(font)
        self.combo_mark.setObjectName("combo_mark")
        ####################################################
        self.combo_mark.addItems(self.initialLoading_qnmark())
        ############################### #######################
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(390, 560, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        #####################################################
        self.btn_add.clicked.connect(self.addQuestion)
        ###########################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Questions"))
        self.lbl_head.setText(_translate("Dialog", "Add Your Question"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))
        self.combo_sem.setItemText(0, _translate("Dialog", "S1"))
        self.lbl_sub.setText(_translate("Dialog", "Subject"))
        self.lbl_module.setText(_translate("Dialog", "Module"))
        self.lbl_desc.setText(_translate("Dialog", "Knowledge Level"))
        self.lbl_desc_2.setText(_translate("Dialog", "Question Description"))
        self.lbl_qmark.setText(_translate("Dialog", "Question\'s Mark"))
        self.btn_add.setText(_translate("Dialog", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AddQuestions()
    ui.setupUi(Dialog)
    #Dialog.setWindowTitle("Add Questions")
    Dialog.show()
    sys.exit(app.exec_())

