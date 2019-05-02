""" File that does the inital data base set up """
import cx_Oracle
import config

def setUpApplication():
    checker=1
    con=cx_Oracle.connect(config.connection)
    cur=con.cursor()
    try:
        cur.execute("""DROP TABLE qns_tbl""")
        cur.execute("""DROP TABLE blooms_tbl""")
        cur.execute("""DROP TABLE id""")
        cur.execute("""DROP TABLE subject_tbl""")
        cur.execute("""DROP TABLE system_codes""")
        cur.execute("""DROP TABLE user_tbl""")
    except cx_Oracle.DatabaseError:
        checker=0
    try:
        cur.execute("""CREATE TABLE user_tbl(
                    first_name VARCHAR2(40) NOT NULL,
                    middle_name VARCHAR2(40),
                    last_name VARCHAR2(40),
                    email_id VARCHAR2(50),
                    pswd VARCHAR2(50),
                    adm_flg NUMBER(1),
                    PRIMARY KEY (email_id)
                    )""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE user_tbl CREATED")

    try:
        cur.execute("""CREATE TABLE system_codes(
                    code_id NUMBER(3),
                    code_val NUMBER(2),
                    code_type NUMBER(4),
                    cd_val_desc VARCHAR2(20),
                    cd_typ_desc VARCHAR2(20),
                    PRIMARY KEY (code_id)
                    """)
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE system_codes CREATED")

    try:
        cur.execute("""CREATE TABLE subject_tbl(
                    sub_code VARCHAR2(15),
                    sub_name VARCHAR2(50),
                    sem VARCHAR2(3),
                    PRIMARY KEY(sub_code)
                    )""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE subject_tbl CREATED")

    try:
        cur.execute("""CREATE TABLE id(
                    id_val NUMBER(5),
                    id_desc VARCHAR2(20),
                    PRIMARY KEY(id_desc)
                    )""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE id CREATED")

    try:
        cur.execute("""CREATE TABLE blooms_tbl(
                    blm_cd VARCHAR2(5),
                    blm_verb VARCHAR2(20),
                    blm_lvl VARCHAR2(3),
                    PRIMARY KEY(blm_cd)
                    )""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE blooms_tbl CREATED")

    try:
        cur.execute("""CREATE TABLE qns_tbl(
                    qn_code VARCHAR(5),
                    qn_desc VARCHAR2(200),
                    sub_code VARCHAR2(15) REFERENCES subject_tbl(sub_code),
                    mdl VARCHAR2(8),
                    mrk VARCHAR2(2),
                    blm_lvl VARCHAR2(3),
                    fac_emailid VARCHAR2(50) REFERENCES user_tbl(email_id),
                    PRIMARY KEY(qn_code)
                    )""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("TABLE qns_tbl CREATED")

    try:
        cur.execute("""Insert into ID (ID_VAL,ID_DESC) values (1,'blm_code')""")
        cur.execute("""Insert into ID (ID_VAL,ID_DESC) values (1,'qn_code')""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("Initial Data Added to TABLE id")

    try:
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (301,1,202,'Module 1','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (302,1,201,'S1','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (303,2,201,'S2','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (304,3,201,'S3','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (305,4,201,'S4','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (306,5,201,'S5','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (307,6,201,'S6','Semester')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (308,2,202,'Module 2','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (309,3,202,'Module 3','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (310,4,202,'Module 4','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (311,5,202,'Module 5','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (312,6,202,'Module 6','Module')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (313,1,203,'K1','Blooms Level')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (314,2,203,'K2','Blooms Level')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (315,3,203,'K3','Blooms Level')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (316,1,204,'3','Mark Type')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (317,2,204,'6','Mark Type')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (318,4,203,'K4','Blooms Level')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (319,5,203,'K5','Blooms Level')""")
        cur.execute("""Insert into SYSTEM_CODES (CODE_ID,CODE_VAL,CODE_TYPE,CD_VAL_DESC,CD_TYP_DESC) values (320,6,203,'K6','Blooms Level')""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("Initial Data Added to TABLE system_codes")

    try:
        cur.execute("""Insert into USER_TBL (FIRST_NAME,MIDDLE_NAME,LAST_NAME,EMAIL_ID,PSWD,ADM_FLG) values ('Admin','Admin','Admin','admin@admin.com','admin',1)""")
    except cx_Oracle.DatabaseError:
        checker=0
    else:
        print("Initial Data Added to user_tbl")

    con.commit()
    con.close()


    if checker == 1:
        print("Initial Data Base Set Up Is Ready")
    else:
        print("Error Occured Please Check Data Base In Detail")


setUpApplication()