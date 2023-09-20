from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Photo, Category
from .serializers import PhotoSerializer

# Create your views here.


def getCategories():
    return Category.objects.all()

def index(request):

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    
    context={"categories": getCategories(),
             "photos": photos}
    
    return render(request, 'index.html', context=context)


def deleteCategory(request, id):
    print(request)
    category = Category.objects.get(pk=id)
    if not category: 
        print('Category does not exist')
    category.delete()
    return redirect('index')
    

@api_view(['GET'])
def getPhoto(request, id):
    photo = get_object_or_404(Photo, pk=id)
    context = {"photo": photo}
    return render(request,'view_photo.html', context=context)

@api_view(['GET', 'POST'])
def addPhoto(request, id=0):
    if request.method == 'GET':
        context = {
            "categories": getCategories(),
        }

      
        return render(request, 'add_photo.html', context)
    
    if request.method == 'POST':
        data = request.data
    
        # process request data
     
        category = data['select-category']

        if data['create-category'] != "":
            category = Category.objects.create(name=data['create-category'])
            category_key = category.pk
        
        seri_data = {
            'title': data['title'],
            'description': data['description'],
            'image_file': data['image_file'],
            'category': category_key
        }

        serializer = PhotoSerializer(data=seri_data)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        else: 
            data = {"message": "failed, invalid data."}
            return Response(status=400, data=data)
