# urls.py
from django.urls import path
from . import views

app_name = 'paraphrase'  # Define the namespace for the paraphrase app

urlpatterns = [
    path('', views.translate_paraphrase, name='translate'),  # The main translation view
]
