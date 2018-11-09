from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import mileage_user, mileage_entry

# Create your views here.


def index(request):
    context = {
        "mileage_user": mileage_user.objects.all()
    }
    return render(request, "Mileage/index.html", context)

def view_user(request, user_id):
    try:
        my_user_entry = mileage_user.objects.get(pk=user_id)
    except Mileage.DoesNotExist:
        raise Http404("User does not exist")
    context = {
        "user_person": my_user_entry
    }
    return render(request, "Mileage/mileagePage.html", context)
