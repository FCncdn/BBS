from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django import forms
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})



class LoginForm(forms.Form):
   username = forms.CharField(required=True, min_length=5)
   password = forms.CharField(required=True, min_length=8)
   captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码form
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

class ResetForm(forms.Form):
    pwd1 = forms.CharField(required=True, min_length=8)
    pwd2 = forms.CharField(required=True, min_length=8)
