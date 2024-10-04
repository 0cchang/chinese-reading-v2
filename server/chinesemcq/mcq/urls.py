from django.urls import path
from .views import getQuestion, getCharacterFromOmega, saveText, getSavedTexts, deleteSavedText

urlpatterns = [
    path('question/', getQuestion, name='getQuestion'),
    path('get-character/', getCharacterFromOmega, name="getCharacterFromOmega"),
    path('saveText/', saveText, name="saveText"),
    path('savedTexts/', getSavedTexts, name='getSavedTexts'),
    path('delete-savedtext/<int:text_id>/', deleteSavedText, name="deleteSavedText"),

]