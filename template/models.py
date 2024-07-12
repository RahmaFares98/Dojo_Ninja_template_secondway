
# Create your models here.
# your_app_name/models.py
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=25)
    desc = models.TextField(default="old dojo")  # Added default value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #ninjas

def create_dojo( name, city, state):
    dojo_type=Dojo.objects.create(name=name ,city=city,state=state)
    return dojo_type


def delete_dojo(dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)  # Use id=dojo_id for primary key lookup
    dojo.delete()
    return dojo

    
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)

def create_ninja (first_name, last_name, dojo_id):
    Ninja_user=Ninja.objects.create(first_name=first_name, last_name=last_name,dojo_id=dojo_id)
    return Ninja_user


