from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


type_choices = [
    ('student', 'Student'), 
    ('teacher', 'Teacher')
]

username_validator = UnicodeUsernameValidator()

class UserForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=type_choices, required=True, help_text=None,
                                widget=forms.Select(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Select Account Type'}))

    first_name = forms.CharField(max_length=19, required=True, help_text=None,
                                widget=forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=19, required=True, help_text=None,
                               widget=(forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder':'Last Name'})))
    
    email = forms.EmailField(max_length=50, help_text=None,
                             widget=(forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder':'Email'})))
    
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder':'Password'})),
                                help_text=None)
    
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder':'Conformation Password'}),
                                help_text=None)
    
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        help_text=None,
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control py-3  border-dark', 'placeholder':'Username'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'account_type')
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', _("Passwords do not match."))
        
        return cleaned_data


    
class UserLogInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
