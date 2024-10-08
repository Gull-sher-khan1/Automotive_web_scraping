"""Utility for mailers on exception"""
# pylint: disable=dangerous-default-value
import smtplib
from email.mime.text import MIMEText
from jinja2 import Environment, PackageLoader, select_autoescape
from .data_utils import DataFormater

class MailerUtils:
    """Class that handles sending mails"""
    context = {}
    file = "exception"

    def __init__(self, context = {}):
        self.assign_data(context)
        self.cred = DataFormater("mail").get_data()
        self.env = Environment(
            loader=PackageLoader("Automotive_web_scraping"),
            autoescape=select_autoescape()
        )

    def assign_data(self, context):
        """method that assigns the body"""
        for key in context:
            self.context.setdefault(key, []).append(context[key])

    def send_email(self, context = {}, file = None):
        """Mehtod that sends email to all recipients"""
        self.assign_data(context)
        template = self.env.get_template(f"{file or self.file}.html.jinja")
        msg = MIMEText(template.render(context = self.context), 'html')
        msg['Subject'] = "Exeption Occured"
        msg['From'] = self.cred['sender']
        msg['To'] = ', '.join(self.cred['recipients'])
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.cred['sender'], self.cred['password'])
            smtp_server.sendmail(self.cred['sender'], self.cred['recipients'], msg.as_string())
