
# Create your views here.
# your_app_name/views.py
from django.shortcuts import render, redirect , get_object_or_404
from .models import Dojo, Ninja
from . import models

def index(request):
    dojos = Dojo.objects.all() #gets all the records in the tabl
    ninjas=Ninja.objects.all()#gets all the records in the tabl
    dojos_with_ninjas = [] #define a list
    for dojo in dojos:
        ninjas = Ninja.objects.filter(dojo_id=dojo.id) # to put dojo in the right selected ninja
        dojos_with_ninjas.append({
            'dojo': dojo,
            'ninja': ninjas,
            'ninja_count': ninjas.count(), #to count how many ninjas in Dojo 
        })
        print (dojos_with_ninjas)
    context = {
        'dojos': dojos,
        'ninjas': ninjas,
        'dojos_with_ninjas': dojos_with_ninjas
    }
    return render(request, 'index.html', context)

def add_dojo(request):#  let user added dojo types like (doctor, arch, painting)
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        models.create_dojo(name=name, city=city, state=state)
    return redirect('/')

def delete_btn(request,dojo_id): #when Click delete the data 
    models.delete_dojo(dojo_id)# call delete_dojo from Models
    return redirect('/')

def add_ninja(request):# add ninja users 
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dojo_id = request.POST.get('dojo') # to choose Ninja with Dojo (Rahma-Painting)
        models.create_ninja(first_name=first_name, last_name=last_name, dojo_id=dojo_id)
    return redirect('/') #all these in one page route 
