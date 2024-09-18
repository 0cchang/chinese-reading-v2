from rest_framework import serializers
from .models import SingleCharacterQuestion, omegaCharacter

class SCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleCharacterQuestion
        fields = '__all__'

class omegaSerializer():
    class Meta:
        model = omegaCharacter
        fields = '__all__'
