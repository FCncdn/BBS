from random import Random
from django.core.mail import send_mail
from bbs.models import EmailVerifyRecord
from BBSPRO.settings import  EMAIL_FROM


# 生成随机字符串函数
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str



# 发送邮箱验证码
def send_email(email, send_type="forget"):
    # 创建邮箱验证码实例
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    # 将数据验证码、邮箱保存、验证类型保存
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""


    if send_type == 'forget':
        email_title = '汕大BBS密码重置链接'
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
