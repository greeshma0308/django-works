from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
# def Home(request):
#
#     if(request.method=="GET"):
#
#         return HttpResponse("Welcome to Django")
#
# # define index view returns message "Index Page"
#
# def Index(request):
#
#     if(request.method=="GET"):
#
#         return HttpResponse("Index")


#CLASS BASED
class Home(View):

    def get(self,request):

        return HttpResponse("Welcome to Django")

# define index view returns message "Index Page"

class Index(View):

    def get(self,request):

        return HttpResponse("Index")
