from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Activity

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'homepage.html', {
            'navbar': 'home',
        })

class ActivityList(View):
    def get(self, request, *args, **kwargs):
        activities = Activity.published.all()
        return render(request, 'activities.html', {
            'activities': activities,
            'navbar':'activity',
        })

class ActivityDetail(View):
    def get(self, request, activity, *args, **kwargs):
        activity = get_object_or_404(Activity, slug = activity, status = "published")
        return render(request, 'activityDetail.html', {
            'activity': activity,
        })

class Testing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'testing.html')