from django import forms

from .models import filename

class filenameForm(forms.ModelForm):
    class Meta:
        model = filename
        fields=['file','email_id']

    def clean_email_id(self):
        email=self.cleaned_data.get('email_id')
        email_base,provider = email.split("@")
        domain, extension = provider.split('.')

        if not extension =="com":
            raise forms.ValidationError("Please use .com extension id")
        return email

    def clean_file(self):
        file= self.cleaned_data.get('file')
        return file

    def clean_Training(self):
        Training = self.cleaned_data.get('Training')
        return Training

    """def clean_Testing(self):
        Testing=self.cleaned_data.get('Testing')
        return Testing

    def clean_id1(self):
        id1=self.cleaned_data.get('id1')
        return id1"""


