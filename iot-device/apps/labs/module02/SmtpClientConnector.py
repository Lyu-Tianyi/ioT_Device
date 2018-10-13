'''
Created on Sep 22, 2018

@author: l0t0y
'''

from labs.common.ConfigUtil import ConfigUtil
from labs.common.ConfigConst import ConfigConst
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

class SmtpClientConnector():
    def __init__(self):
        self.config = ConfigUtil('D:/git/repository/iot-device/data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
    def publishMessage(self, topic, data):
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
    def sendEmailMessage(self,topic,message):
        for destinAddr in self.destinAddr:
            
            msg=MIMEText(str(message))
            msg["From"]=self.sourceAddr
            msg["to"]=destinAddr
            msg["Subject"]=topic
        
            try:
                mailServer=smtplib.SMTP_SSL(self.host,self.port)
                mailServer.ehlo()
                mailServer.login(self.sourceAddr,self.passphrase)
                mailServer.send_message(msg,self.sourceAddr,destinAddr)
                mailServer.close()
                print("Sent successfully to "+destinAddr)
            except Exception as e:
                print("Failed to send email\n"+e)
    
    def printInfo(self):
        print("host:"+self.host+"\nport:"+str(self.port)+"\nFromAddr:"+self.sourceAddr+"\ntoAddr:"+self.destinAddr+"\n"+
              "authToken:"+self.passphrase)