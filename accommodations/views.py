from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import UnihavenUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/accommodation/Acc_Home.html')

class Detail(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/accommodation/Acc_Detail.html')
    
class Favorite(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/accommodation/Acc_Favorite.html')
    
class Contact(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/accommodation/Acc_Contact.html')
    
class ListAll(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/accommodation/Acc_ListAll.html')
