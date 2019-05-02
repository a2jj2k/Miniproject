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
import config

class Ui_ViewQuestions(object):

    def trimmer(self,ids):
        """ Function that trims and returns the id in ready format """
        q=""
        for i in ids:
            #print(i)
            q=q+"'"+i+"'"+","
        q=q[0:len(q)-1]
        return q

    def loadData(self):
        """ Function that loads the initial data to the qtable widget """
        self.tblwidget_qnview.setRowCount(0);
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        sql="""
        select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
        from qns_tbl qt
        left outer join subject_tbl st on qt.sub_code = st.sub_code
        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
        where st.SEM='S1'
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

    def showMessageBox(self,title,message):
        """ Function that displays warnings & info """
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
        cur.execute("""select sub_name from subject_tbl""")
        res=cur.fetchall()
        sub=["All"]
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
        mod=["All"]

        #mod.append("All")
        for i in range(0,cur.rowcount,1):
            mod.append(str(res[i][0]))
        cur.close()
        con.close()
        #mod.append(str("All"))
        #print(mod)
        return mod

    def initialLoading_mark(self):
        """ Function to put initial values to the mark combo box """
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        cur.execute("""select cd_val_desc from system_codes where code_type=204 order by cd_val_desc asc""")
        res=cur.fetchall()
        mrk=["All"]
        for i in range(0,cur.rowcount,1):
            mrk.append(str(res[i][0]))
        cur.close()
        con.close()
        return mrk

    def subjectLoading(self):
        """ Function that loads values to the subject combo box based on the change event of semester combo box """
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

    def searchQuestions(self):
        """ Function that searches and updtes the qtable widget  """
        semester=self.combo_sem.currentText()
        subject=self.combo_sub.currentText()
        module=self.combo_module.currentText()
        mark=self.combo_mark.currentText()
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()

        if ( subject=="All" and module=="All" and mark=="All" ):
            #### To search for questions of a particular semester,all subjects,all module and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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

        elif( module=="All" and mark=="All" ):
            #### To search for questions of a particular semester,all module and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester and st.sub_name=:subject
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,subject=subject)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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

        elif( subject=="All" and mark=="All" ):
            #### To search for questions of a particular semester,all subjects and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=&semester and qt.mdl=:module
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,module=module)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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

        elif( subject=="All" and module=="All"):
            #### To search for questions of a particular semester,all subjects and all modules ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=&semester and qt.mrk=:mark
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,mark=mark)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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
        ######################################
        elif( subject == "All"):
            #### To search for questions of a particular semester,all module and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester  and qt.mdl=:module and qt.mrk=:mark
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,module=module,mark=mark)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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
        ######################################
        elif( mark == "All"):
            #### To search for questions of a particular semester,all module and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester and st.sub_name=:subject and qt.mdl=:module and st.sub_name=:subject
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,module=module,subject=subject)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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
            #######################################################################################

        elif( module == "All"):

            #### To search for questions of a particular semester,all module and all marks ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester and st.sub_name=:subject and qt.mrk=:mark and st.sub_name=:subject
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,mark=mark,subject=subject)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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

        else:
            #### Fully customised search ##########
            cur.execute("""select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM=:semester and st.sub_name=:subject and qt.mdl=:module and qt.mrk=:mark
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk""",semester=semester,subject=subject,module=module,mark=mark)
            res=cur.fetchall()
            #print(res)
            self.tblwidget_qnview.setRowCount(0)
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
        cur.close()
        con.close()


    def deleteData(self):
        """ Function that deletes the selected rows of data from data base and qtable widget """
        #print(self.tblwidget_qnview.selectionModel().selectedRows().row())
        print(self.tblwidget_qnview.selectionModel().selectedRows())
        #print(self.tblwidget_qnview.selectionModel().selectedIndexes())
        """indexes = self.tblwidget_qnview.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())"""
        """for currentQTableWidgetItem in self.tblwidget_qnview.selectionModel().selectedRows():
            print(currentQTableWidgetItem.text())"""
        indexes = self.tblwidget_qnview.selectionModel().selectedRows()
        #str=""
        rowtext = []
        for index in sorted(indexes):
            row = index.row()
            #rowtext = []
            #for c in range(self.tblwidget_qnview.columnCount()):
            rowtext.append(self.tblwidget_qnview.item(row, 0).text())
            #str=str+self.tblwidget_qnview.item(row, 0).text()+','
            #print(rowtext)
        #print('-------------')
        #print(rowtext)
        qns=self.trimmer(rowtext)
        #print("***************")
        #print(temp)
        con=cx_Oracle.connect(config.connection)
        cur=con.cursor()
        query="select qn_code from qns_tbl where qn_desc in ("+qns+")"
        try:

            cur.execute(query)
            res=cur.fetchall()
        except cx_Oracle.DatabaseError:
            pass
        #cur.fetchall()

        result=[]
        for i in range(0,cur.rowcount,1):
            result.append(str(res[i][0]))
            #result=result+str(res[i][0])
            #print(res[i][0])


        deletingids=self.trimmer(result)
        print("****************")
        print(deletingids)

        if deletingids != "":

            try:

                query="delete from qns_tbl where qn_code in ("+deletingids+")"
                cur.execute(query)
            except cx_Oracle.DatabaseError:
                pass
            else:
                con.commit()
                cur.close()
                con.close()
                self.showMessageBox('Warning','Questions Successfully Deleted')
                self.searchQuestions()
        else:
            self.showMessageBox('Warning','Please Select Atleast One Question to Delete')



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(1332, 610)
        Dialog.setFixedSize(1332,610)
        self.tblwidget_qnview = QtWidgets.QTableWidget(Dialog)
        self.tblwidget_qnview.setGeometry(QtCore.QRect(10, 90, 1311, 491))
        self.tblwidget_qnview.setMinimumSize(QtCore.QSize(1311, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.tblwidget_qnview.setFont(font)
        self.tblwidget_qnview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tblwidget_qnview.setLineWidth(3)
        self.tblwidget_qnview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblwidget_qnview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)#impo
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
        self.tblwidget_qnview.verticalHeader().setDefaultSectionSize(50) ####impo
        self.lbl_sub = QtWidgets.QLabel(Dialog)
        self.lbl_sub.setGeometry(QtCore.QRect(310, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sub.setFont(font)
        self.lbl_sub.setObjectName("lbl_sub")
        self.combo_sub = QtWidgets.QComboBox(Dialog)
        self.combo_sub.setGeometry(QtCore.QRect(200, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sub.setFont(font)
        self.combo_sub.setObjectName("combo_sub")
        #########################################################
        self.combo_sub.addItems(self.initialLoading_sub())
        #############################################################
        self.combo_module = QtWidgets.QComboBox(Dialog)
        self.combo_module.setGeometry(QtCore.QRect(520, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_module.setFont(font)
        self.combo_module.setObjectName("combo_module")
        #########################################################
        #self.combo_module.addItem("All")
        self.combo_module.addItems(self.initialLoading_mod())
        #############################################################
        #self.combo_module.addItem("")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(90, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")
        self.lbl_module = QtWidgets.QLabel(Dialog)
        self.lbl_module.setGeometry(QtCore.QRect(530, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_module.setFont(font)
        self.lbl_module.setObjectName("lbl_module")
        self.lbl_qmark = QtWidgets.QLabel(Dialog)
        self.lbl_qmark.setGeometry(QtCore.QRect(660, 10, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qmark.setFont(font)
        self.lbl_qmark.setObjectName("lbl_qmark")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(90, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        #########################################################
        self.combo_sem.addItems(self.initialLoading_sem())
        self.combo_sem.currentIndexChanged.connect(self.subjectLoading)
        #############################################################
        #self.combo_sem.addItem("")
        self.combo_mark = QtWidgets.QComboBox(Dialog)
        self.combo_mark.setGeometry(QtCore.QRect(650, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mark.setFont(font)
        self.combo_mark.setObjectName("combo_mark")
         #########################################################
        self.combo_mark.addItems(self.initialLoading_mark())
        #############################################################
        self.btn_search = QtWidgets.QPushButton(Dialog)
        self.btn_search.setGeometry(QtCore.QRect(760, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        #####################################################
        self.btn_search.clicked.connect(self.searchQuestions)
        ###########################################################
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setGeometry(QtCore.QRect(890, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        #####################################################
        self.btn_delete.clicked.connect(self.deleteData)
        ###########################################################
        self.loadData()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Questions"))
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
        #self.tblwidget_qnview.verticalHeader().setDefaultSectionSize(31)
        item.setText(_translate("Dialog", "Faculty Emaiid"))
        self.lbl_sub.setText(_translate("Dialog", "Subject"))
        #self.combo_module.setItemText(0, _translate("Dialog", "All"))
        #self.combo_mark.setItemText(0, _translate("Dialog", "All"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))
        self.lbl_module.setText(_translate("Dialog", "Module"))
        self.lbl_qmark.setText(_translate("Dialog", "Mark"))
        self.combo_sem.setItemText(0, _translate("Dialog", "S1"))
        self.btn_search.setText(_translate("Dialog", "Search"))
        self.btn_delete.setText(_translate("Dialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ViewQuestions()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("View Questions")
    Dialog.show()
    sys.exit(app.exec_())

