from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.decorators import login_required
from wanderful.forms import TravelerForm, LocationForm, TravelListForm
from geolocation.google_maps import GoogleMaps
from wanderful.models import *
# Create your views here.
#test github

def home(request):
    return render_to_response("home.html")

def testing2(request):
    return render_to_response("map.html")

def testing3(request):
    return render_to_response("testing3.html")

### traveler
def traveler(request):
    travelers = Traveler.objects.all()
    return render_to_response("traveler/traveler.html", {'travelers': travelers})

def view_traveler(request, traveler_id):
    traveler = Traveler.objects.get(id=traveler_id)
    data = {'traveler': traveler}
    return render_to_response("traveler/view_traveler.html", data)

def new_traveler(request):
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = TravelerForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Genre object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/traveler")
    # Else if the user is looking at the form page
    else:
        form = TravelerForm()

    data = {'form': form}
    return render(request, "traveler/new_traveler.html", data)


### location
def location(request):
    locations = Location.objects.all()
    return render_to_response("location/location.html", {'locations': locations})

def view_location(request, location_id):
    location = Location.objects.get(id=location_id)
    data = {'location': location}
    # image = Location.image.url
    return render_to_response("location/view_location.html", data)

def new_location(request):
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = LocationForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Genre object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/location")
    # Else if the user is looking at the form page
    else:
        form = LocationForm()

    data = {'form': form}
    return render(request, "location/new_location.html", data)


### travel list
@login_required
def travellist(request):
    travellists = TravelList.objects.all()
    return render_to_response("travellist/travellist.html", {'travellists': travellists})

@login_required
def view_travellist(request, travellist_id):
    travellist = Location.objects.all().filter(userlist=travellist_id)
    data = {'travellist': travellist}
    return render_to_response("travellist/view_travellist.html", data)

@login_required
def new_travellist(request):
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = TravelListForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Genre object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/travellist")
    # Else if the user is looking at the form page
    else:
        form = TravelListForm()

    data = {'form': form}
    return render(request, "travellist/new_travellist.html", data)



def profile(request):
    if not request.user.is_authenticated():
        return redirect("login")

    return render(request, "registration/profile.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def map(request):

    #all_locations = Location.objects.all()

    address = "225 Bush Street San Francisco California"

    google_maps = GoogleMaps(api_key='AIzaSyDlHBtlOb1-JpUPZ8CHAZqaNha6Uw_l_ow')

    location_info = google_maps.query(location=address)

    location_info = location_info.first()

    data = {"location_info":location_info}


    return render(request, "map.html", data)
