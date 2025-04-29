from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

import json
file=open(r'E:\CarsWebsite\CarProject\cars.json','r')
# file=open(r'E:\templates_inheritance\App\recipes.json','r')
json_data=file.read()
py_data=json.loads(json_data)

cars=py_data["cars"]

def CarsView(request):
    context={
        'cars' : cars,
    }
    return render(request, 'carsview.html', context)


def Cars(request, id):
    context={
        'cars' : cars[id - 1],
    }
    return render(request, 'cardetails.html',context)

def About(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')