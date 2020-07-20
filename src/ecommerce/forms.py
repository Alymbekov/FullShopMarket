from django import forms

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


    
