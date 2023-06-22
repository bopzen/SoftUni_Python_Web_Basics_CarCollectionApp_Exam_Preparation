from django.urls import path, include

from CarCollectionApp.car_collection.views import index, create_profile, catalogue, create_car, car_details, edit_car,\
    delete_car, profile_details, edit_profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create-profile'),
        path('details/', profile_details, name='profile-details'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile')
    ])),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', create_car, name='create-car'),
        path('<int:pk>/details/', car_details, name='car-details'),
        path('<int:pk>/edit/', edit_car, name='edit-car'),
        path('<int:pk>/delete/', delete_car, name='delete-car')
    ]))
]