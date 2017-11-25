from email.message import EmailMessage
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import codecs


# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
with codecs.open('aaa.txt', encoding='GB2312') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

from_addr = 'itlog@szjuhang.cn'
password = 'JH@123.log'
to_addr = 'erp@szjuhang.cn,2631189308@qq.com'
smtp_server = 'smtp.exmail.qq.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header(u'数据库备份日志', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 465)
server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

