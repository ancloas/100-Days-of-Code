import smtplib
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()
Gmail_APP_Password=os.getenv('Gmail_APP_Password')
my_email=os.getenv('my_email')
recipient_email=os.getenv('recipient_email')

def send_mail(subject, msg_content, sender=my_email, password= Gmail_APP_Password, receiver=recipient_email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #start tls
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=receiver, 
                            msg=f"Subject: {subject}\n\n{msg_content}"
                            )



        


# send_mail('hello', 'Yo Its winter and a new year so how is it going?', receiver='anugrahgupta.52@gmail.com')