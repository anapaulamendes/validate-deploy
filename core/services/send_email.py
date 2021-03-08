from django.conf import settings
from sendgrid import Mail, SendGridAPIClient


class SendEmail:
    def __init__(self, to_emails, subject, message):
        self.from_email = "anapaula.ds.mendes@gmail.com"
        self.to_emails = to_emails
        self.subject = subject
        self.message = message

    def send_email(self):
        message = Mail(
            from_email=self.from_email,
            to_emails=self.to_emails,
            subject=self.subject,
            html_content=self.message,
        )
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            return sg.send(message)
        except Exception as error:
            raise error
