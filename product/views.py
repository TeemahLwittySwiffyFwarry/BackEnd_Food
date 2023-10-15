from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import food
from rest_framework import serializers

# Create your views here.
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'

@api_view(['GET'])
def fetchallfood(request):
    allfood = food.objects.all()
    serializer = FoodSerializer(allfood, many=True)
    print(allfood)
    #return Response(allfood)
    return Response(serializer.data)

@api_view(['POST'])
def createfood(request):
    print(request.data)
    return Response('The title is')