from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, BookSerializer, CategorySerializer
from django.http import HttpResponse, JsonResponse
from .models import Book, Category, Cuisine
# from pprint import pprint


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('published_year')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

# def some_view(request):
#     data = list(SomeModel.objects.values())
#     return JsonResponse(data, safe=False)

def get_books(request):
    books = list(Book.objects.values())
    print(books)
    return JsonResponse({'data': books})
    if request.method == 'GET':
        print('GET request')
    # pprint(dir(request))
    else:
        print('NOT A GET request')

    return HttpResponse('Books be workin\'')

def menu_items(request):
    menuItems = list(Book.objects.values())
    return JsonResponse(menuItems, safe=False)

def books_by_year(request, year):
    books = list(Book.objects.filter(published_year=year).values())
    print(books)
    if len(books) > 0:
        return JsonResponse({'data': books})
    else:
        return HttpResponse('Nope')

    return HttpResponse('You be at the year index.')

def books_by_title(request, letter):
    # print(letter)
    return HttpResponse(f'letter is {letter}')