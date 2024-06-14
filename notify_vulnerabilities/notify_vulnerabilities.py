import os
import json
import smtplib
from email.mime.text import MIMEText

RESULTS_DIR   = 'results'
EMAIL_FROM    = os.getenv('EMAIL_FROM')
EMAIL_TO      = os.getenv('EMAIL_TO')
SMTP_SERVER   = os.getenv('SMTP_SERVER')
SMTP_USER     = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
SMTP_PORT     = os.getenv('SMTP_PORT')  


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Start TLS encryption
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

def parse_results():
    for filename in os.listdir(RESULTS_DIR):
        print(filename)
        if filename.endswith('.json'):
            with open(os.path.join(RESULTS_DIR, filename), 'r') as f:
                results = json.load(f)
                vulnerabilities = results.get('scanFindings', [])
                if vulnerabilities:
                    print(f"Vulnerabilities found on {filename}:")
                    body = f"Vulnerabilities found on {filename}:\n"
                    for vuln in vulnerabilities:
                        body += f"- {vuln['vulnerability']['title']}: {vuln['vulnerability']['description']}\n"
                    send_email(f"Vulnerabilities on {filename}", body)
                else:
                    print(f"No vulnerabilities found on {filename}")

if __name__ == "__main__":
    parse_results()
