from django import forms

class LoginForm(forms.Form):
     uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',   'id':'uid','placeholder':'Username'}))
     pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',   'id':'pwd','placeholder':'Password'}))

class RegisterForm(forms.Form):
     username = forms.CharField(label='username',max_length=256,                           widget=forms.TextInput(attrs={'id':'username'}))
     password1 = forms.CharField(widget=forms.PasswordInput)
     password2 = forms.CharField(widget=forms.PasswordInput)
