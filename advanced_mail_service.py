import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Bidontavu'
email['to'] = 'bidontavu@gmail.com'
email['subject'] = 'Dummy subject'

email.set_content(html.substitute(name='TestUser'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp_host:
    smtp_host.ehlo()
    smtp_host.starttls()
    smtp_host.login('bidontavu@gmail.com', 'Champignon:visceral!Wahl')
    smtp_host.send_message(email)
    print(f'Mail sent to {email["to"]}')