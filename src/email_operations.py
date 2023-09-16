import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, key):
    sender_email = 'Email Address'
    sender_password = 'Password'
    subject = 'Your key'
    message = 'Thanks for using CipherVault! your key is: ' + key
    # Set up the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the email server and send the email
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)  # Change SMTP server and port if using a different provider
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return ("Email sent successfully!")
    except Exception as e:
        return ("An error occurred while sending the email:", str(e))


def is_valid_email(email):
    if '@' not in email:
        return False
    return True
