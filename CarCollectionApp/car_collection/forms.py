from django import forms
from CarCollectionApp.car_collection.models import Profile, Car


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class ProfileDeleteForm(ProfileEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if self.instance:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


class CarDeleteForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_read_only_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_read_only_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

