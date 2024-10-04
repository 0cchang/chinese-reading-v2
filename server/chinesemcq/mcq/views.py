from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SingleCharacterQuestion, omegaCharacter, SavedText
from .serializer import SCQSerializer

@api_view(['GET'])
def getQuestion(request):
    question_data = SingleCharacterQuestion.objects.all()
    serializedData = SCQSerializer(question_data, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def getCharacterFromOmega(request):
    id = request.query_params.get('id')  # Use query_params with REST framework
    print(id)
    if id is not None and id.isdigit():
        character_id = int(id)
        try:
            character_obj = omegaCharacter.objects.get(unique_id=character_id)
            print(character_obj.character)
            return Response({'character': character_obj.character}, status=status.HTTP_200_OK)
        except omegaCharacter.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def saveText(request):
    text = request.data.get('text')
    if text:
        # Create a new SavedText object
        new_text = SavedText(text=text)
        new_text.save()
        return Response({'message': 'Text saved successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSavedTexts(request):
    saved_texts = SavedText.objects.all()
    texts_data = [{'id': text.id, 'text': text.text[:20]} for text in saved_texts]  # Preview text
    return Response(texts_data)

@api_view(['DELETE'])
def deleteSavedText(request, text_id):
    try:
        saved_text = SavedText.objects.get(id=text_id)
        saved_text.delete()
        return Response({'message': 'Saved text deleted successfully'}, status=status.HTTP_200_OK)
    except SavedText.DoesNotExist:
        return Response({'error': 'Saved text not found'}, status=status.HTTP_404_NOT_FOUND)