import requests
from core.emails.email_templates.welcome_email import welcome_email_content
from core.emails.email_templates.notification import (
    low_stock_email_content,
    nearing_expiry_email_content,
    expired_product_email_content,
)
from core.settings import EMAIL_SERVER_TOKEN

# Replace with your information
server_token = EMAIL_SERVER_TOKEN


url = "https://api.postmarkapp.com/email"
headers = {"X-Postmark-Server-Token": server_token, "Content-Type": "application/json"}


def send_email(recipient_email, subject, html_body):
    body = {
        "From": "i.busah@alustudent.com",
        "To": recipient_email,
        "Subject": subject,
        "HtmlBody": html_body,
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Error sending email: {response.status_code}")
        print(response.text)


def send_low_inventory_email(recipient_email, recipient_name, low_stock_products):
    product_list_html = "".join(
        f'<li>{product["name"]} - {product["stock_quantity"]} left</li>'
        for product in low_stock_products
    )

    formatted_email_content = low_stock_email_content.format(
        first_name=recipient_name, product_list=product_list_html
    )

    subject = "Low Inventory Alert - MarketPulse Platform"

    send_email(recipient_email, subject, formatted_email_content)


def send_nearing_expiry_email(recipient_email, recipient_name, nearing_expiry_products):
    products_html = "".join(
        f"<li><strong>{product['name']}:</strong> Expiry Date - {product['expiry_date']}</li>"
        for product in nearing_expiry_products
    )

    formatted_email_content = nearing_expiry_email_content.format(
        first_name=recipient_name,
        product_list=products_html,
    )

    subject = "Nearing Expiry Notification - MarketPulse Platform"

    send_email(recipient_email, subject, formatted_email_content)


def send_expired_product_email(recipient_email, recipient_name, expired_products):
    product_list_html = "".join(
        f'<li>{product["name"]} - Expired on {product["expiry_date"]}</li>'
        for product in expired_products
    )

    formatted_email_content = expired_product_email_content.format(
        first_name=recipient_name, product_list=product_list_html
    )

    subject = "Expired Product Notification - MarketPulse Platform"

    send_email(recipient_email, subject, formatted_email_content)
