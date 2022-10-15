from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NewsSerializers
from .models import News

# Create your views here.


@api_view(['GET'])
def index(request):
    task = News.objects.all()
    serializer = NewsSerializers(task, many=True)
    return Response(
        serializer.data
    )

