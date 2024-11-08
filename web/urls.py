from django.urls import path

from . import views

app_name = 'conf'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('index/', views.home, name='index'),
    path('receipt_list/', views.receipt_list, name='receipt_list'),

    path('', views.save_sample_data, name='save_sample_data'),
    path('success/', views.success_page, name='success_page'),
    path('upload/', views.upload_file_view, name='upload_file'),
]
