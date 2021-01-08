from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.trips, name='trips'),
    path('trips/<int:id>/', views.trip, name='trip'),
    path('trips/edit/<int:id>/', views.edit, name='edit'),
    path('trips/delete/<int:id>/', views.delete, name='delete'),
    path('trips/new/', views.new, name='new'),
    path('trips/<int:id>/entries/', views.trip_entries, name='trip_entries'),
    path('trips/<int:id>/entries/new/', views.new_entry, name='new_entry'),
    path('trips/<int:trip_id>/entries/edit/<int:entry_id>/', views.edit, name='edit_entry')
]
