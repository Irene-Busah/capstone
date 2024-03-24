# Define the HTML content as a variable with placeholders
login_successful_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Verified</title>
</head>
<body style="font-family: Arial, sans-serif;">

<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
    <td style="padding: 20px;">
        <p>Dear {first_name},</p>
        <p>Congratulations! Your login to MarketPulse was successful</p>
        <p>You now have full access to our platform.</p>
        <p>If you have any questions or need further assistance, feel free to contact our support team.</p>
        <p>Best regards,<br/> MarketPulse Team</p>
    </td>
</tr>
</table>

</body>
</html>
"""
