from django.shortcuts import render
from django.http import HttpResponse
from Mission.models import Don_info

# Create your views here.
def index(request):
    return render(request,'Mission/index.html')

def users(request):
    user_list = Don_info.objects.order_by()
    user_dict = {'users': user_list}
    return render(request,'Mission/users.html',context= user_dict)
