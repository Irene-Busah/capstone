low_stock_email_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Low Inventory Alert - MarketPulse</title>
</head>
<body style="font-family: Arial, sans-serif;">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
    <td style="padding: 20px;">
        <p>Dear {first_name},</p>
        <p>This is an automated notification from the MarketPulse Platform to inform you that the following product(s) in your inventory are running low:</p>
        <ul>
            {product_list}
        </ul>
        <p>We recommend reviewing your current stock levels and considering a restock to avoid any disruptions in your sales. You can manage your inventory and place orders directly through your MarketPulse dashboard.</p>
        <p>If you have any questions or need further assistance, please don't hesitate to reach out to our support team.</p>
        <p>Best regards,<br/>The MarketPulse Team</p>
    </td>
</tr>
</table>

</body>
</html>
"""

nearing_expiry_email_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Nearing Expiry Notification</title>
</head>
<body style="font-family: Arial, sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
    <td style="padding: 20px;">
        <p>Dear {first_name},</p>
        <p>We wanted to remind you that the following product(s) are nearing their expiry dates:</p>
        <ul>
            {product_list}
        </ul>
        <p>Please take the necessary actions to avoid wastage.</p>
        <p>If you have any questions or need assistance, please feel free to contact us.</p>
        <p>Best regards,<br/> The MarketPulse Team</p>
    </td>
</tr>
</table>
</body>
</html>
"""


expired_product_email_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Expired Product Notification</title>
</head>
<body style="font-family: Arial, sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
    <td style="padding: 20px;">
        <p>Dear {first_name},</p>
        <p>Unfortunately, the following product(s) have expired:</p>
        <ul>
            {product_list}
        </ul>
        <p>Please ensure to remove these products from your inventory to maintain quality and safety standards.</p>
        <p>If you have any questions or require assistance, do not hesitate to reach out to us.</p>
        <p>Best regards,<br/> The MarketPulse Team</p>
    </td>
</tr>
</table>
</body>
</html>
"""
