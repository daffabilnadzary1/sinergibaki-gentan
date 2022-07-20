from django.shortcuts import render, redirect
from django.views import View
from .models import Activity

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'homepage.html', {
            'navbar': 'home',
        })

class Activity(View):
    def get(self, request,*args, **kwargs):
        activities = Activity.published.all()
        return render(request, 'activities.html', {
            'activities': activities,
            'navbar':'activity'
        })

class ActivityDetail(View):
    def get(self, request,*args, **kwargs):
        return render(request, 'activityDetail.html')

class Testing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'testing.html')