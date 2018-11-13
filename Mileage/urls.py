from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_me, name='about_me'),
    path('mileage_app', views.mileage_app, name='mileage_app'),
    path('add', views.add_user, name='mileage_form_add'),
    path('create', views.create_entry, name='mileage_form_create'),
    path('view', views.view_database, name='mileage_form_view'),
    path('add_user', views.mileage_app_form_add, name='mileage_form_add_user'),
    path('create_entry', views.mileage_app_form_create, name='mileage_form_create_entry'),
    path('view_database', views.mileage_app_form_view, name='mileage_form_view_database'),

    path('<int:user_id>', views.view_user, name='mileage_user'),
]
