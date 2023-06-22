from django import forms
from CarCollectionApp.car_collection.models import Profile, Car


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput()
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
