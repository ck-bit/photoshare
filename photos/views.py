from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Photo, Category

# Create your views here.


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def getPhoto(request, id):
    if request.method == 'GET':
        photo = Photo.objects.filter(id=id)
        if not photo:
            return Response(status=404)
        return Response(status=200, data=photo)
     