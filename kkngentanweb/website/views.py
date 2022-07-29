from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Activity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
import pandas as pd

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'homepage.html', {
            'navbar': 'home',
        })

class ActivityList(View):
    def get(self, request, *args, **kwargs):
        activities = Activity.published.all()
        #search functionality
        query = request.GET.get('q')
        if query:
            activities = Activity.published.filter(Q(title__icontains=query)).distinct()
        paginator = Paginator(activities, 6)
        page = request.GET.get('page')
        try:
            activities = paginator.page(page)
        except PageNotAnInteger:
            activities = paginator.page(1)
        except EmptyPage:
            activities = paginator.page(paginator.num_pages)

        return render(request, 'activities.html', {
            'activities': activities,
            page:'pages',
            'navbar':'activity',
        })

class ActivityDetail(View):
    def get(self, request, activity, *args, **kwargs):
        activities = Activity.published.all()[:4]
        activity = get_object_or_404(Activity, slug = activity, status = "published")
        return render(request, 'activityDetail.html', {
            'activity': activity,
            'activities': activities,
        })

class Testing(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'testing.html')

class Chart(View):
    def get(self, request, *args, **kwargs):
        data = {
            "sales": 100,
            "customers":10,
        }
        return JsonResponse(data) #http response

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')

class Testing(View):
    # data = pd.read_csv('kkngentanweb\static\file\data_sampah-1.csv')
    def get(self, request, *args, **kwargs):
        # values = data.values
        # keys = data.keys()

        # listkeys = []
        # listvalues = []

        # for x in keys:
        #     listkeys.append(x)
        # for x in values:
        #     listvalues.append(x)
        
        # values = pd.DataFrame(listvalues).to_dict(orient = 'records')
        # keys = pd.DataFrame(listkeys).to_dict(orient = 'records')

        # return render(request, 'testing.html',{
        #     'values':values,
        #     'keys':keys,
        # })

        return render(request, 'testing.html')
