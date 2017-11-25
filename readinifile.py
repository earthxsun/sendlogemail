import configparser

def readconf():
    conf = configparser.ConfigParser()
    try:
        conf.read('config.ini',encoding='UTF-8')
        smtpserver = conf.get('config','smtp_server')
        sender = conf.get('config','sender')
        password = conf.get('config','password')
        recipients = conf.get('config','recipients')
        subject = conf.get('config','Subject')
        mailcontent = conf.get('config','mailcontent')
    except configparser.NoSectionError:
        print("没有找到配置文件：config.ini或者配置文件里没有config选项")
    else:
        confdict = {'smtpsrv':smtpserver,'sender':sender,'pwd':password,'recipients':recipients,'subject':subject,
                    'mailcontent':mailcontent}
        return confdict


