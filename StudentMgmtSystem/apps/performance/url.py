from django.urls import path
from..registration.models import Student
from . import views

urlpatterns=[
    path('', views.reports, name="reports"),
    path('addScore', views.addScore, name="addScore"),
    path('saveScore',views.saveScore,name="saveScore"),
    path('updateScore/<int:pk>', views.updateScore, name="updateScore"),
    path('saveUpdatedScore/<int:pk>', views.saveUpdatedScore, name="saveUpdatedScore"),

]