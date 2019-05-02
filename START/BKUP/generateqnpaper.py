# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generateqnpaper.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import cx_Oracle
import random
import os
import config
import bloomspdfwriter
from fpdf import FPDF

class Ui_Generateqnpaper(object):

    def showMessageBox(self,title,message):
        """ Function that display warnings & info """
        #QMessageBox.about(self, "Title", "Message")
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def chooser(self,names,limit):
        """ Function that choose random qn id's without repeatition """
        container=[]
        i=0
        while i <limit:
            random.shuffle(names)
            #print (random.choice(names))
            temp=(random.choice(names))
            if temp in container:
                random.shuffle(names)
            else:
                container.append(temp)
                random.shuffle(names)
                i=i+1
        return container

    def trimmer(self,ids):
        """ Function that trims and prepares the query input ids """
        q=""
        for i in ids:
            q=q+"'"+i+"'"+","
        q=q[0:len(q)-1]
        return q

    def qnPaperTypSelection(self):
        """ Function to enable and disable some widgets based on the type of examnation choosed """
        qnpprtyp = self.combo_exmtyp.currentText()

        if qnpprtyp == "University Examnation":
            try:
                #self.infoChanger()
                strng="Total no. of questions selected for PART A 0/8"
                self.lbl_qnstatus.setText(strng)
                #self.combo_sem.setEnabled(False)
                #self.combo_sub.setEnabled(False)
                #self.combo_mod1.setEnabled(False)
                #self.combo_mod2.setEnabled(False)
                #self.combo_mod3.setEnabled(False)
                #self.combo_mod4.setEnabled(False)
                #self.combo_mod5.setEnabled(False)
                #self.combo_mod6.setEnabled(False)
                #self.lbl_info.setEnabled(False)
                #self.lbl_mod1.setEnabled(False)
                #self.lbl_mod2.setEnabled(False)
                #self.lbl_mod3.setEnabled(False)
                #self.lbl_mod4.setEnabled(False)
                #self.lbl_mod5.setEnabled(False)
                #self.lbl_mod6.setEnabled(False)
                #self.lbl_qnstatus.hide()
                self.combo_mod1_2.setEnabled(False)
                self.combo_mod2_2.setEnabled(False)
                self.combo_mod3_2.setEnabled(False)
                self.combo_mod4_2.setEnabled(False)
                self.combo_mod5_2.setEnabled(False)
                self.combo_mod6_2.setEnabled(False)
                self.lbl_info_2.setEnabled(False)
                self.lbl_mod1_2.setEnabled(False)
                self.lbl_mod2_2.setEnabled(False)
                self.lbl_mod3_2.setEnabled(False)
                self.lbl_mod4_2.setEnabled(False)
                self.lbl_mod5_2.setEnabled(False)
                self.lbl_mod6_2.setEnabled(False)
                self.lbl_qnstatus_2.hide()
            except AttributeError:
                pass
        else:
            try:
                #self.combo_sem.setEnabled(True)
                #self.combo_sub.setEnabled(True)
                strng="Total no. of questions selected for PART A 0/5"
                self.lbl_qnstatus.setText(strng)
                self.combo_mod1.setEnabled(True)
                self.combo_mod2.setEnabled(True)
                self.combo_mod3.setEnabled(True)
                self.combo_mod4.setEnabled(True)
                self.combo_mod5.setEnabled(True)
                self.combo_mod6.setEnabled(True)
                self.lbl_info.setEnabled(True)
                self.lbl_mod1.setEnabled(True)
                self.lbl_mod2.setEnabled(True)
                self.lbl_mod3.setEnabled(True)
                self.lbl_mod4.setEnabled(True)
                self.lbl_mod5.setEnabled(True)
                self.lbl_mod6.setEnabled(True)
                self.lbl_qnstatus.show()
                self.combo_mod1_2.setEnabled(True)
                self.combo_mod2_2.setEnabled(True)
                self.combo_mod3_2.setEnabled(True)
                self.combo_mod4_2.setEnabled(True)
                self.combo_mod5_2.setEnabled(True)
                self.combo_mod6_2.setEnabled(True)
                self.lbl_info_2.setEnabled(True)
                self.lbl_mod1_2.setEnabled(True)
                self.lbl_mod2_2.setEnabled(True)
                self.lbl_mod3_2.setEnabled(True)
                self.lbl_mod4_2.setEnabled(True)
                self.lbl_mod5_2.setEnabled(True)
                self.lbl_mod6_2.setEnabled(True)
                self.lbl_qnstatus_2.show()
            except AttributeError:
                pass

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


    def subjectLoading(self):
        """ Function to load values to the subject combo box based on the change event of the semester combo box """
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

    def qnCountCalcPartA(self):
        """ Function that handles the no.of qns for part A & the information display """
        try:
            qnpprtyp = self.combo_exmtyp.currentText()
            if qnpprtyp == "Internal Examination":
                mod1_qncnt=int(self.combo_mod1.currentText())
                mod2_qncnt=int(self.combo_mod2.currentText())
                mod3_qncnt=int(self.combo_mod3.currentText())
                mod4_qncnt=int(self.combo_mod4.currentText())
                mod5_qncnt=int(self.combo_mod5.currentText())
                mod6_qncnt=int(self.combo_mod6.currentText())
                tot_cnt=mod1_qncnt+mod2_qncnt+mod3_qncnt+mod4_qncnt+mod5_qncnt+mod6_qncnt
                strng="Total no. of questions selected for PART A "+str(tot_cnt)+"/5"
                self.lbl_qnstatus.setText(strng)
                if tot_cnt == 5:
                    self.lbl_qnstatus.setStyleSheet('color: green')
                else:
                    self.lbl_qnstatus.setStyleSheet('color: red')
            else:
                mod1_qncnt=int(self.combo_mod1.currentText())
                mod2_qncnt=int(self.combo_mod2.currentText())
                mod3_qncnt=int(self.combo_mod3.currentText())
                mod4_qncnt=int(self.combo_mod4.currentText())
                mod5_qncnt=int(self.combo_mod5.currentText())
                mod6_qncnt=int(self.combo_mod6.currentText())
                tot_cnt=mod1_qncnt+mod2_qncnt+mod3_qncnt+mod4_qncnt+mod5_qncnt+mod6_qncnt
                strng="Total no. of questions selected for PART A "+str(tot_cnt)+"/8"
                self.lbl_qnstatus.setText(strng)
                if tot_cnt == 8:
                    self.lbl_qnstatus.setStyleSheet('color: green')
                else:
                    self.lbl_qnstatus.setStyleSheet('color: red')

        except ValueError:
            pass
        except AttributeError:
            pass

    def qnCountCalcPartB(self):
        """ Function that handles the no.of qns for part B & the information display """
        try:
            mod1_qncnt=int(self.combo_mod1_2.currentText())
            mod2_qncnt=int(self.combo_mod2_2.currentText())
            mod3_qncnt=int(self.combo_mod3_2.currentText())
            mod4_qncnt=int(self.combo_mod4_2.currentText())
            mod5_qncnt=int(self.combo_mod5_2.currentText())
            mod6_qncnt=int(self.combo_mod6_2.currentText())
            tot_cnt=mod1_qncnt+mod2_qncnt+mod3_qncnt+mod4_qncnt+mod5_qncnt+mod6_qncnt
            strng="Total no. of questions selected for PART B "+str(tot_cnt)+"/2"
            self.lbl_qnstatus_2.setText(strng)
            if tot_cnt == 2:
                self.lbl_qnstatus_2.setStyleSheet('color: green')
            else:
                self.lbl_qnstatus_2.setStyleSheet('color: red')
        except ValueError:
            pass
        except AttributeError:
            pass

    def pdfWritterIntrnlExm(self,result_a,result_b,subject,semester,exm_name):
        """ Function that writes the question paper of internal exam to pdf """
        part_a_1=result_a[0]
        part_a_2=result_a[1]
        part_a_3=result_a[2]
        part_a_4=result_a[3]
        part_a_5=result_a[4]

        part_b_1=result_b[0]
        part_b_2=result_b[1]

        pdf = FPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times', 'B', 14)
        pdf.image(config.image_fldr_path+"sjcet.png", 10, 15, 12)
        pdf.set_xy(30, 17)
        pdf.cell(0, 10, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", 0, 1)

        pdf.set_font('Times', '', 10)
        pdf.set_xy(81, 23)
        pdf.cell(0, 10, "(An ISO 9001: 2008 Certified College)", 0, 1)

        pdf.set_font('Times', 'B', 12)
        pdf.set_xy(62, 30)
        pdf.cell(0, 10, "DEPARTMENT OF COMPUTER APPLICATIONS", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 45)
        pdf.cell(0, 10, "Name of Examination : "+exm_name, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 50)
        pdf.cell(0, 10, "Subject                         : "+subject, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 55)
        pdf.cell(0, 10, "Semester                       : "+semester, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(18, 65)
        pdf.cell(0, 10, "Time: 1 Hour", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(170, 65)
        pdf.cell(0, 10, "Max.Marks: 15", 0, 1)

        pdf.set_font('Times', 'B', 12)
        pdf.set_xy(90, 80)
        pdf.cell(0, 10, "PART  A", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(57, 85)
        pdf.cell(0, 10, "(Each Question carries 3 marks, Answer any 3 questions)", 0, 1)
        pdf.ln(10)

        pdf.set_left_margin(18)
        effective_page_width = pdf.w - 1.7*pdf.l_margin
        orwidth= pdf.w - 10.0*pdf.l_margin
        pdf.set_font('Times','',11.0)

        #pdf.set_left_margin(18)
        pdf.multi_cell(effective_page_width, 5, "1.  "+part_a_1)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "2.  "+part_a_2)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "3.  "+part_a_3)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "4.  "+part_a_4)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "5.  "+part_a_5)
        pdf.ln(10)

        pdf.set_font('Times','B',12.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                     PART B")
        pdf.set_font('Times', 'B', 10)
        #pdf.cell(0, 10, "(Each Question carries 3 marks, Answer any 3 questions)", 0, 1)
        pdf.multi_cell(effective_page_width, 5, "                                         (Each Question carries 6 marks, Answer only one question)")

        pdf.ln(10)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "6.  "+part_b_1)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "7.  "+part_b_2)

        now = datetime.datetime.now()
        #file_name=subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        file_name=config.qn_output_path+subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        del_file=subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        #print(del_file)
        pdf.output(file_name, 'F')
        """try:
            os.startfile(file_name)
        except FileNotFoundError:
            pass"""
        return del_file

    def pdfWritterUnvrstyExm(self,result_a,result_b,subject,semester,exm_name):
        """ Function that writes the university question paper to pdf """
        #print("***********8")
        #print(result_a[0])
        part_a_1=result_a[0]
        part_a_2=result_a[1]
        part_a_3=result_a[2]
        part_a_4=result_a[3]
        part_a_5=result_a[4]
        part_a_6=result_a[5]
        part_a_7=result_a[6]
        part_a_8=result_a[7]


        part_b_1=result_b[0]
        part_b_2=result_b[1]
        part_b_3=result_b[2]
        part_b_4=result_b[3]
        part_b_5=result_b[4]
        part_b_6=result_b[5]
        part_b_7=result_b[6]
        part_b_8=result_b[7]
        part_b_9=result_b[8]
        part_b_10=result_b[9]
        part_b_11=result_b[10]
        part_b_12=result_b[11]

        pdf = FPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Times', 'B', 14)
        pdf.image(config.image_fldr_path+"sjcet.png", 10, 15, 12)
        pdf.set_xy(30, 17)
        pdf.cell(0, 10, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", 0, 1)

        pdf.set_font('Times', '', 10)
        pdf.set_xy(81, 23)
        pdf.cell(0, 10, "(An ISO 9001: 2008 Certified College)", 0, 1)

        pdf.set_font('Times', 'B', 12)
        pdf.set_xy(62, 30)
        pdf.cell(0, 10, "DEPARTMENT OF COMPUTER APPLICATIONS", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 45)
        pdf.cell(0, 10, "Name of Examination : "+exm_name, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 50)
        pdf.cell(0, 10, "Subject                         : "+subject, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(30, 55)
        pdf.cell(0, 10, "Semester                       : "+semester, 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(18, 65)
        pdf.cell(0, 10, "Time: 3 Hours", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(170, 65)
        pdf.cell(0, 10, "Max.Marks: 60", 0, 1)

        pdf.set_font('Times', 'B', 12)
        pdf.set_xy(90, 80)
        pdf.cell(0, 10, "PART  A", 0, 1)

        pdf.set_font('Times', 'B', 10)
        pdf.set_xy(57, 85)
        pdf.cell(0, 10, "(Each Question carries 3 marks, Answer all questions)", 0, 1)
        pdf.ln(10)

        pdf.set_left_margin(18)
        effective_page_width = pdf.w - 1.7*pdf.l_margin
        orwidth= pdf.w - 10.0*pdf.l_margin
        pdf.set_font('Times','',11.0)

        #pdf.set_left_margin(18)
        pdf.multi_cell(effective_page_width, 5, "1.  "+part_a_1)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "2.  "+part_a_2)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "3.  "+part_a_3)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "4.  "+part_a_4)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "5.  "+part_a_5)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "6.  "+part_a_6)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "7.  "+part_a_7)
        pdf.ln(1.0)

        pdf.multi_cell(effective_page_width, 5, "8.  "+part_a_8)
        pdf.ln(10)



        pdf.set_font('Times','B',12.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                     PART B")
        pdf.set_font('Times', 'B', 10)
        #pdf.cell(0, 10, "(Each Question carries 3 marks, Answer any 3 questions)", 0, 1)
        pdf.multi_cell(effective_page_width, 5, "                     (Answer any six questions, one full question from each module and carries 6 marks.)")

        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 1")

        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "9.  "+part_b_1)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "10.  "+part_b_2)

        pdf.ln(2)
        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 2")
        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "11.  "+part_b_3)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "12.  "+part_b_4)

        pdf.ln(2)
        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 3")
        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "13.  "+part_b_5)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "14.  "+part_b_6)

        pdf.ln(2)
        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 4")
        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "15.  "+part_b_7)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "16.  "+part_b_8)

        pdf.ln(2)
        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 5")
        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "17.  "+part_b_9)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "18.  "+part_b_10)

        pdf.ln(2)
        pdf.ln(5.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   Module 6")
        pdf.ln(3.5)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "19.  "+part_b_11)
        pdf.ln(1.0)
        pdf.set_font('Times','B',11.0)
        pdf.multi_cell(effective_page_width, 5, "                                                                                   OR")
        pdf.ln(2)
        pdf.set_font('Times','',11.0)
        pdf.multi_cell(effective_page_width, 5, "20.  "+part_b_12)

        now = datetime.datetime.now()
        #file_name=subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        file_name=config.qn_output_path+subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        del_file=subject+"_"+exm_name+"_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".pdf"
        pdf.output(file_name, 'F')
        """try:
            os.startfile(file_name)
        except FileNotFoundError:
            pass"""
        return del_file

    def questionChooserInternal(self):
        """ Function that chooses the questions for Internal exam """
        randomlypkdqns_parta=[]
        randomlypkdqns_partb=[]
        slctd_qns_parta=[]
        qnpprtyp = self.combo_exmtyp.currentText()
        if qnpprtyp == "Internal Examination":
            mod1_qncnt_a=int(self.combo_mod1.currentText())
            mod2_qncnt_a=int(self.combo_mod2.currentText())
            mod3_qncnt_a=int(self.combo_mod3.currentText())
            mod4_qncnt_a=int(self.combo_mod4.currentText())
            mod5_qncnt_a=int(self.combo_mod5.currentText())
            mod6_qncnt_a=int(self.combo_mod6.currentText())
            tot_cnt_parta=mod1_qncnt_a+mod2_qncnt_a+mod3_qncnt_a+mod4_qncnt_a+mod5_qncnt_a+mod6_qncnt_a
            #print(tot_cnt_parta)
            mod1_qncnt_b=int(self.combo_mod1_2.currentText())
            mod2_qncnt_b=int(self.combo_mod2_2.currentText())
            mod3_qncnt_b=int(self.combo_mod3_2.currentText())
            mod4_qncnt_b=int(self.combo_mod4_2.currentText())
            mod5_qncnt_b=int(self.combo_mod5_2.currentText())
            mod6_qncnt_b=int(self.combo_mod6_2.currentText())
            tot_cnt_partb=mod1_qncnt_b+mod2_qncnt_b+mod3_qncnt_b+mod4_qncnt_b+mod5_qncnt_b+mod6_qncnt_b
            #print(tot_cnt_partb)

            if tot_cnt_parta == 5 and tot_cnt_partb == 2:
                #print("Success")
                subject=self.combo_sub.currentText()
                #print(subject)
                con=cx_Oracle.connect(config.connection)
                cur_mod_1=con.cursor()
                cur_mod_2=con.cursor()
                cur_mod_3=con.cursor()
                cur_mod_4=con.cursor()
                cur_mod_5=con.cursor()
                cur_mod_6=con.cursor()

###################### code for choosing a part qn for internal exam begins here #########################

                cur_mod_1.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 1' and mrk='3'""",subject=subject)
                #cur_mod_1.fetchall()
                #print(cur_mod_1.rowcount)
                res_mod1=cur_mod_1.fetchall()
                #print(cur_mod_1.rowcount)
                #print("module 1")
                #print(res_mod1)
                qn_mod1=[]
                for i in range(0,cur_mod_1.rowcount,1):
                    qn_mod1.append(str(res_mod1[i][0]))

                cur_mod_2.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 2' and mrk='3'""",subject=subject)
                #cur_mod_2.fetchall()
                res_mod2=cur_mod_2.fetchall()
                #print("module 2")
                #print(res_mod2)
                qn_mod2=[]
                for i in range(0,cur_mod_2.rowcount,1):
                    qn_mod2.append(str(res_mod2[i][0]))

                cur_mod_3.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 3' and mrk='3'""",subject=subject)
                #cur_mod_3.fetchall()
                res_mod3=cur_mod_3.fetchall()
                #print("module 3")
                #print(res_mod3)
                qn_mod3=[]
                for i in range(0,cur_mod_3.rowcount,1):
                    qn_mod3.append(str(res_mod3[i][0]))

                cur_mod_4.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 4' and mrk='3'""",subject=subject)
                #cur_mod_4.fetchall()
                res_mod4=cur_mod_4.fetchall()
                #print("module 4")
                #print(res_mod4)
                qn_mod4=[]
                for i in range(0,cur_mod_4.rowcount,1):
                    qn_mod4.append(str(res_mod4[i][0]))

                cur_mod_5.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 5' and mrk='3'""",subject=subject)
                #cur_mod_5.fetchall()
                res_mod5=cur_mod_5.fetchall()
                #print("module 5")
                #print(res_mod5)
                qn_mod5=[]
                for i in range(0,cur_mod_5.rowcount,1):
                    qn_mod5.append(str(res_mod5[i][0]))

                cur_mod_6.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 6' and mrk='3'""",subject=subject)
                #cur_mod_6.fetchall()
                res_mod6=cur_mod_6.fetchall()
                #print("module 6")
                #print(res_mod6)
                qn_mod6=[]
                for i in range(0,cur_mod_6.rowcount,1):
                    qn_mod6.append(str(res_mod6[i][0]))

                if mod1_qncnt_a != 0:
                    if cur_mod_1.rowcount >= mod1_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod1,mod1_qncnt_a)
                    else:
                         self.showMessageBox('Warning','Not enough no.of PART A questions of Module 1 in Question Bank\n Please enter sufficient questions & Try Again')
                         return
                        #print("A part qns")
                        #print(randomlypkdqns_parta)

                if mod2_qncnt_a != 0:
                    if cur_mod_2.rowcount >= mod2_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod2,mod2_qncnt_a)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART A questions of Module 2 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod3_qncnt_a != 0:
                    if cur_mod_3.rowcount >= mod3_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod3,mod3_qncnt_a)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART A questions of Module 3 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod4_qncnt_a != 0:
                    if cur_mod_4.rowcount >= mod4_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod4,mod4_qncnt_a)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART A questions of Module 4 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod5_qncnt_a != 0:
                    if cur_mod_5.rowcount >= mod5_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod5,mod5_qncnt_a)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART A questions of Module 5 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod6_qncnt_a != 0:
                    if cur_mod_6.rowcount >= mod6_qncnt_a:
                        randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod6,mod6_qncnt_a)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART A questions of Module 6 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                slctd_ids_parta=self.trimmer(randomlypkdqns_parta)
                #print(slctd_ids_parta)
                cur=con.cursor()
                query="select qn_desc,blm_lvl from qns_tbl where qn_code in ("+slctd_ids_parta+")"
                cur.execute(query)
                result_a_temp=cur.fetchall()
                result_a=[]
                klevel_a=[]
                for i in range(0,cur.rowcount,1):
                    result_a.append(str(result_a_temp[i][0]))
                    for i in range(0,cur.rowcount,1):
                        klevel_a.append(str(result_a_temp[i][1]))
                """print("******************")
                print(cur.rowcount)
                print(result_a[0][0])
                print(result_a[1][0])
                print(result_a[2][0])
                print(result_a[3][0])
                print(result_a[4][0])"""

##################### code for choosing a part qn for internal exam ends here #############################

#################### code for choosing b part qn for internal exam begins here ############################

                cur_mod_1.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 1' and mrk='6'""",subject=subject)
                #cur_mod_1.fetchall()
                print(cur_mod_1.rowcount)
                res_mod1=cur_mod_1.fetchall()
                #print(cur_mod_1.rowcount)
                #print("module 1")
                #print(res_mod1)
                qn_mod1=[]
                for i in range(0,cur_mod_1.rowcount,1):
                    qn_mod1.append(str(res_mod1[i][0]))

                cur_mod_2.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 2' and mrk='6'""",subject=subject)
                #cur_mod_2.fetchall()
                res_mod2=cur_mod_2.fetchall()
                #print("module 2")
                #print(res_mod2)
                qn_mod2=[]
                for i in range(0,cur_mod_2.rowcount,1):
                    qn_mod2.append(str(res_mod2[i][0]))

                cur_mod_3.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 3' and mrk='6'""",subject=subject)
                #cur_mod_3.fetchall()
                res_mod3=cur_mod_3.fetchall()
                #print("module 3")
                #print(res_mod3)
                qn_mod3=[]
                for i in range(0,cur_mod_3.rowcount,1):
                    qn_mod3.append(str(res_mod3[i][0]))

                cur_mod_4.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 4' and mrk='6'""",subject=subject)
                #cur_mod_4.fetchall()
                res_mod4=cur_mod_4.fetchall()
                #print("module 4")
                #print(res_mod4)
                qn_mod4=[]
                for i in range(0,cur_mod_4.rowcount,1):
                    qn_mod4.append(str(res_mod4[i][0]))

                cur_mod_5.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 5' and mrk='6'""",subject=subject)
                #cur_mod_5.fetchall()
                res_mod5=cur_mod_5.fetchall()
                #print("module 5")
                #print(res_mod5)
                qn_mod5=[]
                for i in range(0,cur_mod_5.rowcount,1):
                    qn_mod5.append(str(res_mod5[i][0]))

                cur_mod_6.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 6' and mrk='6'""",subject=subject)
                #cur_mod_6.fetchall()
                res_mod6=cur_mod_6.fetchall()
                #print("module 6")
                #print(res_mod6)
                qn_mod6=[]
                for i in range(0,cur_mod_6.rowcount,1):
                    qn_mod6.append(str(res_mod6[i][0]))

                if mod1_qncnt_b != 0:
                    if cur_mod_1.rowcount >= mod1_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod1,mod1_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 1 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod2_qncnt_b != 0:
                    if cur_mod_2.rowcount >= mod2_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod2,mod2_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 2 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod3_qncnt_b != 0:
                    if cur_mod_3.rowcount >= mod3_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod3,mod3_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 3 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod4_qncnt_b != 0:
                    if cur_mod_4.rowcount >= mod4_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod4,mod4_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 4 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod5_qncnt_b != 0:
                    if cur_mod_5.rowcount >= mod5_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod5,mod5_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 5 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                if mod6_qncnt_b != 0:
                    if cur_mod_6.rowcount >= mod6_qncnt_b:
                        randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod6,mod6_qncnt_b)
                    else:
                        self.showMessageBox('Warning','Not enough no.of PART B questions of Module 6 in Question Bank\n Please enter sufficient questions & Try Again')
                        return

                #print(randomlypkdqns_partb)
                slctd_ids_partb=self.trimmer(randomlypkdqns_partb)
                #print(slctd_ids_partb)
                cur=con.cursor()
                query="select qn_desc,blm_lvl from qns_tbl where qn_code in ("+slctd_ids_partb+")"
                cur.execute(query)
                result_b_temp=cur.fetchall()
                result_b=[]
                klevel_b=[]
                for i in range(0,cur.rowcount,1):
                    result_b.append(str(result_b_temp[i][0]))
                    for i in range(0,cur.rowcount,1):
                        klevel_b.append(str(result_b_temp[i][1]))

                #print("******************")
                #print(cur.rowcount)
                #print(result_b[0][0])
                #print(result_b[1][0])
                #print(result_b[2][0])
                #print(result_b[3][0])
                #print(result_b[4][0])

########################### code for choosing b part qn for internal exam ends here ####################################
                subject=self.combo_sub.currentText()
                semester=self.combo_sem.currentText()
                exm_name=self.txt_id.text()
                temp=result_a+result_b
                cur.execute("""select sub_code from subject_tbl where sub_name=:subject""",subject=subject)
                temp=cur.fetchall()
                print("****************************************")
                subcode=temp[0][0]+" - "+subject
                subject=subcode
                del_file=self.pdfWritterIntrnlExm(result_a,result_b,subject,semester,exm_name)
                klevel=klevel_a+klevel_b
                bloomspdfwriter.pdfBloomsWriterInternal(klevel,subject,del_file)
                #os.remove(config.qn_output_path+"blooms.pdf")
                #self.pdfWritterIntrnlExm(result_a,result_b,subject,semester,exm_name)

            else:
                if tot_cnt_parta != 5:
                    self.showMessageBox('Warning','Total no.of questions from PART A should be 5')
                if tot_cnt_partb != 2:
                    self.showMessageBox('Warning','Total no.of questions from PART B should be 2')
        else:
            print("u choose univesrity exam")

    def questionChooserUniversity(self):
        """ Function that chooses the university exam questions """
        randomlypkdqns_parta=[]
        randomlypkdqns_partb=[]
        slctd_qns_parta=[]
        qnpprtyp = self.combo_exmtyp.currentText()
        if qnpprtyp == "University Examnation":
            mod1_qncnt_a=int(self.combo_mod1.currentText())
            mod2_qncnt_a=int(self.combo_mod2.currentText())
            mod3_qncnt_a=int(self.combo_mod3.currentText())
            mod4_qncnt_a=int(self.combo_mod4.currentText())
            mod5_qncnt_a=int(self.combo_mod5.currentText())
            mod6_qncnt_a=int(self.combo_mod6.currentText())
            tot_cnt_parta=mod1_qncnt_a+mod2_qncnt_a+mod3_qncnt_a+mod4_qncnt_a+mod5_qncnt_a+mod6_qncnt_a
            #print(tot_cnt_parta)
            mod1_qncnt_b=2
            mod2_qncnt_b=2
            mod3_qncnt_b=2
            mod4_qncnt_b=2
            mod5_qncnt_b=2
            mod6_qncnt_b=2
            tot_cnt_partb=mod1_qncnt_b+mod2_qncnt_b+mod3_qncnt_b+mod4_qncnt_b+mod5_qncnt_b+mod6_qncnt_b
            #print(tot_cnt_partb)

            if tot_cnt_parta == 8 and tot_cnt_partb == 12:
                if mod1_qncnt_a >= 1 and mod2_qncnt_a >= 1 and mod3_qncnt_a >= 1 and mod4_qncnt_a >= 1 and mod5_qncnt_a >= 1 and mod6_qncnt_a >= 1:

                    #print("Success")
                    subject=self.combo_sub.currentText()
                    #print(subject)
                    con=cx_Oracle.connect(config.connection)
                    cur_mod_1=con.cursor()
                    cur_mod_2=con.cursor()
                    cur_mod_3=con.cursor()
                    cur_mod_4=con.cursor()
                    cur_mod_5=con.cursor()
                    cur_mod_6=con.cursor()

###################### code for choosing a part qn for university exam begins here #########################

                    cur_mod_1.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 1' and mrk='3'""",subject=subject)
                    #cur_mod_1.fetchall()
                    #print(cur_mod_1.rowcount)
                    res_mod1=cur_mod_1.fetchall()
                    #print(cur_mod_1.rowcount)
                    #print("module 1")
                    #print(res_mod1)
                    qn_mod1=[]
                    for i in range(0,cur_mod_1.rowcount,1):
                        qn_mod1.append(str(res_mod1[i][0]))

                    cur_mod_2.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 2' and mrk='3'""",subject=subject)
                    #cur_mod_2.fetchall()
                    res_mod2=cur_mod_2.fetchall()
                    #print("module 2")
                    #print(res_mod2)
                    qn_mod2=[]
                    for i in range(0,cur_mod_2.rowcount,1):
                        qn_mod2.append(str(res_mod2[i][0]))

                    cur_mod_3.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 3' and mrk='3'""",subject=subject)
                    #cur_mod_3.fetchall()
                    res_mod3=cur_mod_3.fetchall()
                    #print("module 3")
                    #print(res_mod3)
                    qn_mod3=[]
                    for i in range(0,cur_mod_3.rowcount,1):
                        qn_mod3.append(str(res_mod3[i][0]))

                    cur_mod_4.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 4' and mrk='3'""",subject=subject)
                    #cur_mod_4.fetchall()
                    res_mod4=cur_mod_4.fetchall()
                    #print("module 4")
                    #print(res_mod4)
                    qn_mod4=[]
                    for i in range(0,cur_mod_4.rowcount,1):
                        qn_mod4.append(str(res_mod4[i][0]))

                    cur_mod_5.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 5' and mrk='3'""",subject=subject)
                    #cur_mod_5.fetchall()
                    res_mod5=cur_mod_5.fetchall()
                    #print("module 5")
                    #print(res_mod5)
                    qn_mod5=[]
                    for i in range(0,cur_mod_5.rowcount,1):
                        qn_mod5.append(str(res_mod5[i][0]))

                    cur_mod_6.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 6' and mrk='3'""",subject=subject)
                    #cur_mod_6.fetchall()
                    res_mod6=cur_mod_6.fetchall()
                    #print("module 6")
                    #print(res_mod6)
                    qn_mod6=[]
                    for i in range(0,cur_mod_6.rowcount,1):
                        qn_mod6.append(str(res_mod6[i][0]))

                    if mod1_qncnt_a != 0:
                        if cur_mod_1.rowcount >= mod1_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod1,mod1_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 1 in Question Bank\n Please enter sufficient questions & Try Again')
                            return


                    if mod2_qncnt_a != 0:
                        if cur_mod_2.rowcount >= mod2_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod2,mod2_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 2 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod3_qncnt_a != 0:
                        if cur_mod_3.rowcount >= mod3_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod3,mod3_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 3 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod4_qncnt_a != 0:
                        if cur_mod_4.rowcount >= mod4_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod4,mod4_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 4 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod5_qncnt_a != 0:
                        if cur_mod_5.rowcount >= mod5_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod5,mod5_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 5 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod6_qncnt_a != 0:
                        if cur_mod_6.rowcount >= mod6_qncnt_a:
                            randomlypkdqns_parta=randomlypkdqns_parta+self.chooser(qn_mod6,mod6_qncnt_a)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART A questions of Module 6 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    slctd_ids_parta=self.trimmer(randomlypkdqns_parta)
                    #print(slctd_ids_parta)
                    cur=con.cursor()
                    query="select qn_desc,blm_lvl from qns_tbl where qn_code in ("+slctd_ids_parta+")"
                    cur.execute(query)
                    result_a_temp=cur.fetchall()
                    result_a=[]
                    klevel_a=[]
                    for i in range(0,cur.rowcount,1):
                        result_a.append(str(result_a_temp[i][0]))
                    for i in range(0,cur.rowcount,1):
                        klevel_a.append(str(result_a_temp[i][1]))

                    print("resul a")
                    print(result_a)
                    print("klevel a")
                    print(klevel_a)

                    """print("******************")
                    print(cur.rowcount)
                    print(result_a[0][0])
                    print(result_a[1][0])
                    print(result_a[2][0])
                    print(result_a[3][0])
                    print(result_a[4][0])
                    print(result_a[5][0])
                    print(result_a[6][0])
                    print(result_a[7][0])"""


##################### code for choosing a part qn for university exam ends here #############################

#################### code for choosing b part qn for university exam begins here ############################

                    cur_mod_1.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 1' and mrk='6'""",subject=subject)
                    #cur_mod_1.fetchall()
                    print(cur_mod_1.rowcount)
                    res_mod1=cur_mod_1.fetchall()
                    #print(cur_mod_1.rowcount)
                    #print("module 1")
                    #print(res_mod1)
                    qn_mod1=[]
                    for i in range(0,cur_mod_1.rowcount,1):
                        qn_mod1.append(str(res_mod1[i][0]))

                    cur_mod_2.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 2' and mrk='6'""",subject=subject)
                    #cur_mod_2.fetchall()
                    res_mod2=cur_mod_2.fetchall()
                    #print("module 2")
                    #print(res_mod2)
                    qn_mod2=[]
                    for i in range(0,cur_mod_2.rowcount,1):
                        qn_mod2.append(str(res_mod2[i][0]))

                    cur_mod_3.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 3' and mrk='6'""",subject=subject)
                    #cur_mod_3.fetchall()
                    res_mod3=cur_mod_3.fetchall()
                    #print("module 3")
                    #print(res_mod3)
                    qn_mod3=[]
                    for i in range(0,cur_mod_3.rowcount,1):
                        qn_mod3.append(str(res_mod3[i][0]))

                    cur_mod_4.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 4' and mrk='6'""",subject=subject)
                    #cur_mod_4.fetchall()
                    res_mod4=cur_mod_4.fetchall()
                    #print("module 4")
                    #print(res_mod4)
                    qn_mod4=[]
                    for i in range(0,cur_mod_4.rowcount,1):
                        qn_mod4.append(str(res_mod4[i][0]))

                    cur_mod_5.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 5' and mrk='6'""",subject=subject)
                    #cur_mod_5.fetchall()
                    res_mod5=cur_mod_5.fetchall()
                    #print("module 5")
                    #print(res_mod5)
                    qn_mod5=[]
                    for i in range(0,cur_mod_5.rowcount,1):
                        qn_mod5.append(str(res_mod5[i][0]))

                    cur_mod_6.execute("""select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name=:subject) and mdl='Module 6' and mrk='6'""",subject=subject)
                    #cur_mod_6.fetchall()
                    res_mod6=cur_mod_6.fetchall()
                    #print("module 6")
                    #print(res_mod6)
                    qn_mod6=[]
                    for i in range(0,cur_mod_6.rowcount,1):
                        qn_mod6.append(str(res_mod6[i][0]))

                    if mod1_qncnt_b != 0:
                        if cur_mod_1.rowcount >= mod1_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod1,mod1_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 1 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod2_qncnt_b != 0:
                        if cur_mod_2.rowcount >= mod2_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod2,mod2_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 2 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod3_qncnt_b != 0:
                        if cur_mod_3.rowcount >= mod3_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod3,mod3_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 3 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod4_qncnt_b != 0:
                        if cur_mod_4.rowcount >= mod4_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod4,mod4_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 4 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod5_qncnt_b != 0:
                        if cur_mod_5.rowcount >= mod5_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod5,mod5_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 5 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    if mod6_qncnt_b != 0:
                        if cur_mod_6.rowcount >= mod6_qncnt_b:
                            randomlypkdqns_partb=randomlypkdqns_partb+self.chooser(qn_mod6,mod6_qncnt_b)
                        else:
                            self.showMessageBox('Warning','Not enough no.of PART B questions of Module 6 in Question Bank\n Please enter sufficient questions & Try Again')
                            return

                    #print(randomlypkdqns_partb)
                    slctd_ids_partb=self.trimmer(randomlypkdqns_partb)
                    #print(slctd_ids_partb)
                    cur=con.cursor()
                    query="select qn_desc,blm_lvl from qns_tbl where qn_code in ("+slctd_ids_partb+") order by mdl"
                    cur.execute(query)
                    result_b_temp=cur.fetchall()
                    result_b=[]
                    klevel_b=[]
                    for i in range(0,cur.rowcount,1):
                        result_b.append(str(result_b_temp[i][0]))
                    for i in range(0,cur.rowcount,1):
                        klevel_b.append(str(result_b_temp[i][1]))

                    print("resul b")
                    print(result_b)
                    print("klevel b")
                    print(klevel_b)

                    #print("******************")
                    #print(cur.rowcount)
                    #print(result_b[0][0])
                    #print(result_b[1][0])
                    #print(result_b[2][0])
                    #print(result_b[3][0])
                    #print(result_b[4][0])
                    #print(result_b[5][0])
                    #print(result_b[6][0])
                    #print(result_b[7][0])
                    #print(result_b[8][0])
                    #print(result_b[9][0])
                    #print(result_b[10][0])
                    #print(result_b[11][0])


########################### code for choosing b part qn for university exam ends here ####################################
                    subject=self.combo_sub.currentText()
                    semester=self.combo_sem.currentText()
                    exm_name=self.txt_id.text()
                    #query="select sub_code from qns_tbl where qn_code in ("+slctd_ids_partb+") order by mdl"
                    cur.execute("""select sub_code from subject_tbl where sub_name=:subject""",subject=subject)
                    temp=cur.fetchall()
                    print("****************************************")
                    subcode=temp[0][0]+" - "+subject
                    subject=subcode
                    #temp=result_a+result_b
                    #print(temp)
                    del_file=self.pdfWritterUnvrstyExm(result_a,result_b,subject,semester,exm_name)
                    klevel=klevel_a+klevel_b
                    bloomspdfwriter.pdfBloomsWriterUniversity(klevel,subject,del_file)
                else:
                    self.showMessageBox('Warning','There should be atleast one question from each module')

            else:
                if tot_cnt_parta != 8:
                    self.showMessageBox('Warning','Total no.of questions from PART A should be 8')
                if tot_cnt_partb != 12:
                    self.showMessageBox('Warning','Total no.of questions from PART B should be 12')
        else:
            print("u choose univesrity exam")

    def generateQnPaper(self):
        """ Function that trigers the qn paper generation  """
        qnpprtyp = self.combo_exmtyp.currentText()
        if qnpprtyp == "Internal Examination":
            self.questionChooserInternal()
        else:
            self.questionChooserUniversity()

    def infoChanger(self):
        """ Function that updates the info display """
        qnpprtyp = self.combo_exmtyp.currentText()
        if qnpprtyp=="University Examination":
            strng="Total no. of questions selected for PART A 0/8"
            self.lbl_qnstatus.setText(strng)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 671)
        Dialog.setFixedSize(770,671)

        """qnpprtyp = self.combo_exmtyp.currentText()
        if qnpprtyp=="University Examination":
            strng="Total no. of questions selected for PART A "+str(tot_cnt)+"/8"
            self.lbl_qnstatus.setText(strng)"""
        #self.infoChanger()

        self.lbl_head = QtWidgets.QLabel(Dialog)
        self.lbl_head.setGeometry(QtCore.QRect(150, 0, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_head.setFont(font)
        self.lbl_head.setObjectName("lbl_head")
        self.lb_exmtyp = QtWidgets.QLabel(Dialog)
        self.lb_exmtyp.setGeometry(QtCore.QRect(60, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_exmtyp.setFont(font)
        self.lb_exmtyp.setObjectName("lb_exmtyp")
        self.combo_exmtyp = QtWidgets.QComboBox(Dialog)
        self.combo_exmtyp.setGeometry(QtCore.QRect(280, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_exmtyp.setFont(font)
        self.combo_exmtyp.setObjectName("combo_exmtyp")
        ######################################################
        self.combo_exmtyp.currentIndexChanged.connect(self.qnPaperTypSelection)
        ###################################################################
        self.combo_exmtyp.addItem("")
        self.combo_exmtyp.addItem("")
        self.lbl_exmname = QtWidgets.QLabel(Dialog)
        self.lbl_exmname.setGeometry(QtCore.QRect(60, 150, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_exmname.setFont(font)
        self.lbl_exmname.setObjectName("lbl_exmname")
        self.txt_id = QtWidgets.QLineEdit(Dialog)
        self.txt_id.setGeometry(QtCore.QRect(280, 150, 431, 31))
        ###############################################################
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txt_id.setFont(font)
        ###############################################################
        self.txt_id.setObjectName("txt_id")
        self.lb_sem = QtWidgets.QLabel(Dialog)
        self.lb_sem.setGeometry(QtCore.QRect(60, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sem.setFont(font)
        self.lb_sem.setObjectName("lb_sem")
        self.combo_sem = QtWidgets.QComboBox(Dialog)
        self.combo_sem.setGeometry(QtCore.QRect(280, 210, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setObjectName("combo_sem")
        ##############################################################
        self.combo_sem.addItems(self.initialLoading_sem())
        self.combo_sem.currentIndexChanged.connect(self.subjectLoading)
        #############################################################
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.lbl_sub = QtWidgets.QLabel(Dialog)
        self.lbl_sub.setGeometry(QtCore.QRect(60, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sub.setFont(font)
        self.lbl_sub.setObjectName("lbl_sub")
        self.combo_sub = QtWidgets.QComboBox(Dialog)
        self.combo_sub.setGeometry(QtCore.QRect(280, 270, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sub.setFont(font)
        self.combo_sub.setObjectName("combo_sub")
        ######################################################
        self.combo_sub.addItems(self.initialLoading_sub())
        ########################################################
        self.lbl_info = QtWidgets.QLabel(Dialog)
        self.lbl_info.setGeometry(QtCore.QRect(60, 310, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info.setFont(font)
        self.lbl_info.setObjectName("lbl_info")
        self.lbl_mod1 = QtWidgets.QLabel(Dialog)
        self.lbl_mod1.setGeometry(QtCore.QRect(60, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod1.setFont(font)
        self.lbl_mod1.setObjectName("lbl_mod1")
        self.lbl_mod2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod2.setGeometry(QtCore.QRect(140, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod2.setFont(font)
        self.lbl_mod2.setObjectName("lbl_mod2")
        self.lbl_mod3 = QtWidgets.QLabel(Dialog)
        self.lbl_mod3.setGeometry(QtCore.QRect(220, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod3.setFont(font)
        self.lbl_mod3.setObjectName("lbl_mod3")
        self.lbl_mod4 = QtWidgets.QLabel(Dialog)
        self.lbl_mod4.setGeometry(QtCore.QRect(300, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod4.setFont(font)
        self.lbl_mod4.setObjectName("lbl_mod4")
        self.lbl_mod5 = QtWidgets.QLabel(Dialog)
        self.lbl_mod5.setGeometry(QtCore.QRect(380, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod5.setFont(font)
        self.lbl_mod5.setObjectName("lbl_mod5")
        self.lbl_mod6 = QtWidgets.QLabel(Dialog)
        self.lbl_mod6.setGeometry(QtCore.QRect(460, 360, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod6.setFont(font)
        self.lbl_mod6.setObjectName("lbl_mod6")
        self.combo_mod1 = QtWidgets.QComboBox(Dialog)
        self.combo_mod1.setGeometry(QtCore.QRect(70, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod1.setFont(font)
        self.combo_mod1.setObjectName("combo_mod1")
        ############################################################
        self.combo_mod1.currentIndexChanged.connect(self.qnCountCalcPartA)
        ##############################################################
        self.combo_mod1.addItem("")
        self.combo_mod1.addItem("")
        self.combo_mod1.addItem("")
        self.combo_mod1.addItem("")
        self.combo_mod1.addItem("")
        self.combo_mod1.addItem("")
        self.combo_mod2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod2.setGeometry(QtCore.QRect(150, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod2.setFont(font)
        self.combo_mod2.setObjectName("combo_mod2")
        ############################################################
        self.combo_mod2.currentIndexChanged.connect(self.qnCountCalcPartA)
        #################################################################
        self.combo_mod2.addItem("")
        self.combo_mod2.addItem("")
        self.combo_mod2.addItem("")
        self.combo_mod2.addItem("")
        self.combo_mod2.addItem("")
        self.combo_mod2.addItem("")
        self.combo_mod3 = QtWidgets.QComboBox(Dialog)
        self.combo_mod3.setGeometry(QtCore.QRect(230, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod3.setFont(font)
        self.combo_mod3.setObjectName("combo_mod3")
        ############################################################
        self.combo_mod3.currentIndexChanged.connect(self.qnCountCalcPartA)
        #################################################################
        self.combo_mod3.addItem("")
        self.combo_mod3.addItem("")
        self.combo_mod3.addItem("")
        self.combo_mod3.addItem("")
        self.combo_mod3.addItem("")
        self.combo_mod3.addItem("")
        self.combo_mod4 = QtWidgets.QComboBox(Dialog)
        self.combo_mod4.setGeometry(QtCore.QRect(310, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod4.setFont(font)
        self.combo_mod4.setObjectName("combo_mod4")
        ############################################################
        self.combo_mod4.currentIndexChanged.connect(self.qnCountCalcPartA)
        #################################################################
        self.combo_mod4.addItem("")
        self.combo_mod4.addItem("")
        self.combo_mod4.addItem("")
        self.combo_mod4.addItem("")
        self.combo_mod4.addItem("")
        self.combo_mod4.addItem("")
        self.combo_mod5 = QtWidgets.QComboBox(Dialog)
        self.combo_mod5.setGeometry(QtCore.QRect(390, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod5.setFont(font)
        self.combo_mod5.setObjectName("combo_mod5")
        ############################################################
        self.combo_mod5.currentIndexChanged.connect(self.qnCountCalcPartA)
        #################################################################
        self.combo_mod5.addItem("")
        self.combo_mod5.addItem("")
        self.combo_mod5.addItem("")
        self.combo_mod5.addItem("")
        self.combo_mod5.addItem("")
        self.combo_mod5.addItem("")
        self.combo_mod6 = QtWidgets.QComboBox(Dialog)
        self.combo_mod6.setGeometry(QtCore.QRect(470, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod6.setFont(font)
        self.combo_mod6.setObjectName("combo_mod6")
        ############################################################
        self.combo_mod6.currentIndexChanged.connect(self.qnCountCalcPartA)
        #################################################################
        self.combo_mod6.addItem("")
        self.combo_mod6.addItem("")
        self.combo_mod6.addItem("")
        self.combo_mod6.addItem("")
        self.combo_mod6.addItem("")
        self.combo_mod6.addItem("")
        self.lbl_qnstatus = QtWidgets.QLabel(Dialog)
        self.lbl_qnstatus.setGeometry(QtCore.QRect(60, 430, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qnstatus.setFont(font)
        self.lbl_qnstatus.setObjectName("lbl_qnstatus")
        self.lbl_qnstatus.setStyleSheet('color: red')
        self.btn_generate = QtWidgets.QPushButton(Dialog)
        self.btn_generate.setGeometry(QtCore.QRect(310, 610, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_generate.setFont(font)
        self.btn_generate.setObjectName("btn_generate")
        ######################################################
        self.btn_generate.clicked.connect(self.generateQnPaper)
         #####################################################
        self.lbl_mod2_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod2_2.setGeometry(QtCore.QRect(140, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod2_2.setFont(font)
        self.lbl_mod2_2.setObjectName("lbl_mod2_2")
        self.combo_mod2_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod2_2.setGeometry(QtCore.QRect(150, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod2_2.setFont(font)
        self.combo_mod2_2.setObjectName("combo_mod2_2")
        ############################################################
        self.combo_mod2_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod2_2.addItem("0")
        self.combo_mod2_2.addItem("1")
        self.combo_mod2_2.addItem("2")
        #self.combo_mod2_2.addItem("")
        #self.combo_mod2_2.addItem("")
        #self.combo_mod2_2.addItem("")
        self.combo_mod4_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod4_2.setGeometry(QtCore.QRect(310, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod4_2.setFont(font)
        self.combo_mod4_2.setObjectName("combo_mod4_2")
        ############################################################
        self.combo_mod4_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod4_2.addItem("0")
        self.combo_mod4_2.addItem("1")
        self.combo_mod4_2.addItem("2")
        #self.combo_mod4_2.addItem("")
        #self.combo_mod4_2.addItem("")
        #self.combo_mod4_2.addItem("")
        self.lbl_info_2 = QtWidgets.QLabel(Dialog)
        self.lbl_info_2.setGeometry(QtCore.QRect(60, 450, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info_2.setFont(font)
        self.lbl_info_2.setObjectName("lbl_info_2")
        self.combo_mod5_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod5_2.setGeometry(QtCore.QRect(390, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod5_2.setFont(font)
        self.combo_mod5_2.setObjectName("combo_mod5_2")
        ############################################################
        self.combo_mod5_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod5_2.addItem("0")
        self.combo_mod5_2.addItem("1")
        self.combo_mod5_2.addItem("2")
        #self.combo_mod5_2.addItem("")
        #self.combo_mod5_2.addItem("")
        #self.combo_mod5_2.addItem("")
        self.combo_mod6_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod6_2.setGeometry(QtCore.QRect(470, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod6_2.setFont(font)
        self.combo_mod6_2.setObjectName("combo_mod6_2")
        ############################################################
        self.combo_mod6_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod6_2.addItem("0")
        self.combo_mod6_2.addItem("1")
        self.combo_mod6_2.addItem("2")
        #self.combo_mod6_2.addItem("")
        #self.combo_mod6_2.addItem("")
        #self.combo_mod6_2.addItem("")
        self.lbl_mod6_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod6_2.setGeometry(QtCore.QRect(460, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod6_2.setFont(font)
        self.lbl_mod6_2.setObjectName("lbl_mod6_2")
        self.lbl_mod4_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod4_2.setGeometry(QtCore.QRect(300, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod4_2.setFont(font)
        self.lbl_mod4_2.setObjectName("lbl_mod4_2")
        self.lbl_mod3_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod3_2.setGeometry(QtCore.QRect(220, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod3_2.setFont(font)
        self.lbl_mod3_2.setObjectName("lbl_mod3_2")
        self.combo_mod3_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod3_2.setGeometry(QtCore.QRect(230, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod3_2.setFont(font)
        self.combo_mod3_2.setObjectName("combo_mod3_2")
        ############################################################
        self.combo_mod3_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod3_2.addItem("0")
        self.combo_mod3_2.addItem("1")
        self.combo_mod3_2.addItem("2")
        #self.combo_mod3_2.addItem("")
        #self.combo_mod3_2.addItem("")
        #self.combo_mod3_2.addItem("")
        self.combo_mod1_2 = QtWidgets.QComboBox(Dialog)
        self.combo_mod1_2.setGeometry(QtCore.QRect(70, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_mod1_2.setFont(font)
        self.combo_mod1_2.setObjectName("combo_mod1_2")
        ############################################################
        self.combo_mod1_2.currentIndexChanged.connect(self.qnCountCalcPartB)
        #################################################################
        self.combo_mod1_2.addItem("0")
        self.combo_mod1_2.addItem("1")
        self.combo_mod1_2.addItem("2")
        #self.combo_mod1_2.addItem("")
        #self.combo_mod1_2.addItem("")
        #self.combo_mod1_2.addItem("")
        self.lbl_mod5_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod5_2.setGeometry(QtCore.QRect(380, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod5_2.setFont(font)
        self.lbl_mod5_2.setObjectName("lbl_mod5_2")
        self.lbl_mod1_2 = QtWidgets.QLabel(Dialog)
        self.lbl_mod1_2.setGeometry(QtCore.QRect(60, 500, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mod1_2.setFont(font)
        self.lbl_mod1_2.setObjectName("lbl_mod1_2")
        self.lbl_qnstatus_2 = QtWidgets.QLabel(Dialog)
        self.lbl_qnstatus_2.setGeometry(QtCore.QRect(60, 570, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qnstatus_2.setFont(font)
        self.lbl_qnstatus_2.setObjectName("lbl_qnstatus_2")
        self.lbl_qnstatus_2.setStyleSheet('color: red')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate Question Paper"))
        self.lbl_head.setText(_translate("Dialog", "Generate Your Question Paper Here"))
        self.lb_exmtyp.setText(_translate("Dialog", "Examination Type"))
        self.combo_exmtyp.setItemText(0, _translate("Dialog", "Internal Examination"))
        self.combo_exmtyp.setItemText(1, _translate("Dialog", "University Examnation"))
        self.lbl_exmname.setText(_translate("Dialog", "<html><head/><body><p>Name of Examination</p></body></html>"))
        self.lb_sem.setText(_translate("Dialog", "Semester"))
        self.combo_sem.setItemText(0, _translate("Dialog", "S1"))
        self.combo_sem.setItemText(1, _translate("Dialog", "S2"))
        self.lbl_sub.setText(_translate("Dialog", "Subject"))
        self.lbl_info.setText(_translate("Dialog", "<html><head/><body><p>No. of Questions For PART A From Each Module</p></body></html>"))
        self.lbl_mod1.setText(_translate("Dialog", "Module  1"))
        self.lbl_mod2.setText(_translate("Dialog", "Module  2"))
        self.lbl_mod3.setText(_translate("Dialog", "Module  3"))
        self.lbl_mod4.setText(_translate("Dialog", "Module  4"))
        self.lbl_mod5.setText(_translate("Dialog", "Module  5"))
        self.lbl_mod6.setText(_translate("Dialog", "Module  6"))
        self.combo_mod1.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod1.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod1.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod1.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod1.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod1.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod2.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod3.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod3.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod3.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod3.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod3.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod3.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod4.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod4.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod4.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod4.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod4.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod4.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod5.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod5.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod5.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod5.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod5.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod5.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod6.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod6.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod6.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod6.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod6.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod6.setItemText(5, _translate("Dialog", "5"))
        self.lbl_qnstatus.setText(_translate("Dialog", "Total no. of questions selected for PART A  0/5"))
        self.btn_generate.setText(_translate("Dialog", "GENERATE"))
        self.lbl_mod2_2.setText(_translate("Dialog", "Module  2"))
        self.combo_mod2_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod2_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod2_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod2_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod2_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod2_2.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod4_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod4_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod4_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod4_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod4_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod4_2.setItemText(5, _translate("Dialog", "5"))
        self.lbl_info_2.setText(_translate("Dialog", "<html><head/><body><p>No. of Questions For PART B From Each Module</p></body></html>"))
        self.combo_mod5_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod5_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod5_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod5_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod5_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod5_2.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod6_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod6_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod6_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod6_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod6_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod6_2.setItemText(5, _translate("Dialog", "5"))
        self.lbl_mod6_2.setText(_translate("Dialog", "Module  6"))
        self.lbl_mod4_2.setText(_translate("Dialog", "Module  4"))
        self.lbl_mod3_2.setText(_translate("Dialog", "Module  3"))
        self.combo_mod3_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod3_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod3_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod3_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod3_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod3_2.setItemText(5, _translate("Dialog", "5"))
        self.combo_mod1_2.setItemText(0, _translate("Dialog", "0"))
        self.combo_mod1_2.setItemText(1, _translate("Dialog", "1"))
        self.combo_mod1_2.setItemText(2, _translate("Dialog", "2"))
        self.combo_mod1_2.setItemText(3, _translate("Dialog", "3"))
        self.combo_mod1_2.setItemText(4, _translate("Dialog", "4"))
        self.combo_mod1_2.setItemText(5, _translate("Dialog", "5"))
        self.lbl_mod5_2.setText(_translate("Dialog", "Module  5"))
        self.lbl_mod1_2.setText(_translate("Dialog", "Module  1"))
        self.lbl_qnstatus_2.setText(_translate("Dialog", "Total no. of questions selected for PART B  0/2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Generateqnpaper()
    ui.setupUi(Dialog)
    #Dialog.setWindowTitle("Generate Question Paper")
    Dialog.show()
    sys.exit(app.exec_())