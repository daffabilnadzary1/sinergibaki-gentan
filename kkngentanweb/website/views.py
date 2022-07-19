from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'homepage.html', {
            'navbar': 'home',
        })

class Activity(View):
    def get(self, request,*args, **kwargs):
        return render(request, 'activities.html', {
            'navbar':'activity'
        })

class ActivityDetail(View):
    def get(self, request,*args, **kwargs):
        return render(request, 'activityDetail.html')