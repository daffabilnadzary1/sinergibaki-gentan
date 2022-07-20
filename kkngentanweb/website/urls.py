from django.urls import path
from .views import Home, ActivityList, ActivityDetail, Testing

app_name = 'website'

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('activity/', ActivityList.as_view(), name = 'activity'),
    path('activity/<slug:activity>', ActivityDetail.as_view(), name = 'activityDetail'),
    path('testing/', Testing.as_view(), name ='testing'),
]