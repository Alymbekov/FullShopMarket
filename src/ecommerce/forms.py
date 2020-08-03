from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "id_fullname",
            "placeholder": "Your FullName"
        }
    )
    )
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "id": "id_email",
            "placeholder": "Your email"
        }
    )
    )

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "id": "id_content",
            "placeholder": "Your content"
        }
    )
    )

    def clean_email(self):
        return self.validate_email_field(self.cleaned_data.get("email"))

    @staticmethod
    def validate_email_field(email):
        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to be gmail.com ")
        return email

    def clean_fullname(self):
        return self.validate_fullname_field(self.cleaned_data.get("fullname"))

    @staticmethod
    def validate_fullname_field(fullname):
        if "gmail.com" in fullname:
            raise forms.ValidationError("Email has not be in FullName ")
        return fullname


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username has been taken! ")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email has been taken! ")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password, password2)
        if password2 != password:
            raise forms.ValidationError(
                "Password1 and Password2 must be match")
        return data
