import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = #Sender name
email['to'] = #Destination email
email['subject'] = #Mail subject

email.set_content(html.substitute(name='TestUser'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp_host:
    smtp_host.ehlo()
    smtp_host.starttls()
    smtp_host.login(#youremailaccount, #yourpassword)
    smtp_host.send_message(email)
    print(f'Mail sent to {email["to"]}')