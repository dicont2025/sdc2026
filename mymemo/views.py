from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main.html')

def create(request):
    content = request.GET['memoContent']
    return HttpResponse("메모 내용 = " + content)
