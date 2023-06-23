from django.shortcuts import render, redirect

from CarCollectionApp.car_collection.forms import ProfileForm, CarForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
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
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CarForm()
    else:
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'cars/car-create.html', context)


def car_details(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()
    context = {
        'profile': profile,
        'car': car
    }
    return render(request, 'cars/car-details.html', context)


def edit_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarForm(instance=car)
    else:
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'car': car,
        'form': form
    }
    return render(request, 'cars/car-delete.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    context = {
        'profile': profile,
        'cars': cars,
        'total_price': total_price
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/profile-delete.html', context)