from django import forms
from django.forms import ModelForm
from .models import Person, Age, Upload


class PersonForm(ModelForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password', 'confirm_password')  # '__all__'

        # widgets = {
  #           'username': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
  #       }


class AgeForm(ModelForm):

    class Meta:
        model = Age
        fields = '__all__'


class UploadForm(ModelForm):

    class Meta:
        model = Upload
        fields = '__all__'