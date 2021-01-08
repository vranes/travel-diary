from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import TripForm, EntryForm
from app.models import Trip, Entry


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Login page'})
    else:
        return redirect('app:trips')


@login_required
def trips(req):
    tmp = Trip.objects.all()
    return render(req, 'trips.html', {'trips': tmp})

@login_required
def trip(req, id):
    tmp = get_object_or_404(Trip, id=id)
    return render(req, 'trip.html', {'trip': tmp, 'page_title': tmp.destination})

@permission_required('app.add_trip')
def new(req):
    if req.method == 'POST':
        form = TripForm(req.POST)
        print(form.is_valid())
        if form.is_valid():
            a = Trip(destination=form.cleaned_data['destination'], date=form.cleaned_data['date'], cost=form.cleaned_data['cost'], travel_agency=form.cleaned_data['travel_agency'], num_travellers = form.cleaned_data['num_travellers'])
            a.save()
            return redirect('app:trips')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = TripForm()
        return render(req, 'new.html', {'form': form})

@permission_required('app.change_trip')
def edit(req, id):
    if req.method == 'POST':
        form = TripForm(req.POST)

        if form.is_valid():
            t = Trip.objects.get(id=id)
            t.destination = form.cleaned_data['destination']
            t.date = form.cleaned_data['date']
            t.cost = form.cleaned_data['cost']
            t.travel_agency = form.cleaned_data['travel_agency']
            t.num_travellers = form.cleaned_data['num_travellers']
            t.save()
            return redirect('app:trips')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        t = Trip.objects.get(id=id)
        form = TripForm(instance=t)
        return render(req, 'edit.html', {'form': form, 'id': id})

def delete(req, id):
    tmp = get_object_or_404(Trip, id=id)
    tmp.delete()
    #Trip.delete(tmp)
    return redirect('app:trips')

@login_required
def trip_entries(req, id):
    tmp = get_object_or_404(Trip, id=id)
    return render(req, 'entry/entries.html', {'trip': tmp})

@permission_required('app.add_entry')
def new_entry(req, id):
    if req.method == 'POST':
        form = EntryForm(req.POST)

        if form.is_valid():
            tmp = get_object_or_404(Trip, id=id)
            a = Entry(date=form.cleaned_data['date'], content=form.cleaned_data['content'], traveller=req.user, trip=tmp)
            a.save()
            return redirect('app:trip_entries', id)
        else:
            return render(req, 'entry/new_entry.html', {'form': form, 'id': id})
    else:
        form = EntryForm()
        return render(req, 'entry/new_entry.html', {'form': form, 'id': id})

@permission_required('app.change_entry')
def edit_entry(req, trip_id, entry_id):
    if req.method == 'POST':
        form = EntryForm(req.POST)

        if form.is_valid():
            e = Entry.objects.get(id=entry_id)
            e.date = form.cleaned_data['date']
            e.content = form.cleaned_data['content']
            e.save()
            return redirect('app:trip_entries', trip_id)
        else:
            return render(req, 'edit_entry.html', {'form': form, 'trip_id': trip_id, 'entry_id': entry_id})
    else:
        e = Entry.objects.get(id=entry_id)
        form = EntryForm(instance=e)
        return render(req, 'edit_entry.html', {'form': form, 'trip_id': trip_id, 'entry_id': entry_id})
