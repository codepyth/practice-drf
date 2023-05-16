# attachment_path = 'textfile.txt'
#
#
# def get_file_size(attachment_path):
#     with open(attachment_path, "rb") as file:
#         file.seek(0, 2)  # move to the end of the file
#         file_size = file.tell()  # get the current position, which is the file size
#         print(file_size, 'size')
#     return file_size
#
#
# attachment_size = get_file_size(attachment_path)
# if attachment_size > 0:
#     # send email with attachment
#     email_send = EmailOperator(
#         dep_list=[write_noob_file],
#         attachments=attachment_path,
#         manifold_bucket="new_hire_report",
#         manifold_sub_dir="tree/New_hire_optimization",
#         is_html=True,
#         maximum_file_size=40280000,
#         sender="Tom smith <Tomsmith@gmail.com>",
#         recipients=["najah.hajar93@gmail.com"],
#         subject="Noob Report - <DATETIME:%m/%d/%Y>",
#         body="""<!DOCTYPE HTML5>
#        <html>
#        <head>
#            <style>
#                table {
#                    border-collapse: collapse;
#                }
#            </style>
#        </head>
#        <body>
#            <h1>Hello World...this is a test!</h1>
#            <p>
#                <i>[This is an automated email to inform you of the New Hires for your team. Please reach out if you have any questions.]</i><br><br>
#                Hello,<br><br>
#                Please find the attached file for the latest New Hire report for your team.<br>
#                blablabla<br><br>
#                Could you kindly let me know that this pipeline works by replying it. Thank you!<br><br>
#                Please reach out if you have any questions.<br><br>
#                Best,<br>
#              Hajar
#            </p>
#        </body>
#        </html>""",
#     )
# else:
#     # send email without attachment
#     email_send = EmailOperator(
#         dep_list=[write_noob_file],
#         manifold_bucket="new_hire_report",
#         manifold_sub_dir="tree/New_hire_optimization",
#         is_html=True,
#         sender="Tom smith <Tomsmith@gmail.com>",
#         recipients=["najah.hajar93@gmail.com"],
#         subject="No new hire - <DATETIME:%m/%d/%Y>",
#         body="""<!DOCTYPE HTML5>
#        <html>
#        <head>
#            <style>
#                table {
#                    border-collapse: collapse;
#                }
#            </style>
#        </head>
#        <body>
#            <h1>Hello World...this is a test!</h1>
#            <p>
#                <i>[This is an automated email to inform you that there are no new hires for your team.]</i><br><br>
#                Hello,<br><br>
#                There are no new hires to report for your team.<br>
#                blablabla<br><br>
#                Could you kindly let me know that this pipeline works by replying it. Thank you!<br><br>
#                Please reach out if you have any questions.<br><br>
#                Best,<br>
#                Rachel
#            </p>
#        </body>
#        </html>
#    """,
#     )

import smtplib

attachment_path = 'textfile.txt'

# Check if the file has content
with open(attachment_path) as f:
    if not f.read().strip():
        print("File is empty, skipping email send.")
        exit()

# Open the file and read the content
with open(attachment_path) as f:
    attachment_content = f.read()

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "waseempy@gmail.com"
receiver_email = "wasimbaloch9@gmail.com"
password = "bsuztqrvzfsbwxbw"
subject = "Test Email"
body = "This is a test email sent using Python."

message = f"""\
From: {sender_email}
To: {receiver_email}
Subject: {subject}
Content-Type: text/plain
Content-Disposition: attachment; filename={attachment_path}

{attachment_content}
"""


# Connect to the SMTP server and login
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)


# Send the email
server.sendmail(sender_email, receiver_email, message)

# Disconnect from the SMTP server
server.quit()

print("Email sent!")