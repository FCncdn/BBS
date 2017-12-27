from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from bbs.models import UserProfile

class personalProfileSettingForm(forms.Form):
    name = forms.CharField(help_text = "enter a name")

    def clean_name_data(self):
        data = self.cleaned_data['name']
        #do validation
        
        #
        return data

class personalprofileSettingModelForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'signature', 'headImage']