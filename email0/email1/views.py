# from django.shortcuts import render, redirect
# from .utils import send_email_to_client, email_attechement
# from django.conf import settings
#
# def send_email(request):
#     # Your existing code here
#     subject ="Send this Email Attechment Using Django"
#     message ="Hello its my friest  email attechment using python and django"
#     recipient_list = ["shaikhsufi8691@gmail.com"]
#     file_path=f"{settings.BASE_DIR}/main.xlsx"
#     email_attechement(subject, message, recipient_list, file_path)
#     return redirect('/')

def email(request):
    return render(request, "home.html")


from django.shortcuts import render, redirect
from .utils import send_email_to_client, email_attechement
from django.conf import settings

def send_email(request=None):  # <-- Add a default value of None for the request
    # Your existing code here
    subject ="Send this Email Attachment Using Django"
    message ="Hello its my first email attachment using python and django"
    recipient_list = ["shaikhsufi8691@gmail.com"]
    file_path=f"{settings.BASE_DIR}/main.xlsx"
    email_attechement(subject, message, recipient_list, file_path)
    return redirect('/')
