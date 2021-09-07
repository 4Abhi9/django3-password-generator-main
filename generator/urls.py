from django.urls import path
from generator import views

urlpatterns = [
    path('',views.home),
    path('generatedpassword/',views.password, name='password'),
    path('PageIntro/', views.intro, name='intro'),
]
    
