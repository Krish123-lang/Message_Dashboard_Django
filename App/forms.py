from django import forms
from App.models import Customer
from multiupload.fields import MultiFileField



class Customerform(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'


class EmailForm(forms.Form):
    email = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)