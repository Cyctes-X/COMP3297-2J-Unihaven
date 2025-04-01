from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import UnihavenUser
from .serializers import UnihavenUserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/registration/register.html')

    def post(self, request):
        serializer = UnihavenUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return render(request, 'templates/registration/login.html')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
         
        if user is not None:

            if user.user_type == "STUDENT":

                messages.success(request, f'Welcome {user.username}! You are in the group: {user.user_type}')
                
                return redirect('hku_member') 
            
            elif user.user_type == "CEDARS":

                messages.success(request, f'Welcome {user.username}! You are in the group: {user.user_type}')
                
                return redirect('cedars') 

            elif  user.user_type == "OWNER":

                messages.success(request, f'Welcome {user.username}! You are in the group: {user.user_type}')
                
                return redirect('property_owner') 

        else:
            messages.error(request, f'message": "Invalid credentials')
            return redirect('login') 
        
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

@method_decorator(login_required, name='dispatch') #test only
class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/home.html')


#@method_decorator([login_required, group_required('HKU Member')], name='dispatch')  
class HKU_member_view(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/group/hku_member.html')  
  

#@method_decorator([login_required, group_required('CEDARS Specialist')], name='dispatch')
class Cedars_view(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/group/cedars.html')


#@method_decorator([login_required, group_required('Property Owner')], name='dispatch')
class Property_owner_view(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'templates/property_owner.html')
