from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder":'Your fullname'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder":'Your email'}
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder":'Your content'}
    ))

    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        return self.validate_fullname_field(fullname)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return self.validate_email_field(email)

    @staticmethod
    def validate_email_field(email):
        if '@gmail.com' not in email:
            raise forms.ValidationError("Email has to be gmail.com ")
        return email
    
    @staticmethod
    def validate_fullname_field(fullname):
        if '@gmail.com' in fullname:
            raise forms.ValidationError("Email has not in fullname ")
        return fullname


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}
    ))
    email = forms.EmailField( widget=forms.EmailInput(
        attrs={"class": "form-control"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password, password2)
        if password2 != password:
            raise forms.ValidationError(
                "Password1 and Password2 must be match"
            )
        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username has been taken !")
        return username
    

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email has been taken !")
        return email

