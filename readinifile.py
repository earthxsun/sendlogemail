import configparser

def readconf():
    conf = configparser.ConfigParser()
    conf.read('config.ini',encoding='UTF-8')

    smtpserver = conf.get('config','smtp_server')
    sender = conf.get('config','sender')
    password = conf.get('config','password')
    recipients = conf.get('config','recipients')
    subject = conf.get('config','Subject')

    confdict = {'smtpsrv':smtpserver,'sender':sender,'pwd':password,'recipients':recipients,'subject':subject}
    return confdict


