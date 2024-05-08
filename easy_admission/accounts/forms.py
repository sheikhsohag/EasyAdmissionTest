from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from . models import ProfileModel, TeacherProfileModel


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


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Full Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Mother Name'}),
            'village': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Village'}),
            'subdistrict': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Subdistrict'}),
            'district': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'District'}),
            'ssc_board': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'SSC Board'}),
            'ssc_year': forms.NumberInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'SSC Passing Year'}),
            'ssc_result': forms.NumberInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'SSC Result'}),
            'hsc_board': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'HSC Board'}),
            'hsc_year': forms.NumberInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'HSC Passing Year'}),
            'hsc_result': forms.NumberInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'HSC  Result'}),
        }



class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfileModel
        fields = '__all__'
        widgets = {
            'cur_village': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Current Village'}),
            'cur_subdistrict': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Current Subdistrict'}),
            'cur_district': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Current District'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Full Name'}),
            'village': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Village'}),
            'subdistrict': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Subdistrict'}),
            'district': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'District'}),
            'phd': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'phd_checkbox'}),  # Assuming phd is a checkbox
            'dept': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Department'}),
            'title': forms.TextInput(attrs={'class': 'form-control py-3 border border-dark', 'placeholder': 'Title'}),
        }

