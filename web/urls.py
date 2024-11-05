from django.urls import path

from web import views

# app_name = 'conf'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('index/', views.home, name='index'),
    path('save_data/', views.save_data, name='save_data'),
    path('add_recepit/', views.add_recepit, name='add_recepit'),

]
