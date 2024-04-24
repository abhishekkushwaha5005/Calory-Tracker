from django.shortcuts import render, redirect
from .models import Food, Consume
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
import requests
from django.http import JsonResponse
import json
import joblib
import math
API_KEYS = ""

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/index")
            else:
                return render(request, 'myapp/login.html', {'form': form, "error_message": "Invalid username or password"})
        else:
            return render(request, 'myapp/login.html', {'form': form, "error_message":None})
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})


def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/index')
    return render(request, 'myapp/delete.html')


def food_details(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': API_KEYS})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'myapp/food_info.html', {'api': api})
    else:
        return render(request, 'myapp/food_info.html', {'query': 'Enter a valid query'})
    
def bmi(request):
    if request.method == 'POST':
        prediction_mapper = {
            0 : "Extremely Weak",
            1 : "Weak",
            2 : "Normal",
            3 : "Overweight",
            4 : "Obesity",
            5 : "Extreme Obesity",
        }
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        if gender == 'male':
            gender = 0
        else:
            gender = 1
        bmi = round(float(weight) / ((float(height)/100) ** 2), 2)
        print(height, weight, gender)
        model = joblib.load('/Users/abhishekkushwaha/Dev/calary tracker/bmi_model.pkl') 
        model_response = math.floor(model.predict([[int(height), int(weight), gender]])[0])
        print(height, weight)
        print(bmi)
        return JsonResponse({"bmi": bmi, "model_response": prediction_mapper.get(model_response)})
    else:
        return render(request, 'myapp/bmi.html', {'query': 'Enter a valid query'})