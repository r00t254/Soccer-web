from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.Userbet, name="mainpage"),
    path('livescore/', views.Userbet, name="livescore"),
    # path('add/', views.addbet, name='add'),
    

]