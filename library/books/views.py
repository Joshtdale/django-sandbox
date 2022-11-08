from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book
from pprint import pprint

def some_view(request):
    data = list(SomeModel.objects.values())
    return JsonResponse(data, safe=False)

def get_books(request):
    books = list(Book.objects.values())
    print(books)
    return JsonResponse({'data': books})
    # if request.method == 'GET':
    #     print('GET request')
    # # pprint(dir(request))
    # else:
    #     print('NOT A GET request')

    # return HttpResponse('Books be workin\'')

def books_by_year(request, year):
    books = list(Book.objects.filter(published_year=year).values())
    print(books)
    if len(books) > 0:
        return JsonResponse({'data': books})
    else:
        return HttpResponse('Nope')

    # return HttpResponse('You be at the year index.')

def books_by_title(request, letter):
    # print(letter)
    return HttpResponse(f'letter is {letter}')