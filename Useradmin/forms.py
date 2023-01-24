from django import forms
from django.contrib.auth.models import User
from .models import ExtendedUser


class MySignUpForm(forms.ModelForm):
    # additional fields to default Django User
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    gender = forms.CharField(widget=forms.Select(choices=ExtendedUser.GENDERS))
    street = forms.CharField()
    house_number = forms.IntegerField()
    plz = forms.IntegerField()
    city = forms.CharField()
    mobile_number = forms.IntegerField(required=False)
    profile_picture = forms.ImageField(required=False)

    # fields inherited from Django User
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput()
        }

class MyEditUpForm(forms.ModelForm):
    # fields inherited from Django User
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'password': forms.PasswordInput()
        }


class MyExtendedUpForm(forms.ModelForm):
    # fields inherited from Django User
    class Meta:
        model = ExtendedUser
        fields = ('date_of_birth', 'gender', 'street', 'house_number', 'plz', 'city', 'mobile_number')

class MyProfilePictureEditForm(forms.ModelForm):
    # fields inherited from Django User
    class Meta:
        model = ExtendedUser
        fields = ('profile_picture', )
