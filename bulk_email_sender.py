# Imports
# email imports
# ==> For sending emails via SMTP
import smtplib 
# creating plain text emails
from email.mime.text import MIMEText 
# to allow combining text, html, and attatchments in one email we use MIMEMultipart
from email.mime.multipart import MIMEMultipart
import time # for delays

# =====================================================
# Smtp Configuration
# =====================================================
SMTP_SERVER = "smtp.gmail.com" # Put your smtp details
SMTP_PORT = 587
FROM_EMAIL = "email"
USERNAME = "user"
PASSWORD = "pass"
# OR YOU CAN CREATE AN .ENV FILE FOR THAT

# =============================================================
# RECIPIENT LIST
# =============================================================
recipients = [
    "user@gmail.com",
    "user2@gmail.com",
    "user3@outlook.com"
    # upto 100 emails
]


# =====================================
# create message
try:
    # Connect to Gmail SMTP and TLS ehlo
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME, PASSWORD)

        # Send emails one by one == for loop innit!
        for recipient in recipients:
            msg = MIMEMultipart()
            msg["From"] = FROM_EMAIL
            msg["To"] = recipient
            msg["Subject"] = "Hello from Joy Njoroge!"

            # Personalized body, can be anyything
            body = f"Hello {recipient.split('@')[0]},\n\nThis is a test email sent from a Python script using Gmail SMTP."
            msg.attach(MIMEText(body, "plain"))

            # Send the email to teh recipients
            server.sendmail(FROM_EMAIL, recipient, msg.as_string())
            print(f"Sent to {recipient}")
            
            time.sleep(2)  # Delay to avoid Gmail limits=== can be flagged as spam!

    print("All emails sent successfully!")

except Exception as e:
    print(f"Error: {e}")
# done!!