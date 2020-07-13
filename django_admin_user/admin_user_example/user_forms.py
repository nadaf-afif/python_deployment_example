from django import forms
from django.contrib.auth.models import User
from admin_user_example.models import UserInformation

class UserForm(forms.ModelForm):
     class Meta():
         model = User
         fields = ('username','email','password')


class UserInformationForm(forms.ModelForm):
      class Meta():
          model = UserInformation
          fields = ('gender', 'profile_pic')   