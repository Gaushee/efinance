from wechat_work import WechatWork

corpid = 'wwd9b77516c3c5063e'
appid = '1000003'
corpsecret = 'EE6KhSKrId17rb4Vajzae-dbveJ14iqvD5v3utWy9QA'
users = ['GaoXi']
w = WechatWork(corpid=corpid, appid=appid, corpsecret=corpsecret)
# 发送文本
#w.send_text('Hello World!', users)
# 发送 Markdown
#w.send_markdown('# Hello World', users)
# 发送图片
#w.send_image('./hello.jpg', users)
# 发送文件
#w.send_file('./hello.txt', users)


def send_text(msg):
    w.send_text(msg, users)
