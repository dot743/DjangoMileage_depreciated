from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import *
from .readMileageCSV import *

# Create your views here.

# Home page
def index(request):
    return render(request, "Mileage/comingsoon.html")

# Mileage app main page
def mileage_app(request):
    return render(request, "Mileage/mileage_app.html")

# Render "add user" form to render into "mileage app" page
def add_user(request):
    return render(request, "Mileage/mileage_app_form_add_user.html")

# Grab "add user" POST data from input forms
def mileage_app_form_add(request):
    my_username = request.POST.get('my_username')
    my_email = request.POST.get('my_email')
    my_password = request.POST.get('my_password')

    my_user = mileage_user(username = my_username, email = my_email)
    my_user.save()

    my_userID = mileage_user.objects.filter(username = my_username)

    context = {
        "message": f"{my_username} has been successfully created",
        "username": my_username,
        "email": my_email,
        "password": my_password,
        "userid": my_userID
    }
    return render(request, "Mileage/success.html", context)

# Render "create entry" form to render into "mileage app" page
def create_entry(request):

    context = {
        "locationList": findAllLocations()
    }
    return render(request, "Mileage/mileage_app_form_create_entry.html", context)

# Grab "create entry" POST data from input forms
def mileage_app_form_create(request):
    my_userid = request.POST.get('grab_user_ID')
    my_entry_date = request.POST.get('dateOne')
    location_list = []
    i = 1
    # Reads up to a maximum of 10 locations


    while i < 10:
        my_location_entry = request.POST.get("location" + str(i))
        print(f"The location entry at box : {my_location_entry}")
        if my_location_entry is None:
            break
        location_list.append(my_location_entry)
        i += 1
    my_miles_driven = calculateTotalDisance(location_list)
    my_mileage_user = mileage_user.objects.get(pk = my_userid)
    my_entry = mileage_entry(date_entered = my_entry_date, locations = location_list, miles_driven = my_miles_driven, mileage_user_key = my_mileage_user)
    my_entry.save()

# This is where I add into my new table

    try:
        for i in range(len(location_list)):
            my_entry = Trip(date_driven = my_entry_date, location_1 = location_list[i], location_2 = location_list[i+1], miles_driven = my_miles_driven, userID_trip = my_mileage_user
    except IndexError:
        pass

######

    context = {
    "locationList": findAllLocations(),
    "my_userid": my_userid,
    "my_entry_date": my_entry_date,
    "location_list": location_list,
    "my_miles_driven": my_miles_driven,
    "entry_added": True,
    "message": f"{my_userid} - {my_mileage_user.username}, your entry has been added. You have driven: \n {my_miles_driven} - {location_list}"
    }
    return render(request, "Mileage/success.html", context)

# Render "view database" form to render into "mileage app" page
def view_database(request):
    return render(request, "Mileage/mileage_app_form_view_database.html")

# "View database" queries
def mileage_app_form_view(request):

    my_userid = request.POST.get('myUserID')
    my_username = request.POST.get('myUsername')
    my_email = request.POST.get('myEmail')
    if my_userid != '':
        all_location_entries = mileage_entry.objects.filter(mileage_user_key_id = my_userid).order_by('date_entered')
        user_object = mileage_user.objects.get(id=my_userid)
        all_trip_entries = Trip.objects.filter(mileage_user_key_id = my_userid).order_by('date_driven'))
    # elif my_username != '':
    #     all_location_entries = mileage_entry.objects.filter(mileage_user = my_username).all()
    # elif my_email != '':
    #     all_location_entries = mileage_entry.objects.filter(mileage_user = my_email).all()



    print("This is all_location_entries: ")
    print(all_location_entries)
    print_locations = []
    print_location_entry = ''
    print_location_entry2 = ''
    location_list = convertLocationQueryToLocationList(all_location_entries)
    # for each_day in location_list:
    #     for location_number in range(len(each_day)):
    #         print_location_entry += each_day[location_number]
    #         if location_number < len(all_location_entries):
    #             print_location_entry += ' -> '
    #     print_locations.append(print_location_entry)
    context = {
    "my_userid": my_userid,
    "my_username": user_object.username,
    "my_email": my_email,
    "message": f"{my_userid} - {user_object.username}, Your mileage this month is: ",
    "print_locations": print_locations,
    "all_location_entries": all_location_entries,
    "all_trip_entries": all_trip_entries
    }
    return render(request, "Mileage/success.html", context)

def error_page(request):
    return render(request, "Mileage/error.html")
    # render(request, "Mileage/error.html")

def about_me(request):
    return render(request, "Mileage/about_me.html")

def view_user(request, user_id):
    try:
        my_user_entry = mileage_user.objects.get(pk=user_id)
    except Mileage.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        "user_person": my_user_entry
    }
    return render(request, "Mileage/mileagePage.html")
