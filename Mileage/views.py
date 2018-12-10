from django.shortcuts import render
from django.http import HttpResponse, Http404

# from rest_framework.views import APIView
from json import *

from .models import *
from .readMileageCSV import *

import datetime

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
            my_miles_driven = calculateTotalDisance([location_list[i], location_list[i+1]])
            print(f"i: {i}")
            print(f"location1: {location_list[i]}")
            print(f"location2: {location_list[i+1]}")
            print(f"Date_driven: {my_entry_date}")
            my_entry = Trip(date_driven = my_entry_date, location_1 = location_list[i], location_2 = location_list[i+1], miles_driven = my_miles_driven, mileage_user_key = my_mileage_user)
            my_entry.save()
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
        all_trip_entries = Trip.objects.filter(mileage_user_key_id = my_userid).order_by('date_driven')

    all_trip_entries_grouped = []
    try:
        for i in range(len(all_trip_entries)):
            all_trip_entries_grouped.append(all_trip_entries[i])
            if all_trip_entries[i].date_driven != all_trip_entries[i+1].date_driven:
                print("Does not match!!")
                all_trip_entries_grouped.append(" ")
                # print("found a match at: " + str(i))
                # print("location 1: ")
                # print(all_trip_entries[i].date_driven)
                # print(all_trip_entries[i].location_1)
                # print(all_trip_entries[i].location_2)
                # print("location 2: ")
                # print(all_trip_entries[i+1].date_driven)
                # print(all_trip_entries[i+1].location_1)
                # print(all_trip_entries[i+1].location_2)
    except IndexError:
        print("Hi")
        pass

    print("Here is allTRIP locations grouped")
    for each in all_trip_entries:
        print(each)

    format_output = []
    format_output2 = []
    dates_driven_list = []
    one_days_mileage = 0
    daily_mileage_list = []

    temp1 = 0

    for i in range(len(all_trip_entries)):
        if i == 0:
            format_output2.append(all_trip_entries[i].location_1)
            format_output2.append(all_trip_entries[i].location_2)
            dates_driven_list.append(str(all_trip_entries[i].date_driven))
            one_days_mileage += calculateTotalDisance([all_trip_entries[i].location_1, all_trip_entries[i].location_2])
        elif all_trip_entries[i].date_driven == all_trip_entries[i-1].date_driven:
            format_output2.append(all_trip_entries[i].location_1)
            format_output2.append(all_trip_entries[i].location_2)
            one_days_mileage += calculateTotalDisance([all_trip_entries[i].location_1, all_trip_entries[i].location_2])
        elif all_trip_entries[i].date_driven != all_trip_entries[i-1].date_driven:
            format_output.append(format_output2)
            format_output2 = []
            daily_mileage_list.append(round(one_days_mileage,1))
            one_days_mileage = 0
            format_output2.append(all_trip_entries[i].location_1)
            format_output2.append(all_trip_entries[i].location_2)
            dates_driven_list.append(str(all_trip_entries[i].date_driven))
            one_days_mileage += calculateTotalDisance([all_trip_entries[i].location_1, all_trip_entries[i].location_2])
        if i == len(all_trip_entries)-1:
            format_output.append(format_output2)
            daily_mileage_list.append(round(one_days_mileage,1))

    # try:
    #     for i in range(len(all_trip_entries)):
    #         format_output2.append(all_trip_entries[i].location_1)
    #         print(format_output2)
    #         format_output2.append(all_trip_entries[i].location_2)
    #         print(format_output2)
    #         if all_trip_entries[i].date_driven != all_trip_entries[i+1].date_driven:
    #             format_output.append(format_output2)
    #             print("***Putting in format_output2***")
    #             dates_driven_list.append(str(all_trip_entries[i].date_driven))
    #             print(type(dates_driven_list[i]))
    #             print(str(dates_driven_list[i]))
    #             format_output2 = []
    # except IndexError:
    #     print("***Putting in format_output2***")
    #     format_output.append(format_output2)
    #     dates_driven_list.append(str(all_trip_entries[len(all_trip_entries)-1].date_driven))

    print("~~~~~~~~~~~~~~~~~~~")
    print("All schools per day with duplicates")
    print(format_output)

#set(list_item)

    format_output4 = []
    for i in range(len(format_output)):
        format_output3 = []
        for y in range(len(format_output[i])):
            try:
                if format_output[i][y] != format_output[i][y+1]:
                    format_output3.append(format_output[i][y])
            except IndexError:
                format_output3.append(format_output[i][y])
                pass
        format_output4.append(format_output3)

    print("~~~~~~~~~~~~~~~~~~~")
    print("All schools per day NO DUPLICATES")
    print(format_output4)
    print("~~~~~~~~~~~~~~~~~~~")

    location_output_arrow = []

    for each in format_output4:
        location_output_arrow.append(addArrows(each))

    print_locations = []
    print_location_entry = ''
    print_location_entry2 = ''
    location_list = convertLocationQueryToLocationList(all_location_entries)

    context = {
    "my_userid": my_userid,
    "my_username": user_object.username,
    "my_email": my_email,
    "message": f"{my_userid} - {user_object.username}, Your mileage this month is: ",
    "print_locations": print_locations,
    "all_location_entries": all_location_entries,
    "all_trip_entries": all_trip_entries,
    "all_trip_entries_grouped": all_trip_entries_grouped,
    "location_output_arrow": location_output_arrow,
    "dates_driven_list": dates_driven_list,
    "daily_mileage_list": daily_mileage_list
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


# class UserDateAPIView(APIView):
#
#     def get(self, request, user_id, *args, **kwargs):
#         user = User.objects.get(id=user_id)
#         return json.dumps({'last_date':user.last_date})
