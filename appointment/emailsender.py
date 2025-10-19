import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

your_email = os.getenv("screenbondhq")
app_password = os.getenv("screenbondhq_app_password")

subject = "Thank you for Placing a Fake order lol"

email_template = """
Dear {name},

Hi! This is Nellu here! Thanks for placing your order with us, you will get your order soon!

Best regards,
Screenbond Team
"""

def send_email(your_email, app_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(your_email, app_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {str(e)}")

def sendemail(name, recipient_email):
    body = email_template.format(name=name)
    send_email(your_email, app_password, recipient_email, subject, body)

sendemail(name="Ray", recipient_email="werayco@gmail.com")
