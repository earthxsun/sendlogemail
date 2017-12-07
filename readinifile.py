import configparser
import os
import sys


def readconf():
    conf = configparser.ConfigParser()
    filepath = os.path.dirname(os.path.realpath(sys.argv[0])) + '\\' + 'config.ini'

    try:
        conf.read(filepath, encoding='GB2312')
        smtpserver = conf.get('config', 'smtp_server')
        sender = conf.get('config', 'sender')
        password = conf.get('config', 'password')
        recipients = conf.get('config', 'recipients')
        subject = conf.get('config', 'Subject')
        mailcontent = conf.get('config', 'mailcontent')
    except configparser.NoSectionError:
        print("没有找到配置文件：config.ini或者配置文件里没有config选项")
    else:
        confdict = {'smtpsrv': smtpserver, 'sender':sender, 'pwd': password, 'recipients': recipients, 'subject': subject,
                    'mailcontent':mailcontent}
        return confdict

