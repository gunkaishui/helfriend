from django import forms

from friend.models import *

class LoginForm(forms.Form):
     uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',   'id':'uid','placeholder':'Username'}))
     pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',   'id':'pwd','placeholder':'Password'}))

class RegisterForm(forms.Form):
       username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
   'id':'uid','placeholder':'Username'}))
       password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',   'id':'pwd','placeholder':'Password'}))
       password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',   'id':'pwd','placeholder':'Password'}))

class UploadForm(forms.ModelForm):
      class Meta:
            model = Upload
            fields = ['image']
