# this file is for sending account related emails
import os
import requests
from core.helpers.send_email import send_email

# from core.settings import EMAIL_API_KEY
from core.emails.email_templates.welcome_email import welcome_email_content


# Email api endpoint
endpoint = "https://api.elasticemail.com/v2/email/send"


def account_created_email(strong_password):
    print("Generated strong password:", strong_password)


# common data
# common_data = {
#     "apikey": "E3DF424D2FCE8D3F0251F31E9BCB6CE8C37B9E5FB5A90C52C287F4AA31883B36D1813EE57C76BD2A7154BF3082C2E19C",
#     "mergeSource": "api",
# }

# base link
BASE_LINK = "http://127.0.0.1:8000"


# Welcome email
# def send_general_email(
#     receiver_email,
#     template_id,
#     merge_fields,
# ):
#     data = {
#         **common_data,
#         "from": "i.busah@alustudent.com",
#         "to": receiver_email,
#         "template": template_id,
#     }

#     for field_name, field_value in merge_fields.items():
#         data[field_name] = field_value
#     # print(EMAIL_API_KEY)
#     response = requests.post(endpoint, data=data)
#     print(f"Email is sent to: {receiver_email}")
#     print(response.text)


def send_welcome_email(recipient_email, first_name, password, login_link):
    subject = "Welcome to MarketPulse Platform"
    html_body = welcome_email_content.format(
        first_name=first_name,
        email=recipient_email,
        password=password,
        login_link=login_link,
    )
    send_email(recipient_email, subject, html_body)


# Verification email
# def send_verify_email(recipient_email, first_name, verification_code):
#     subject = "Verify your login"
#     html_body = login_verification_email_content.format(
#         first_name=first_name,
#         verification_code=verification_code,
#         login_link=f"{BASE_LINK}/login_link",
#     )
#     data = {
#         "first_name_Value": first_name,
#         "verification_code_Value": verification_code,
#         "login_link": f"{BASE_LINK}/login",
#     }

#     send_email(recipient_email, data, html_body, subject)


# def send_email_verify_success_email(recipient_email, first_name):
#     subject = "Login Successful"
#     html_body = login_successful_content.format(
#         first_name=first_name,
#     )
#     data = {
#         "first_name_Value": first_name,
#     }

#     send_email(recipient_email, data, html_body, subject)


# def send_forgot_password_email(recipient_email, first_name, CODE):
#     subject = "Your Password Reset Code"
#     html_body = password_reset_content.format(first_name=first_name, CODE=CODE)
#     data = {"first_name_Value": first_name, "code_Value": CODE}

#     send_email(recipient_email, data, html_body, subject)


# # Password Reset success
# # def send_password_rest_success_email(
# #     receiver_email,
# #     receiver_name,
# # ):

# #     template_id = "resetSuccess"
# #     merge_fields = {
# #         "merge_NAME":receiver_name,
# #         "merge_EMAIL": receiver_email,
# #     }
# #     send_general_email(
# #         receiver_email,
# #         template_id,
# #         merge_fields,
# #     )


# def send_password_rest_success_email(recipient_email, first_name):
#     subject = "Password Reset Successful"
#     html_body = reset_success_content.format(
#         first_name=first_name,
#     )
#     data = {
#         "first_name_Value": first_name,
#     }

#     send_email(recipient_email, data, html_body, subject)
