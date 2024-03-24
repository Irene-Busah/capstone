# Define the HTML content as a variable with placeholders
welcome_email_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Welcome to MarketPulse</title>
</head>
<body style="font-family: Arial, sans-serif;">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
    <td style="padding: 20px;">
        <p>Dear {first_name},</p>
        <p>Welcome to MarketPulse Platform! We are thrilled to have you on board.</p>
        <p>Your account has been successfully created. To get started, simply click the link below to log in and explore our data-driven dashboard:</p>
        <ul>
            <li><strong>Username:</strong> {email}</li>
            <li><strong>Password:</strong> {password}</li>
        </ul>
        <p>To access your account, please click on the following link:</p>
        <p><a href="{login_link}">Login Now</a></p>
        <p>If you have any questions or need further assistance, feel free to contact our support team.</p>
        <p>Best regards,<br/> MarketPulse Team</p>
    </td>
</tr>
</table>

</body>
</html>
"""
