import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import userdetails


def emailSndngInterface(email_attach):
    """Function that sends the generated question paper to the corresponding mail id"""

    email_user = 'arunjose173@gmail.com'
    email_password = 'CAPTIVAALTO'
    #email_send = 'arunjoseajk@gmail.com'
    email_send = userdetails.emailid

    subject = 'AQPG-Generated Question Paper'

    try:

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        if userdetails.mname == None:
            name=str(userdetails.fname)+" "+str(userdetails.lname)
        else:
            name=str(userdetails.fname)+" "+str(userdetails.mname)+" "+str(userdetails.lname)

        #name=userdetails.fname+" "+userdetails.mname+" "+userdetails.lname

        body = "Hi "+name+",\nPFA question paper generated\n\nThanks & Regards\nTeam AQPG\n*** RAV Technologies ***"
        msg.attach(MIMEText(body,'plain'))

        filename=email_attach
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
    except Exception:
        print("No internet Connection")

def welcomeEmailSndr(email,fname,mname,lname,pswd):
    email_user = 'arunjose173@gmail.com'
    email_password = 'CAPTIVAALTO'
    email_send = email

    subject = 'Welcome to AQPG System'

    try:

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        name=fname+" "+mname+" "+lname

        body = """Hi """+name+""",\nWelcome To AQPG\n\nThe complete system for Automated Question Paper generation\n\n\nUsername : """+email+"""\nPassword : """+pswd+"""\n\n\nThanks & Regards\nTeam AQPG\n*** RAV Technologies ***"""
        msg.attach(MIMEText(body,'plain'))

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
    except Exception as e :
        print("No internet Connection")
        print(e)