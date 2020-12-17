from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer
from .models import Car
from datetime import datetime

def index(request): 
    visits = int(request.COOKIES.get('visits', '1'))

    reset_last_visit_time = False
    response = render(request, 'index.html', {'visits':visits})
    if 'last_visit' in request.COOKIES: 
        last_visit = request.COOKIES['last_visit'] 
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S") 
        if (datetime.now() - last_visit_time).total_seconds() > 0.5:
            visits = visits + 1 
            reset_last_visit_time = True
    else: 
        reset_last_visit_time = True

        
        response = render(request, 'index.html', {'visits':visits})

    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits) 
    return response

    
# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

