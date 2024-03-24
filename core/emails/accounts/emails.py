import os
import requests
from core.helpers.send_email import send_email

from core.emails.email_templates.welcome_email import welcome_email_content
from core.emails.email_templates.login_successful import login_successful_content
from core.emails.email_templates.reset_success import reset_success_content
from core.emails.email_templates.delete_account import delete_account_content


# Email api endpoint
endpoint = "https://api.elasticemail.com/v2/email/send"


def account_created_email(strong_password):
    print("Generated strong password:", strong_password)


# base link
BASE_LINK = "http://127.0.0.1:8000"


def send_welcome_email(recipient_email, first_name, password, login_link):
    subject = "Welcome to MarketPulse Platform"
    html_body = welcome_email_content.format(
        first_name=first_name,
        email=recipient_email,
        password=password,
        login_link=login_link,
    )
    send_email(recipient_email, subject, html_body)


def send_login_successful_email(recipient_email, first_name):
    subject = "Login Successful - MarketPulse Platform"
    html_body = login_successful_content.format(first_name=first_name)

    send_email(recipient_email, subject, html_body)


def send_password_reset_successful_email(recipient_email, first_name):
    subject = "Password Reset Successful - MarketPulse Platform"
    html_body = reset_success_content.format(first_name=first_name)

    send_email(recipient_email, subject, html_body)


def send_delete_account_email(recipient_email, first_name):
    formatted_email_content = delete_account_content.format(first_name=first_name)

    subject = "Account Deletion Confirmation - MarketPulse"

    send_email(recipient_email, subject, formatted_email_content)
