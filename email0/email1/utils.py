from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_email_to_client():
    subject = "Send this Email Using Django"
    message = "Hello its my Fourth email using python and django"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["shaikhsufi8691@gmail.com"]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

def email_attechement(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    try:
        mail.send()
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")