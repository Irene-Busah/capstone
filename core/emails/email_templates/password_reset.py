# Define the HTML content as a variable with placeholders
password_reset_content = """
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
        <p>You've requested to reset your password for KPI Tool.</p>
        <p>Here's your reset code: {CODE}</p>
        <p>Please use this code to reset your password.</p>
        <p>If you didn't request this, you can safely ignore this email.</p>
        <p>Best regards,<br/> KPI Team</p>
    </td>
</tr>
</table>

</body>
</html>
"""
