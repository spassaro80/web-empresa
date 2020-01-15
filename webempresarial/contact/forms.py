from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder': "Introduzca su nombre"}))
    email=forms.EmailField(label="email", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder': "Introduzca su email"}))
    content=forms.CharField(label="Texto", widget=forms.Textarea(attrs={'class':'form-control','placeholder': "Introduzca su mensaje",'rows': 6}), required=True)