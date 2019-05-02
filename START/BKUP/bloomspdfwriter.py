# Import FPDF class
from fpdf import FPDF
import config
from PyPDF2 import PdfFileMerger,PdfFileReader
import os

# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
def pdfBloomsWriterUniversity(klevel,subject,del_file):
    """ Function that writes the blooms taxonomy table of university qn paper to pdf """

    pdf=FPDF(format='letter', unit='in')

    # Add new page. Without this you cannot create the document.
    pdf.add_page()

    """pdf.set_font('Times', 'B', 14)
    pdf.image('sjcet.png', 10, 15, 12)
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
    pdf.cell(0, 10, "Name of Examination : First Internal", 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.set_xy(30, 50)
    pdf.cell(0, 10, "Subject                         : RLMCA 305-Mobile Computing", 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.set_xy(30, 55)
    pdf.cell(0, 10, "Semester                       : S5", 0, 1)"""



    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0)

    # Effective page width, or just epw
    epw = pdf.w - 2.3*pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw/8
    th = pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    """god="arun"

    data = [['qns / k lvl','1','2','3','4','5','6','7'],
    ['K1','!','!','!','!',god,'!','2'],
    ['K2','!','!','!','!','!','!','3'],
    ['K3','!','!','!','!','!','!','4'],
    ['K4','!','!','!','!','!','!','5'],
    ['K5','!','!','!','!','!','!','6'],
    ['K6','!','!','!','!','!','!','7']
    ]

    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times','B',14.0)
    pdf.cell(epw, 0.0, 'Demographic data', align='C')
    pdf.set_font('Times','',10.0)
    pdf.ln(0.5)

    # Text height is the same as current font size
    th = pdf.font_size

    for row in data:
    for datum in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(col_width, th, str(datum), border=1,align='C')

    pdf.ln(th)

    # Line break equivalent to 4 lines
    pdf.ln(4*th)"""


    pdf.image(config.image_fldr_path+"sjcet.png", 0.2, 0.5, 0.7)
    pdf.ln(0.5)
    #pdf.set_xy(30, 17)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", align='C')
    pdf.ln(0.5)
    #pdf.cell(0, 10, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", 0, 1)

    pdf.set_font('Times','B',10.0)
    pdf.cell(epw, 0.0, 'Blooms Taxonomy Evaluation', align='C')
    pdf.set_font('Times','',8.0)
    pdf.ln(0.5)

    pdf.set_font('Times','B',10.0)
    pdf.cell(epw, 0.0,subject, align='C')
    pdf.set_font('Times','',8.0)
    pdf.ln(0.5)

    col_width2 = epw/21

    #klevel=['K3','K2','K1','K2','K2','K1','K4','K5','K2','K6','K2','K1','K2','K3','K2','K4','K5','K1','K3','K2']

    k1=[]
    k2=[]
    k3=[]
    k4=[]
    k5=[]
    k6=[]
    test_0_0=test_0_1=test_0_2=test_0_3=test_0_4=test_0_5=test_0_6=test_0_7=test_0_8=test_0_9=test_0_10=test_0_11=test_0_12=test_0_13=test_0_14=test_0_15=test_0_16=test_0_17=test_0_18=test_0_19=""
    test_1_0=test_1_1=test_1_2=test_1_3=test_1_4=test_1_5=test_1_6=test_1_7=test_1_8=test_1_9=test_1_10=test_1_11=test_1_12=test_1_13=test_1_14=test_1_15=test_1_16=test_1_17=test_1_18=test_1_19=""
    test_2_0=test_2_1=test_2_2=test_2_3=test_2_4=test_2_5=test_2_6=test_2_7=test_2_8=test_2_9=test_2_10=test_2_11=test_2_12=test_2_13=test_2_14=test_2_15=test_2_16=test_2_17=test_2_18=test_2_19=""
    test_3_0=test_3_1=test_3_2=test_3_3=test_3_4=test_3_5=test_3_6=test_3_7=test_3_8=test_3_9=test_3_10=test_3_11=test_3_12=test_3_13=test_3_14=test_3_15=test_3_16=test_3_17=test_3_18=test_3_19=""
    test_4_0=test_4_1=test_4_2=test_4_3=test_4_4=test_4_5=test_4_6=test_4_7=test_4_8=test_4_9=test_4_10=test_4_11=test_4_12=test_4_13=test_4_14=test_4_15=test_4_16=test_4_17=test_4_18=test_4_19=""
    test_5_0=test_5_1=test_5_2=test_5_3=test_5_4=test_5_5=test_5_6=test_5_7=test_5_8=test_5_9=test_5_10=test_5_11=test_5_12=test_5_13=test_5_14=test_5_15=test_5_16=test_5_17=test_5_18=test_5_19=""
    k1per=k2per=k3per=k4per=k5per=k6per=""


    ########## Qn 1################
    if klevel[0] == "K1":
        test_0_0='3'
        k1.append(3)
    elif klevel[0] == "K2":
        test_1_0='3'
        k2.append(3)
    elif klevel[0] == "K3":
        test_2_0='3'
        k3.append(3)
    elif klevel[0] == "K4":
        test_3_0='3'
        k4.append(3)
    elif klevel[0] == "K5":
        test_4_0='3'
        k5.append(3)
    else:
        test_5_0='3'
        k6.append(3)

    ########## Qn 2################
    if klevel[1] == "K1":
        test_0_1='3'
        k1.append(3)
    elif klevel[1] == "K2":
        test_1_1='3'
        k2.append(3)
    elif klevel[1] == "K3":
        test_2_1='3'
        k3.append(3)
    elif klevel[1] == "K4":
        test_3_1='3'
        k4.append(3)
    elif klevel[1] == "K5":
        test_4_1='3'
        k5.append(3)
    else:
        test_5_1='3'
        k6.append(3)

    ########## Qn 3################
    if klevel[2] == "K1":
        test_0_2='3'
        k1.append(3)
    elif klevel[2] == "K2":
        test_1_2='3'
        k2.append(3)
    elif klevel[2] == "K3":
        test_2_2='3'
        k3.append(3)
    elif klevel[2] == "K4":
        test_3_2='3'
        k4.append(3)
    elif klevel[2] == "K5":
        test_4_2='3'
        k5.append(3)
    else:
        test_5_2='3'
        k6.append(3)

    ########## Qn 4 ################
    if klevel[3] == "K1":
        test_0_3='3'
        k1.append(3)
    elif klevel[3] == "K2":
        test_1_3='3'
        k2.append(3)
    elif klevel[3] == "K3":
        test_2_3='3'
        k3.append(3)
    elif klevel[3] == "K4":
        test_3_3='3'
        k4.append(3)
    elif klevel[3] == "K5":
        test_4_3='3'
        k5.append(3)
    else:
        test_5_3='3'
        k6.append(3)

    ########## Qn 5 ################
    if klevel[4] == "K1":
        test_0_4='3'
        k1.append(3)
    elif klevel[4] == "K2":
        test_1_4='3'
        k2.append(3)
    elif klevel[4] == "K3":
        test_2_4='3'
        k3.append(3)
    elif klevel[4] == "K4":
        test_3_4='3'
        k4.append(3)
    elif klevel[4] == "K5":
        test_4_4='3'
        k5.append(3)
    else:
        test_5_4='3'
        k6.append(3)

    ########## Qn 6 ################
    if klevel[5] == "K1":
        test_0_5='3'
        k1.append(3)
    elif klevel[5] == "K2":
        test_1_5='3'
        k2.append(3)
    elif klevel[5] == "K3":
        test_2_5='3'
        k3.append(3)
    elif klevel[5] == "K4":
        test_3_5='3'
        k4.append(3)
    elif klevel[5] == "K5":
        test_4_5='3'
        k5.append(3)
    else:
        test_5_5='3'
        k6.append(3)

    ########## Qn 7 ################
    if klevel[6] == "K1":
        test_0_6='3'
        k1.append(3)
    elif klevel[6] == "K2":
        test_1_6='3'
        k2.append(3)
    elif klevel[6] == "K3":
        test_2_6='3'
        k3.append(3)
    elif klevel[6] == "K4":
        test_3_6='3'
        k4.append(3)
    elif klevel[6] == "K5":
        test_4_6='3'
        k5.append(3)
    else:
        test_5_6='3'
        k6.append(3)

    ########## Qn 8 ################
    if klevel[7] == "K1":
        test_0_7='3'
        k1.append(3)
    elif klevel[7] == "K2":
        test_1_7='3'
        k2.append(3)
    elif klevel[7] == "K3":
        test_2_7='3'
        k3.append(3)
    elif klevel[7] == "K4":
        test_3_7='3'
        k4.append(3)
    elif klevel[7] == "K5":
        test_4_7='3'
        k5.append(3)
    else:
        test_5_7='3'
        k6.append(3)

    ########## Qn 9 ################
    if klevel[8] == "K1":
        test_0_8='6'
        k1.append(6)
    elif klevel[8] == "K2":
        test_1_8='6'
        k2.append(6)
    elif klevel[8] == "K3":
        test_2_8='6'
        k3.append(6)
    elif klevel[8] == "K4":
        test_3_8='6'
        k4.append(6)
    elif klevel[8] == "K5":
        test_4_8='6'
        k5.append(6)
    else:
        test_5_8='6'
        k6.append(6)

    ########## Qn 10 ################
    if klevel[9] == "K1":
        test_0_9='6'
        k1.append(6)
    elif klevel[9] == "K2":
        test_1_9='6'
        k2.append(6)
    elif klevel[9] == "K3":
        test_2_9='6'
        k3.append(6)
    elif klevel[9] == "K4":
        test_3_9='6'
        k4.append(6)
    elif klevel[9] == "K5":
        test_4_9='6'
        k5.append(6)
    else:
        test_5_9='6'
        k6.append(6)

    ########## Qn 11 ################
    if klevel[10] == "K1":
        test_0_10='6'
        k1.append(6)
    elif klevel[10] == "K2":
        test_1_10='6'
        k2.append(6)
    elif klevel[10] == "K3":
        test_2_10='6'
        k3.append(6)
    elif klevel[10] == "K4":
        test_3_10='6'
        k4.append(6)
    elif klevel[10] == "K5":
        test_4_10='6'
        k5.append(6)
    else:
        test_5_10='6'
        k6.append(6)

    ########## Qn 12 ################
    if klevel[11] == "K1":
        test_0_11='6'
        k1.append(6)
    elif klevel[11] == "K2":
        test_1_11='6'
        k2.append(6)
    elif klevel[11] == "K3":
        test_2_11='6'
        k3.append(6)
    elif klevel[11] == "K4":
        test_3_11='6'
        k4.append(6)
    elif klevel[11] == "K5":
        test_4_11='6'
        k5.append(6)
    else:
        test_5_11='6'
        k6.append(6)

    ########## Qn 13 ################
    if klevel[12] == "K1":
        test_0_12='6'
        k1.append(6)
    elif klevel[12] == "K2":
        test_1_12='6'
        k2.append(6)
    elif klevel[12] == "K3":
        test_2_12='6'
        k3.append(6)
    elif klevel[12] == "K4":
        test_3_12='6'
        k4.append(6)
    elif klevel[12] == "K5":
        test_4_12='6'
        k5.append(6)
    else:
        test_5_12='6'
        k6.append(6)

    ########## Qn 14 ################
    if klevel[13] == "K1":
        test_0_13='6'
        k1.append(6)
    elif klevel[13] == "K2":
        test_1_13='6'
        k2.append(6)
    elif klevel[13] == "K3":
        test_2_13='6'
        k3.append(6)
    elif klevel[13] == "K4":
        test_3_13='6'
        k4.append(6)
    elif klevel[13] == "K5":
        test_4_13='6'
        k5.append(6)
    else:
        test_5_13='6'
        k6.append(6)

    ########## Qn 15 ################
    if klevel[14] == "K1":
        test_0_14='6'
        k1.append(6)
    elif klevel[14] == "K2":
        test_1_14='6'
        k2.append(6)
    elif klevel[14] == "K3":
        test_2_14='6'
        k3.append(6)
    elif klevel[14] == "K4":
        test_3_14='6'
        k4.append(6)
    elif klevel[14] == "K5":
        test_4_14='6'
        k5.append(6)
    else:
        test_5_14='6'
        k6.append(6)

    ########## Qn 16 ################
    if klevel[15] == "K1":
        test_0_15='6'
        k1.append(6)
    elif klevel[15] == "K2":
        test_1_15='6'
        k2.append(6)
    elif klevel[15] == "K3":
        test_2_15='6'
        k3.append(6)
    elif klevel[15] == "K4":
        test_3_15='6'
        k4.append(6)
    elif klevel[15] == "K5":
        test_4_15='6'
        k5.append(6)
    else:
        test_5_15='6'
        k6.append(6)

    ########## Qn 17 ################
    if klevel[16] == "K1":
        test_0_16='6'
        k1.append(6)
    elif klevel[16] == "K2":
        test_1_16='6'
        k2.append(6)
    elif klevel[16] == "K3":
        test_2_16='6'
        k3.append(6)
    elif klevel[16] == "K4":
        test_3_16='6'
        k4.append(6)
    elif klevel[16] == "K5":
        test_4_16='6'
        k5.append(6)
    else:
        test_5_16='6'
        k6.append(6)

    ########## Qn 18 ################
    if klevel[17] == "K1":
        test_0_17='6'
        k1.append(6)
    elif klevel[17] == "K2":
        test_1_17='6'
        k2.append(6)
    elif klevel[17] == "K3":
        test_2_17='6'
        k3.append(6)
    elif klevel[17] == "K4":
        test_3_17='6'
        k4.append(6)
    elif klevel[17] == "K5":
        test_4_17='6'
        k5.append(6)
    else:
        test_5_17='6'
        k6.append(6)

    ########## Qn 19 ################
    if klevel[18] == "K1":
        test_0_18='6'
        k1.append(6)
    elif klevel[18] == "K2":
        test_1_18='6'
        k2.append(6)
    elif klevel[18] == "K3":
        test_2_18='6'
        k3.append(6)
    elif klevel[18] == "K4":
        test_3_18='6'
        k4.append(6)
    elif klevel[18] == "K5":
        test_4_18='6'
        k5.append(6)
    else:
        test_5_18='6'
        k6.append(6)

    ########## Qn 20 ################
    if klevel[19] == "K1":
        test_0_19='6'
        k1.append(6)
    elif klevel[19] == "K2":
        test_1_19='6'
        k2.append(6)
    elif klevel[19] == "K3":
        test_2_19='6'
        k3.append(6)
    elif klevel[19] == "K4":
        test_3_19='6'
        k4.append(6)
    elif klevel[19] == "K5":
        test_4_19='6'
        k5.append(6)
    else:
        test_5_19='6'
        k6.append(6)

    k1sum=sum(k1)
    k2sum=sum(k2)
    k3sum=sum(k3)
    k4sum=sum(k4)
    k5sum=sum(k5)
    k6sum=sum(k6)

    """print(k1sum)
    print(k2sum)
    print(k3sum)
    print(k4sum)
    print(k5sum)
    print(k6sum)"""

    k1per=round((k1sum/96)*100,4)
    k2per=round((k2sum/96)*100,4)
    k3per=round((k3sum/96)*100,4)
    k4per=round((k4sum/96)*100,4)
    k5per=round((k5sum/96)*100,4)
    k6per=round((k6sum/96)*100,4)
    #print(k1per)

    data1 = [['  ','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','%'],
    ['K1',test_0_0,test_0_1,test_0_2,test_0_3,test_0_4,test_0_5,test_0_6,test_0_7,test_0_8,test_0_9,test_0_10,test_0_11,test_0_12,test_0_13,test_0_14,test_0_15,test_0_16,test_0_17,test_0_18,test_0_19,k1per],
    ['K2',test_1_0,test_1_1,test_1_2,test_1_3,test_1_4,test_1_5,test_1_6,test_1_7,test_1_8,test_1_9,test_1_10,test_1_11,test_1_12,test_1_13,test_1_14,test_1_15,test_1_16,test_1_17,test_1_18,test_1_19,k2per],
    ['K3',test_2_0,test_2_1,test_2_2,test_2_3,test_2_4,test_2_5,test_2_6,test_2_7,test_2_8,test_2_9,test_2_10,test_2_11,test_2_12,test_2_13,test_2_14,test_2_15,test_2_16,test_2_17,test_2_18,test_2_19,k3per],
    ['K4',test_3_0,test_3_1,test_3_2,test_3_3,test_3_4,test_3_5,test_3_6,test_3_7,test_3_8,test_3_9,test_3_10,test_3_11,test_3_12,test_3_13,test_3_14,test_3_15,test_3_16,test_3_17,test_3_18,test_3_19,k4per],
    ['K5',test_4_0,test_4_1,test_4_2,test_4_3,test_4_4,test_4_5,test_4_6,test_4_7,test_4_8,test_4_9,test_4_10,test_4_11,test_4_12,test_4_13,test_4_14,test_4_15,test_4_16,test_4_17,test_4_18,test_4_19,k5per],
    ['K6',test_5_0,test_5_1,test_5_2,test_5_3,test_5_4,test_5_5,test_5_6,test_5_7,test_5_8,test_5_9,test_5_10,test_5_11,test_5_12,test_5_13,test_5_14,test_5_15,test_5_16,test_5_17,test_5_18,test_5_19,k6per]
    ]

    # Here we add more padding by passing 2*th as height
    for row in data1:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width2, 2*th, str(datum), border=1)

        pdf.ln(2*th)

    #pdf.output('E:\\KTU_MCA\\SEMESTER-5\\mini project\\START\\gnrtd qn papers\\table-using-cell-borders.pdf','F')
    #pdf.output(config.qn_output_path+"table-using-cell-borders.pdf",'F')
    pdf.output(config.qn_output_path+"blooms.pdf",'F')
    #E:\KTU_MCA\SEMESTER-5\mini project\START\gnrtd qn papers\\
    print(del_file)

    path=config.qn_output_path
    pdf_files=[del_file,"blooms.pdf"]
    merger=PdfFileMerger()
    for files in pdf_files:
        merger.append(path+files)
    merger.write(path+"Qp-"+del_file)
    merger.close()

    #config.qn_output_path+"blooms.pdf".close()
    try:
        os.remove(config.qn_output_path+"blooms.pdf")
        os.remove(config.qn_output_path+del_file)
        #os.remove(config.qn_output_path+del_file)
        os.startfile(path+"Qp-"+del_file)
    except FileNotFoundError:
        pass



def pdfBloomsWriterInternal(klevel,subject,del_file):
    """ Function that writes the blooms taxonomy table of internal exam to pdf """

    pdf=FPDF(format='letter', unit='in')

    # Add new page. Without this you cannot create the document.
    pdf.add_page()

    """pdf.set_font('Times', 'B', 14)
    pdf.image('sjcet.png', 10, 15, 12)
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
    pdf.cell(0, 10, "Name of Examination : First Internal", 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.set_xy(30, 50)
    pdf.cell(0, 10, "Subject                         : RLMCA 305-Mobile Computing", 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.set_xy(30, 55)
    pdf.cell(0, 10, "Semester                       : S5", 0, 1)"""



    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0)

    # Effective page width, or just epw
    epw = pdf.w - 2.3*pdf.l_margin

    # Set column width to 1/4 of effective page width to distribute content
    # evenly across table and page
    col_width = epw/8
    th = pdf.font_size

    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.

    """god="arun"

    data = [['qns / k lvl','1','2','3','4','5','6','7'],
    ['K1','!','!','!','!',god,'!','2'],
    ['K2','!','!','!','!','!','!','3'],
    ['K3','!','!','!','!','!','!','4'],
    ['K4','!','!','!','!','!','!','5'],
    ['K5','!','!','!','!','!','!','6'],
    ['K6','!','!','!','!','!','!','7']
    ]

    # Document title centered, 'B'old, 14 pt
    pdf.set_font('Times','B',14.0)
    pdf.cell(epw, 0.0, 'Demographic data', align='C')
    pdf.set_font('Times','',10.0)
    pdf.ln(0.5)

    # Text height is the same as current font size
    th = pdf.font_size

    for row in data:
    for datum in row:
        # Enter data in colums
        # Notice the use of the function str to coerce any input to the
        # string type. This is needed
        # since pyFPDF expects a string, not a number.
        pdf.cell(col_width, th, str(datum), border=1,align='C')

    pdf.ln(th)

    # Line break equivalent to 4 lines
    pdf.ln(4*th)"""


    pdf.image(config.image_fldr_path+"sjcet.png", 0.2, 0.5, 0.7)
    pdf.ln(0.5)
    #pdf.set_xy(30, 17)
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", align='C')
    pdf.ln(0.5)
    #pdf.cell(0, 10, "ST. JOSEPH'S COLLEGE OF ENGINEERING & TECHNOLOGY, PALAI", 0, 1)

    pdf.set_font('Times','B',10.0)
    pdf.cell(epw, 0.0, 'Blooms Taxonomy Evaluation', align='C')
    pdf.set_font('Times','',8.0)
    pdf.ln(0.5)

    pdf.set_font('Times','B',10.0)
    pdf.cell(epw, 0.0,subject, align='C')
    pdf.set_font('Times','',8.0)
    pdf.ln(0.5)

    col_width2 = epw/9

    #klevel=['K3','K2','K1','K2','K2','K1','K4','K5','K2','K6','K2','K1','K2','K3','K2','K4','K5','K1','K3','K2']

    k1=[]
    k2=[]
    k3=[]
    k4=[]
    k5=[]
    k6=[]
    test_0_0=test_0_1=test_0_2=test_0_3=test_0_4=test_0_5=test_0_6=""
    test_1_0=test_1_1=test_1_2=test_1_3=test_1_4=test_1_5=test_1_6=""
    test_2_0=test_2_1=test_2_2=test_2_3=test_2_4=test_2_5=test_2_6=""
    test_3_0=test_3_1=test_3_2=test_3_3=test_3_4=test_3_5=test_3_6=""
    test_4_0=test_4_1=test_4_2=test_4_3=test_4_4=test_4_5=test_4_6=""
    test_5_0=test_5_1=test_5_2=test_5_3=test_5_4=test_5_5=test_5_6=""
    k1per=k2per=k3per=k4per=k5per=k6per=""


    ########## Qn 1################
    if klevel[0] == "K1":
        test_0_0='3'
        k1.append(3)
    elif klevel[0] == "K2":
        test_1_0='3'
        k2.append(3)
    elif klevel[0] == "K3":
        test_2_0='3'
        k3.append(3)
    elif klevel[0] == "K4":
        test_3_0='3'
        k4.append(3)
    elif klevel[0] == "K5":
        test_4_0='3'
        k5.append(3)
    else:
        test_5_0='3'
        k6.append(3)

    ########## Qn 2################
    if klevel[1] == "K1":
        test_0_1='3'
        k1.append(3)
    elif klevel[1] == "K2":
        test_1_1='3'
        k2.append(3)
    elif klevel[1] == "K3":
        test_2_1='3'
        k3.append(3)
    elif klevel[1] == "K4":
        test_3_1='3'
        k4.append(3)
    elif klevel[1] == "K5":
        test_4_1='3'
        k5.append(3)
    else:
        test_5_1='3'
        k6.append(3)

    ########## Qn 3################
    if klevel[2] == "K1":
        test_0_2='3'
        k1.append(3)
    elif klevel[2] == "K2":
        test_1_2='3'
        k2.append(3)
    elif klevel[2] == "K3":
        test_2_2='3'
        k3.append(3)
    elif klevel[2] == "K4":
        test_3_2='3'
        k4.append(3)
    elif klevel[2] == "K5":
        test_4_2='3'
        k5.append(3)
    else:
        test_5_2='3'
        k6.append(3)

    ########## Qn 4 ################
    if klevel[3] == "K1":
        test_0_3='3'
        k1.append(3)
    elif klevel[3] == "K2":
        test_1_3='3'
        k2.append(3)
    elif klevel[3] == "K3":
        test_2_3='3'
        k3.append(3)
    elif klevel[3] == "K4":
        test_3_3='3'
        k4.append(3)
    elif klevel[3] == "K5":
        test_4_3='3'
        k5.append(3)
    else:
        test_5_3='3'
        k6.append(3)

    ########## Qn 5 ################
    if klevel[4] == "K1":
        test_0_4='3'
        k1.append(3)
    elif klevel[4] == "K2":
        test_1_4='3'
        k2.append(3)
    elif klevel[4] == "K3":
        test_2_4='3'
        k3.append(3)
    elif klevel[4] == "K4":
        test_3_4='3'
        k4.append(3)
    elif klevel[4] == "K5":
        test_4_4='3'
        k5.append(3)
    else:
        test_5_4='3'
        k6.append(3)

    ########## Qn 6 ################
    if klevel[5] == "K1":
        test_0_5='6'
        k1.append(6)
    elif klevel[5] == "K2":
        test_1_5='6'
        k2.append(6)
    elif klevel[5] == "K3":
        test_2_5='6'
        k3.append(6)
    elif klevel[5] == "K4":
        test_3_5='6'
        k4.append(6)
    elif klevel[5] == "K5":
        test_4_5='6'
        k5.append(6)
    else:
        test_5_5='6'
        k6.append(6)

    ########## Qn 7 ################
    if klevel[6] == "K1":
        test_0_6='6'
        k1.append(6)
    elif klevel[6] == "K2":
        test_1_6='6'
        k2.append(6)
    elif klevel[6] == "K3":
        test_2_6='6'
        k3.append(6)
    elif klevel[6] == "K4":
        test_3_6='6'
        k4.append(6)
    elif klevel[6] == "K5":
        test_4_6='6'
        k5.append(6)
    else:
        test_5_6='6'
        k6.append(6)


    k1sum=sum(k1)
    k2sum=sum(k2)
    k3sum=sum(k3)
    k4sum=sum(k4)
    k5sum=sum(k5)
    k6sum=sum(k6)

    print(k1sum)
    print(k2sum)
    print(k3sum)
    print(k4sum)
    print(k5sum)
    print(k6sum)

    k1per=round((k1sum/27)*100,4)
    k2per=round((k2sum/27)*100,4)
    k3per=round((k3sum/27)*100,4)
    k4per=round((k4sum/27)*100,4)
    k5per=round((k5sum/27)*100,4)
    k6per=round((k6sum/27)*100,4)
    #print(k1per)

    data1 = [['  ','1','2','3','4','5','6','7','%'],
    ['K1',test_0_0,test_0_1,test_0_2,test_0_3,test_0_4,test_0_5,test_0_6,k1per],
    ['K2',test_1_0,test_1_1,test_1_2,test_1_3,test_1_4,test_1_5,test_1_6,k2per],
    ['K3',test_2_0,test_2_1,test_2_2,test_2_3,test_2_4,test_2_5,test_2_6,k3per],
    ['K4',test_3_0,test_3_1,test_3_2,test_3_3,test_3_4,test_3_5,test_3_6,k4per],
    ['K5',test_4_0,test_4_1,test_4_2,test_4_3,test_4_4,test_4_5,test_4_6,k5per],
    ['K6',test_5_0,test_5_1,test_5_2,test_5_3,test_5_4,test_5_5,test_5_6,k6per]
    ]

    # Here we add more padding by passing 2*th as height
    for row in data1:
        for datum in row:
            # Enter data in colums
            pdf.cell(col_width2, 2*th, str(datum), border=1)

        pdf.ln(2*th)

    #pdf.output('E:\\KTU_MCA\\SEMESTER-5\\mini project\\START\\gnrtd qn papers\\table-using-cell-borders.pdf','F')
    pdf.output(config.qn_output_path+"blooms.pdf",'F')
    #E:\KTU_MCA\SEMESTER-5\mini project\START\gnrtd qn papers\\
    print(del_file)

    path=config.qn_output_path
    pdf_files=[del_file,"blooms.pdf"]
    merger=PdfFileMerger()
    for files in pdf_files:
        merger.append(path+files)
    merger.write(path+"Qp-"+del_file)
    merger.close()

    #config.qn_output_path+"blooms.pdf".close()
    try:
        os.remove(config.qn_output_path+"blooms.pdf")
        os.remove(config.qn_output_path+del_file)
        #os.remove(config.qn_output_path+del_file)
        os.startfile(path+"Qp-"+del_file)
    except FileNotFoundError:
        pass



#klevel=['K3','K2','K1','K2','K2','K1','K4']
#pdfBloomsWriterInternal(klevel)
