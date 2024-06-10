from django.urls import path
from . import views

app_name = 'csv_analysis'

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('analyse/<int:pk>', views.analyse_csv, name='analyse_csv'),
]
