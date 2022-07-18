from django.urls import path
from .views import Home, Activity, ActivityDetail

app_name = 'website'

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('activity/', Activity.as_view(), name = 'activity'),
    path('activityDetail/', ActivityDetail.as_view(), name = 'activityDetail'),
]