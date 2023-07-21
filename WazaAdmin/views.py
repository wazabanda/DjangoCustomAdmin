from django.shortcuts import render
from django.views.generic import View
from django.contrib import admin

# Create your views here.


class AdminStatsView(View):
    
    def get(self,request):
        return render(request,'WazaAdmin/stats.html')
    
    
class MessageAdminView(View):
    def get(self,request):
        return render(request,'WazaAdmin/messages.html')
    
