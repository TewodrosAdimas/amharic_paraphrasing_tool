from django.urls import path
from .views import translate_paraphrase

urlpatterns = [
    path('', translate_paraphrase, name='translate'),
]
