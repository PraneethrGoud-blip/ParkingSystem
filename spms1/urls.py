from django.urls import path
from django.contrib import admin
from spms1 import views

urlpatterns=[
    path('admin/',admin.site.urls),

    path('',views.index,name='index'),
    path('dashboard.html',views.dashboard,name='dashboard'),
    path('Account Settings.html',views.AccountSettings,name='Account Settings'),
    path('category.html/',views.category,name='category'),
    path('ManageVehicles.html',views.ManageVehicles,name='ManageVehicles'),
    path('Reports.html',views.Reports,name='Reports'),
    path('search.html',views.search,name='search'),
    path('VehicleEntry.html',views.VehicleEntry,name='VehicleEntry'),

    path('ManageVehicles/',views.ManageVehicles,name='ManageVehicles'),

    path(
    'UpdateCategory/<int:id>/',
    views.UpdateCategory,
    name='UpdateCategory'
),

path(
    'DeleteCategory/<int:id>/',
    views.DeleteCategory,
    name='DeleteCategory'
),

path(
    'ToggleCategoryStatus/<int:id>/',
    views.ToggleCategoryStatus,
    name='ToggleCategoryStatus'
),

path(
    'UpdateVehicle/<int:id>/',
    views.UpdateVehicle,
    name='UpdateVehicle'
),

path(
    'ToggleVehicleStatus/<int:id>/',
    views.ToggleVehicleStatus,
    name='ToggleVehicleStatus'
),

path(
    'DeleteVehicle/<int:id>/',
    views.DeleteVehicle,
    name='DeleteVehicle'
),

path(
    'forgot_password/',
    views.forgot_password,
    name='forgot_password'
    ),

path('verify_otp/', 
     views.verify_otp, 
     name='verify_otp'
     ),
]