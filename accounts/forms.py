from django import forms

class UserLoginForm(forms.Form):
    """
    Form to be used by visitors to log in
    """
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)