from django.shortcuts import render, redirect

from CarCollectionApp.car_collection.forms import ProfileForm
from CarCollectionApp.car_collection.models import Profile, Car


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)


def create_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/profile-create.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    context = {
        'profile': profile,
        'cars': cars
    }
    return render(request, 'common/catalogue.html', context)


def create_car(request):
    return render(request, 'cars/car-create.html')


def car_details(request, pk):
    return render(request, 'cars/car-details.html')


def edit_car(request, pk):
    return render(request, 'cars/car-edit.html')


def delete_car(request, pk):
    return render(request, 'cars/car-delete.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def edit_profile(request):
    return render(request, 'profile/profile-edit.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')