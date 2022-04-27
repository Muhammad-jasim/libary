from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .models import *
from rest_framework.views import *
from django.contrib.auth import authenticate,login,logout
from rest_framework.parsers import JSONParser 


# Create your views here.

@api_view(['GET'])
def home(request):
    url = {
        'Admin' : 'http://127.0.0.1:8000/log_or_reg',
        'Student' : 'http://127.0.0.1:8000/view_book'
    }
    return Response(url)

@api_view(['GET'])
def log_or_reg(request):
    url = {
        'Admin Login' : 'http://127.0.0.1:8000/login_page',
        'Admin Register' : 'http://127.0.0.1:8000/register_page'
    }
    return Response(url)

# Admin Registration
@api_view(['POST'])
def register_page(request):
    if request.method == 'POST':
        serializer = Admin_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    already ={'serializer':serializer.data,'Already have Account':'http://127.0.0.1:8000/login_page'}
    return Response(already)

# login page
@api_view(['POST'])
def login_page(request):
    if request.method == 'POST':
        try:
            Email = request.data['Email']   
            Password = request.data['Password'] 
            user = authenticate(request,Email=Email,Password=Password)
            if user is not None:
                login(request, user)
                return redirect('login_page')
            ad = Admin_Details.objects.get(Email=Email,Password=Password)   
            if ad:
                return redirect('admin_page')
            else:
                return Response('incorrect email or password')
        except:
            login={
                'Email':'Enter your Email id',
                'Password':'Enter your Password',
            }
            return Response(login)



@api_view(['GET'])
def admin_page(request):
    url = {
        'Admin' : 'http://127.0.0.1:8000/add_book',
        'Student' : 'http://127.0.0.1:8000/book_details'
    }
    return Response(url)
    
# Add registration
@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        serializer = Book_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
    serializers = Book_serializer()
    return Response(serializers.data)

# view book list
@api_view(['GET'])
def view_book(request):
    book = Book_Details.objects.all()
    serializer = Book_serializer(book,many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def book_details(request):
    content=[]
    book = Book_Details.objects.all()
    serializer = Book_serializer(book,many=True)
    for i in serializer.data:
        book_detail = {
            "id": i['id'],
            "Book_name": i['Book_name'],
            "Authors": i['Authors'],
            "Book_code": i['Book_code'],
            "Update": 'http://127.0.0.1:8000/update/'+str(i['id']),
            "Delete": 'http://127.0.0.1:8000/delete_book/'+str(i['id']),       
        }
        content.append(book_detail)
    return Response(content)   

# Delete book  
@api_view(['GET'])
def delete_book(request,id):
    book = Book_Details.objects.get(id=id)
    book.delete()
    return redirect('http://127.0.0.1:8000/book_details')


# update
@api_view(['POST'])
def update(request,id):
    if request.method == 'POST':
        book = Book_Details.objects.get(id=id)
        serializer = Book_serializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)                