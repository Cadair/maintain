import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .models import User, Car

# Create your views here.

@login_required(login_url='login')
def index(request):

    # Get all cars owned by user
    cars = request.user.cars.all()
    return render(request, "maintain/index.html", {
        "cars": cars,
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse(index))
        else:
            return render(request, "maintain/login.html", {
                "alert": "warning",
                "alert_message": "Invalid username or password"
            })
    else:
        return render(request, "maintain/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "maintain/register.html", {
                "alert": "warning",
                "alert_message": "Passwords must match"
            })

        # Create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "maintain/register.html", {
                "alert": "warning",
                "alert_message": "Username not available"
            })
        login(request, user)
        return redirect(reverse("index"))
    else:
        return render(request, "maintain/register.html")

def logout_view(request):
    logout(request)
    return redirect(reverse(index))

def car_view(request):

    # Get car from session
    car = get_default_car(request)
    return render(request, "maintain/car.html")

def get_car(request, car_id):
    try:
        car = request.user.cars.get(pk=car_id)
    except:
        return JsonResponse({"error": "Invalid request"}, status=400)

    if request.method == "GET":
        return JsonResponse(car.serialize())

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("default") is not None:
            car.default = data["default"]
            request.session['default_car'] = car.id
        car.save()
        return HttpResponse(status=204)

def get_default_car(request):
    car_id = request.session.get("default_car")
    car = Car.objects.get(pk=car_id)
    return car
