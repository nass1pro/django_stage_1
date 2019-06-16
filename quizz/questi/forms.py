from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="your_name", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)
