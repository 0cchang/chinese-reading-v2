from django.urls import path
from .views import getQuestion, getCharacterFromOmega

urlpatterns = [
    path('question/', getQuestion, name='getQuestion'),
    path('get-character/', getCharacterFromOmega, name="getCharacterFromOmega"),
]