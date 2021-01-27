from django.shortcuts import render

# Create your views here.

def disseases(request):
    return render(request, 'Disseases/disseases.html',{})