from django.shortcuts import render ,HttpResponse as http
from django.db.models import Count


from .models import Address, Student 
# Create your views here.

def index(request):
    objects = Address.objects.annotate(num_student= Count('student'))
    return http(f"Addresses with student counts: {', '.join([f'{obj.city}: {obj.num_student}' for obj in objects])}")
