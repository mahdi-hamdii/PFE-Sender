
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import os
import time
import random


SENDER = "mail@gmail.com"
EMAIL_PASS = "generatedpassword"
#"qnasnnsaqqlihxxu"
i=0
def send_mail(receiver, name):
    subject = "DevOps Engineer Intern"
    
    manager_name="Hello,"
    if name !="":
        manager_name=f"Dear %s," %(name)
    body= '''%s

My name is FULL NAME and I am a final-year Software Engineering student majoring in Software Engineering at the National Institute of Applied Sciences and Technology (INSAT).

Currently looking for an end-of-studies internship, I am taking the opportunity to contact you as I am highly interested in a graduate position within your team as a DevOps Intern.

You will find attached my resume for an overview of my profile, my cover letter and my certifications.

I thank you in advance for considering my enthusiasm to work in your company.

Looking forward to your response, I would be happy to provide you with any information and answer your questions.

Please receive the assurance of my best regards,

Sincerely,
FULL NAME.
''' %(manager_name)
    
    #Prepare the message
    message=MIMEMultipart()
    message["From"] = SENDER
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    
    #Add the attached docs (just add the name of the doc)
    filenames = ["Attached Documents List"]
    for filename in filenames:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        
        message.attach(part)
    
    
    # prepare our text to send
    text = message.as_string()
    #Send the email
    with smtplib.SMTP('smtp.gmail.com:587') as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            # access to https://myaccount.google.com/lesssecureapps and check if the 2 factor auth is enabled!
            # if it is not enabled, just cturn on the allow less secure apps and type your password
            
            # if it is enabled you need to create an application specific password:
            # to do this go to https://myaccount.google.com/u/1/apppasswords
            smtp.login(SENDER,EMAIL_PASS)
            smtp.sendmail(SENDER,receiver,text)
            smtp.quit()
            print (i,"Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong…. - ",receiver, " - ",ex)
    

with open('mails.txt') as f:
    line = f.readline()
    while line:
        i=i+1
        params = line.split()
        if (len(params)==1):
            send_mail(params[0],"")
        else:
            send_mail(params[0], params[1])
        line = f.readline()
        x = random.randint(30,190)
        time.sleep(x)
