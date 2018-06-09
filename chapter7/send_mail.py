'''
发送邮件至对应的邮箱

'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send_mail(text):

    from_addr = 'psxjoy@163.com'
    password = 'SUPERPSX1995'
    to_addr = '215403065@qq.com'
    smtp_server ='smtp.163.com'

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = _format_addr('网易大新闻 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('网易新闻提醒', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()