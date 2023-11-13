from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'gst_number']



class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    message_text = forms.CharField(widget=forms.Textarea)
