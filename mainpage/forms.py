from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=250, label="Name")
  email = forms.EmailField(max_length=250, label="Email")
  message = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Enter your message here', 'rows':10, 'cols':10,}))

  