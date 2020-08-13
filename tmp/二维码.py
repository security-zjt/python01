# from MyQR import myqr    # 注意大小写
# myqr.run(words='https://www.cnblogs.com/security-guard/')
# # 如果为网站则会自动跳转，文本直接显示，不支持中文
#

from MyQR import myqr

myqr.run(
    words='https://www.cnblogs.com/security-guard/',  # 包含信息
    picture='pika.gif',  # 背景图片
    colorized=True  # 是否有颜色，如果为False则为黑白
)
