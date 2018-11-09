from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:user_id>', views.view_user, name="mileage_user"),
]
