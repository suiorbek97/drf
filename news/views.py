from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NewsSerializers
from .models import News
from django.core.exceptions import ObjectDoesNotExist


# @api_view(['GET', 'PUT', 'DELETE'])
# def index(request, id):
#     try:
#         news = News.objects.get(id=id)
#     except News.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = NewsSerializers(news)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = NewsSerializers(news, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Object": "Object is updated"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         news.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# def index(request):
#     if request.method == "GET":
#         news = News.objects.all()
#         serializer = NewsSerializers(news, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = NewsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Object is created !"})
#         return Response(serializer.errors)


@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        task = News.objects.all()
        serializer = NewsSerializers(task, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NewsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"object": "Object is created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_object_view(request, id=id):
    news = News.objects.get(id=id)
    news.delete()

    return Response({"Object": "Object is deleted"})
