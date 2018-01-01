from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from bbs.models import UserProfile
from haystack.forms import SearchForm
from django.utils.translation import gettext_lazy as _

class personalProfileSettingForm(forms.Form):
    name = forms.CharField(help_text = "enter a name")

    def clean_name_data(self):
        data = self.cleaned_data['name']
        #do validation
        
        #
        return data

class detailSettingModelForm(ModelForm):
    username = forms.CharField(max_length=50, label='昵称')
    email = forms.EmailField(max_length=100, label='邮箱')
    class Meta:
        model = UserProfile
        fields = ['username','signature','email', 'headImage', 'phoneNum','receive_dynamic','receive_email']
        labels = {
            'headImage': _('头像'),
            'phoneNum': _('手机号码'),
            'signature': _('签名'),
            'receive_dynamic': _('接收谁的动态'),
            'receive_email': _('提醒邮件通知'),
        }
        required = {
            'headImage': False,
        }
        #help_text = {}
        #error_messages = {}

class basicSettingModelForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender','resume','website']
        labels = {
            'gender': _('性别'),
            'resume': _('个人简介'),
            'website': _('个人网站'),
        }
        widgets = {
            'resume':forms.Textarea,
        }


class MySearchForm(SearchForm):
    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(MySearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()
        return sqs
