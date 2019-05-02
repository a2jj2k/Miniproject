CREATE TABLE user_tbl(
first_name VARCHAR2(40) NOT NULL,
middle_name VARCHAR2(40),
last_name VARCHAR2(40),
email_id VARCHAR2(50),
pswd VARCHAR2(50),
adm_flg NUMBER(1),
PRIMARY KEY (email_id)
);

CREATE TABLE system_codes(
code_id NUMBER(3),
code_val NUMBER(2),
code_type NUMBER(4),
cd_val_desc VARCHAR2(20),
cd_typ_desc VARCHAR2(20),
PRIMARY KEY (code_id));

CREATE TABLE subject_tbl(
sub_code VARCHAR2(15),
sub_name VARCHAR2(50),
sem VARCHAR2(3),
primary key(sub_code));

CREATE TABLE id(
id_val NUMBER(5),
id_desc VARCHAR2(20),
primary key(id_desc));

insert into id(id_val,id_desc)
values(1,'qn_code');

select id_val from id where id_desc='qn_code';

select * from user_tbl; order by qn_code;

select * from user_tbl where email_id='arunjoseajk@gmail.com'

delete from user_tbl where email_id='a@gmail.com'

select qt.,qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
from qns_tbl qt
left outer join subject_tbl st on qt.sub_code = st.sub_code
left outer join user_tbl ut on ut.email_id = qt.fac_emailid
order by st.sem,st.sub_name,qt.mdl,qt.mrk

select * from user_tbl;

select sub_code from subject_tbl where sub_name='Android';

Select id_val from id where id_desc='qn_code';


CREATE TABLE blooms_tbl(
blm_cd VARCHAR2(5),
blm_verb VARCHAR2(20),
blm_lvl VARCHAR2(3),
primary key(blm_cd));

alter table qns_tbl
modify  qn_desc VARCHAR2(500);


CREATE TABLE qns_tbl(
qn_code VARCHAR(5),
qn_desc VARCHAR2(200),
sub_code VARCHAR2(15) REFERENCES subject_tbl(sub_code),
mdl VARCHAR2(8),
mrk VARCHAR2(2),
blm_lvl VARCHAR2(3),
fac_emailid VARCHAR2(50) REFERENCES user_tbl(email_id),
primary key(qn_code));

select * from system_codes;
select * from qns_tbl;

delete from QNS_TBL where qn_code='qn1'

select * from blooms_tbl;
update id set id_val=1 where id_desc='qn_code'

update id set id_val=1 where id_desc='qn_code';

update id set id_val=(select (id_val+1) from id where id_desc='qn_code') where id_desc='qn_code';

select * from blooms_tbl where subname=


insert into BLOOMS_TBL(blm_cd,blm_verb,blm_lvl)
values('blm5','Determine','K5')

INSERT INTO SUBJECT_TBL(sub_code,sub_name,sem)
VALUES('RLMCA007','Android','S3')

select * from blooms_tbl where sub_code = 'arun'

select * from subject_tbl;
update subject_tbl set sem='S1' where sem='s1'

select sub_name from subject_tbl where sem='S1' order by sub_code

drop table system_codes;

select cd_val_desc from system_codes where code_type=203 order by cd_val_desc asc;

insert into system_codes(code_id,code_val,code_type,cd_val_desc,cd_typ_desc)
values((select max(code_id)+1 from system_codes),2,204,'6','Mark Type');

select cd_val_desc from system_codes where code_type=201;

delete from SYSTEM_CODES where code_id=301;

update SYSTEM_CODES set cd_val_desc = 'Module 5' where code_id=311

INSERT INTO system_codes(code_id,code_val,code_type,cd_val_desc,cd_typ_desc)
VALUES(312,6,202,'Module 6','Module')

INSERT INTO user_tbl (first_name,middle_name,last_name,email_id,pswd) 
VALUES ('Arun','','Jose','arunjoseajk@gmail.com','7559955251');

INSERT INTO user_tbl (first_name,middle_name,last_name,email_id,pswd) 
VALUES ('Rakesh','R','Nair','rakeshrn1995@gmail.com','7559955251');

INSERT INTO user_tbl (first_name,middle_name,last_name,email_id,pswd) 
VALUES ('Visakh','','Harikumar','visakhharikumar870@gmail.com','7559955251');


select * from qns_tbl where qn_code in ('qn10','qn24');

select * from user_tbl;

delete from qns_tbl where qn_code='blm36';

select count(qn_code) from qns_tbl;

select * from subject_tbl;

delete from subject_tbl;

select qn_desc from qns_tbl where qn_code in ('qn2','qn13','qn23','qn21','qn27')

update id set id_val=1 where id_desc='qn_code'

select * from id

update id set id_val=1 where id_desc='qn_code'

select * from subject_tbl where sem='S1'

update subject_tbl set sub_name='Application Development and management Python Prog' where sub_code='RLMCA20985'

select qn_code from qns_tbl where sub_code=(select sub_code from subject_tbl where sub_name='Android') and mdl='Module 3' and mrk='3'

delete from id where qn_code in ('1','2')

select * from id where code_type=203;

insert into system_codes(code_id,code_val,code_type,cd_val_desc,cd_typ_desc)
values((select max(code_id)+1 from system_codes),6,203,'K6','Blooms Level')

select first_name||' '||middle_name||' '||last_name,
email_id,
case adm_flg when 1 Then 'Yes'
else 'No' end
from user_tbl;

select * from user_tbl where EMAIL_ID='a2jj2k@gmail.com'

update user_tbl set pswd='7559955251' where email_id='arunjoseajk@gmail.com'

select * from system_codes order by code_id



select qt.qn_desc,st.sem,st.sub_name,qt.mdl,qt.mrk,qt.blm_lvl,ut.first_name||' '||ut.middle_name||' '||ut.last_name as name,ut.email_id
                        from qns_tbl qt
                        left outer join subject_tbl st on qt.sub_code = st.sub_code
                        left outer join user_tbl ut on ut.email_id = qt.fac_emailid
                        where st.SEM='S3' and st.sub_name='All' and qt.mdl='Module 2' and qt.mrk='3'
                        order by st.sem,st.sub_name,qt.mdl,qt.mrk


select * from id;

select count(blm_cd) from blooms_tbl order by blm_lvl;

delete from blooms_tbl;
update id set id_val=1 where id_desc='blm_code'