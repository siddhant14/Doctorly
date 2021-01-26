from django.shortcuts import render
from .models import Hospital
# Create your views here.

def Hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'Hospitals/Hospital_list.html', {'hospitals' : hospitals})
