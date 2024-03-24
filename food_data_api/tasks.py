from celery import shared_task


@shared_task
def send_low_inventory_emails():
    # Get all products with low stock
    low_stock_products = get_low_stock_products()

    if low_stock_products.exists():
        # Assuming you have a way to determine the recipients for the notification
        recipients = get_notification_recipients()

        for recipient in recipients:
            # Prepare the low stock product list for the email
            low_stock_products_list = low_stock_products.values(
                "name", "stock_quantity"
            )

            # Call the function to send the email
            send_low_inventory_email(
                recipient.email, recipient.first_name, list(low_stock_products_list)
            )
