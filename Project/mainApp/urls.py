
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('profile/',views.profile,name="index"),
    path('analytics/',views.analytics,name="analytics"),
    path('calendar/',views.calendar,name="calendar"),
    path('datasources/',views.datasources,name="datasources"),
    
    path('usercentric/', views.usercentric, name="usercentric"),  # List and form submission
    path('usercentric/<int:adprojid>/', views.usercentric_detail, name="usercentric_detail"),  # Detail view

]
