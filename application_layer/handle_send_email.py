import smtplib
from application_layer.setting import username,password
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


class Handle_Send_Email(object):
    def __init__(self):
        #连接SMTP服务器
        self.client = smtplib.SMTP("smtp.sina.com")
        #开启SSL
        self.client.starttls()
        #登录邮箱
        self.client.login(user=username,password=password)

    #发送邮件
    def send_email(self,address):
        #创建邮件对象
        msg = MIMEMultipart()
        #邮件的主题
        msg['Subject'] = Header("测试邮件",'utf-8')
        #定义发送者
        msg['From'] = Header(username)
        #定义邮件的内容
        content = MIMEText("Hello World",'plain','utf-8')
        msg.attach(content)
        #发送邮件
        self.client.sendmail(username,address,msg.as_string())
        #关闭邮件连接
        self.client.close()

client = Handle_Send_Email()
client.send_email("dazhuang_python@sina.com")
