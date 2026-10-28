from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("서디콘 안녕")

def create(request):
    content = request.GET['memoContent']
    return HttpResponse("메모 내용 = " + content)