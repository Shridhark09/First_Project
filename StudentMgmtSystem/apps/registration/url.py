from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('store/', views.store, name='store'),
    path('delete/<int:pk>', views.deleteStudent, name="deleteStudent"),
    path('updateView/<int:pk>', views.updateView, name='updateView'),
    path('update/<int:pk>', views.update, name='update')

    # path('home',views.home())

]
