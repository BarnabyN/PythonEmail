import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail_from_barney(mail_to):
    
    sender = "barnabynapier@gmail.com"
    recipient = mail_to
    password = "Nassaustraat3596" # Your SMTP password for Gmail
    subject = "Email from Python"
    body = "The Python is a snake, and it has slithered into your inbox"
    
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "Sent From Python"
    msg.attach(MIMEText(body, "Plain"))
    
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    
    text = msg.as_string()
    smtp_server.sendmail(sender, recipient, text)
    
    smtp_server.quit()

mail_from_barney("bn309@bath.ac.uk")