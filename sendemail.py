#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = '2070047236@qq.com'
my_pass='mwzcpfwrixjecfbj'
receivers = '2534324260@qq.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("Github Actions", 'utf-8')
message['To'] = Header("You", 'utf-8')
subject = '文件下载完毕'
message['Subject'] = Header(subject, 'utf-8')


# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('log.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="log.txt"'
message.attach(att1)

server=smtplib.SMTP_SSL("smtp.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
server.login(sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(sender,[receivers,],message.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit() # 关闭连接

print("邮件发送完毕！")
