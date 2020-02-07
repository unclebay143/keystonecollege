from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Username',
                                 }))
    password = forms.CharField(max_length=100,
                                 widget=forms.PasswordInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Password',
                                 }))
    email = forms.CharField(max_length=100,
                                 widget=forms.EmailInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Valid E-mail Address',
                                 }))
    phone = forms.CharField(max_length=100,
                                 widget=forms.NumberInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Mobile Number',
                                 }))
    

    #Login Class

    class LoginData(forms.Form):
        loginusername = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Username',
                                 }))
        loginpassword = forms.CharField(max_length=100,
                                 widget=forms.PasswordInput(attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter Your Password',
                                 }))
