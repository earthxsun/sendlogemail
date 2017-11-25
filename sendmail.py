from email.message import EmailMessage
from email.header import Header
from readinifile import readconf
import smtplib
import codecs

mailparam = readconf()

with codecs.open('aaa.txt', encoding='GB2312') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

from_addr = mailparam['sender']
password = mailparam['pwd']
to_addr = mailparam['recipients']
smtp_server = mailparam['smtpsrv']

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header(mailparam['subject'], 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, mailparam['port'])
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

