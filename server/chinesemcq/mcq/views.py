from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SingleCharacterQuestion, omegaCharacter
from .serializer import SCQSerializer

@api_view(['GET'])
def getQuestion(request):
    question_data = SingleCharacterQuestion.objects.all()
    serializedData = SCQSerializer(question_data, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def getCharacterFromOmega(request):
    id = request.query_params.get('id')  # Use query_params with REST framework
    if id is not None and id.isdigit():
        character_id = int(id)
        try:
            character_obj = omegaCharacter.objects.get(unique_id=character_id)
            return Response({'character': character_obj.character}, status=status.HTTP_200_OK)
        except omegaCharacter.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
