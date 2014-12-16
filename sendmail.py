
import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText


def send_mail(receivers, timeout=5):
    rec = receivers
    sender = 'God'
    smtp = smtplib.SMTP(timeout=timeout)
    smtp.connect('smtp.domain.com')
    smtp.login('username', 'password')

    message = MIMEText(rec['body'], 'text', 'utf-8')
    message.add_header('Subject', rec['subject'])
    message.add_header('From', sender)
    message.add_header('To', rec['email'])
    message.add_header('Date', formatdate(localtime=True))
    smtp.sendmail(sender, rec['email'], message.as_string())
    smtp.quit()

if __name__ == '__main__':

    subject = "God send you an email"
    body = "Do you know me ?"
    for user in open("email"):
        receivers = {'email': user,'subject': subject,'body': body}
        send_mail(receivers)
        print 'Send to %s successful' % user
    
