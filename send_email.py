from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.utils import formataddr
from_addr = "841380419@qq.com"
password = "gussybjjhejwbfej"
smtp_server = "smtp.qq.com"
msg = MIMEMultipart()
msg["Subject"] = "测试"
msg['From'] = formataddr(["myself",from_addr])
msg["To"] = formataddr(["me",from_addr])
print(msg["To"])
msg["To"] = formataddr(["me2","wdpanjing@163.com"])
print(msg["To"])
msg.attach(MIMEText("see attachment"))
att = MIMEText(open("test.py","rb").read(),'plain','utf-8')
att.add_header("Content-Disposition","attac",filename="OK.py")
#msg.attach(att)
att2 = MIMEText(open("vcode.png","rb").read(),'plain','utf-8')
att2.add_header("Content-Disposition","att",filename="2.png")
#msg.attach(att2)
sever = smtplib.SMTP(smtp_server)
sever.set_debuglevel(0)
sever.ehlo(smtp_server)
sever.login(from_addr,password)
sever.sendmail(from_addr,from_addr,msg.as_string())
sever.quit()