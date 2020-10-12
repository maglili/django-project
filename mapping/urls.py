from django.urls import path
from . import views

app_name = 'mapping'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('all/', views.mapping_list, name='all'),
    path('all/error/', views.page_error, name="error"),
]
