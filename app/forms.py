from django.forms import ModelForm, Form, DateField

from app.models import Trip, Entry
from traveldiary import settings


class TripForm(ModelForm):

    class Meta:
        model = Trip
        fields = ['destination', 'date', 'cost', 'travel_agency', 'num_travellers']


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['date', 'content']

