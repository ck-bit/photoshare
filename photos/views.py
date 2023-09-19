from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Photo, Category

# Create your views here.


def getCategories():
    return Category.objects.all()


def index(request):
   
    photos = Photo.objects.all()

    context={"categories": getCategories(),
             "photos": photos}
    
    print(photos[0].image_file)
    
    return render(request, 'index.html', context=context)

@api_view(['GET'])
def getPhoto(request, id):
    if request.method == 'GET':
        photo = Photo.objects.get(id=id)
        if not photo:
            return Response(status=404)
        context = {"photo": photo}
        return render(request,'view_photo.html', context=context)

@api_view(['GET', 'POST'])
def addPhoto(request, id=0):
    if request.method == 'GET':
        context = {
            "categories": getCategories(),
        }

        print(context)
        return render(request, 'add_photo.html', context)
    if request.method == 'POST':
        print(request.POST)
        print(request)
        print(request.FILES)
        return Response(status=200, data=request.POST)
