from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from spms1.forms import LoginForm
from spms1.models import login
from .models import Vehicle, Category
from .forms import VehicleForm, CategoryForm
import random
from django.contrib import messages
from django.utils import timezone

def index (request):
    return render(request, 'index.html')
def AccountSettings (request):
    return render(request, 'Account Settings.html')

def login_page(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=login.objects.filter(
                username=username,
                password=password
            ).exists()
        if user:
            return redirect('dashboard')
        else:
            messages.error(
                request,"Invalid Username or Password"
            )
    return render(
        request,'index.html',{'form':form}
    )

def index(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = login.objects.filter(
            username=username,
            password=password
        )

        if user.exists():
            return redirect('dashboard')

        else:
            return render(request,'index.html',{'error':True})

    return render(request,'index.html')

def dashboard(request):

    vehicles_parked = Vehicle.objects.filter(
        parking_status='Parked'
    ).count()

    departed_vehicles = Vehicle.objects.filter(
        parking_status='Leaved'
    ).count()

    available_category = Category.objects.count()

    total_earnings = 0

    vehicles = Vehicle.objects.all()

    for i in vehicles:

        total_earnings += float(i.charges)

    total_records = Vehicle.objects.count()

    total_slots = 0

    categories = Category.objects.all()

    for i in categories:

        total_slots += i.vehicle_limit

    context = {

        'vehicles_parked': vehicles_parked,

        'departed_vehicles': departed_vehicles,

        'available_category': available_category,

        'total_earnings': total_earnings,

        'total_records': total_records,

        'total_slots': total_slots,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


# INSERT VEHICLE

def VehicleEntry(request):

    data = Vehicle.objects.all()

    if request.method == "POST":

        vehicle_number = request.POST.get('vehicle_number')

        vehicle_type_id = request.POST.get('vehicle_type')

        category = Category.objects.get(id=vehicle_type_id)

        Vehicle.objects.create(

            vehicle_number=vehicle_number,

            vehicle_type=category,

            area_number=category.parking_area_number,

            charges=category.parking_charge,

            parking_status='Parked'

        )

        messages.success(
            request,
            "Vehicle Added Successfully"
        )

        return redirect('VehicleEntry')

    form = VehicleForm()

    return render(
        request,
        'VehicleEntry.html',
        {
            'form': form,
            'data': data
        }
    )

def Reports(request):

    vehicle_data = None

    search_number = request.GET.get('vehicle_number')

    if search_number:

        vehicle_data = Vehicle.objects.filter(
            vehicle_number=search_number
        ).first()

    return render(
        request,
        'Reports.html',
        {
            'vehicle_data': vehicle_data
        }
    )

def search(request):

    vehicle_data = None

    search_number = request.GET.get('vehicle_number')

    if search_number:

        vehicle_data = Vehicle.objects.filter(
            vehicle_number=search_number
        )

    return render(
        request,
        'search.html',
        {
            'vehicle_data': vehicle_data
        }
    )


# VIEW VEHICLES

def ManageVehicles(request):

    search = request.GET.get('search')

    if search:

        data = Vehicle.objects.filter(
            vehicle_type__vehicle_type__icontains=search
        )

    else:

        data = Vehicle.objects.all()

    return render(
        request,
        'ManageVehicle.html',
        {
            'data': data
        }
    )

def ToggleVehicleStatus(request, id):

    obj = Vehicle.objects.get(id=id)

    if obj.parking_status == 'Parked':

        obj.parking_status = 'Leaved'

        obj.departure_time = timezone.now()

    else:

        obj.parking_status = 'Parked'

        obj.departure_time = None

    obj.save()

    messages.success(
        request,
        "Vehicle Status Updated Successfully"
    )

    return redirect('ManageVehicles')


# UPDATE VEHICLE


def UpdateCategory(request, id):

    obj = Category.objects.get(id=id)

    form = CategoryForm(instance=obj)

    if request.method == "POST":

        form = CategoryForm(
            request.POST,
            instance=obj
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Category Updated Successfully"
            )

            return redirect('category')

    return render(
        request,
        'UpdateCategory.html',
        {'form': form}
    )

# DELETE VEHICLE

def DeleteVehicle(request, id):

    obj = Vehicle.objects.get(id=id)

    obj.delete()

    messages.success(
        request,
        "Vehicle Deleted Successfully"
    )

    return redirect('VehicleEntry')

def category(request):

    form = CategoryForm()

    data = Category.objects.all()

    if request.method == "POST":

        form = CategoryForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Category Added Successfully"
            )

            return redirect('category')

    return render(
        request,
        'category.html',
        {
            'form': form,
            'data': data
        }
    )


# DELETE VEHICLE

def DeleteCategory(request, id):

    obj = Category.objects.get(id=id)

    obj.delete()

    messages.success(
        request,
        "Category Deleted Successfully"
    )

    return redirect('category')

def ToggleCategoryStatus(request, id):

    obj = Category.objects.get(id=id)

    obj.status = not obj.status

    obj.save()

    return redirect('category')

def UpdateVehicle(request, id):

    obj = Vehicle.objects.get(id=id)

    if request.method == "POST":

        vehicle_number = request.POST.get('vehicle_number')

        vehicle_type_id = request.POST.get('vehicle_type')

        category = Category.objects.get(id=vehicle_type_id)

        obj.vehicle_number = vehicle_number

        obj.vehicle_type = category

        obj.area_number = category.parking_area_number

        obj.charges = category.parking_charge

        obj.save()

        messages.success(
            request,
            "Vehicle Updated Successfully"
        )

        return redirect('VehicleEntry')

    categories = Category.objects.all()

    return render(
        request,
        'UpdateVehicle.html',
        {
            'obj': obj,
            'categories': categories
        }
    )

# FORGOT PASSWORD PAGE

def forgot_password(request):

    if request.method == "POST":

        mobile = request.POST.get('mobile')

        user = login.objects.filter(mobile=mobile).first()

        if user:

            otp = random.randint(1000, 9999)

            request.session['otp'] = str(otp)
            request.session['mobile'] = mobile

            # TEMPORARY OTP DISPLAY
            print("OTP is:", otp)

            messages.success(request, f"OTP Generated: {otp}")

            return redirect('verify_otp')

        else:

            messages.error(request, "Mobile Number Not Found")

    return render(request, 'forgot_password.html')


# VERIFY OTP

def verify_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get('otp')

        saved_otp = request.session.get('otp')

        if entered_otp == saved_otp:

            return redirect('dashboard')

        else:

            messages.error(request, "Invalid OTP")

    return render(request, 'verify_otp.html')