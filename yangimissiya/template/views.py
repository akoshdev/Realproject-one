from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request,'index.html',)

def reverse(request):
    user_text = request.GET['usertext']
    split_text = user_text.split()
    words = len(split_text)
    reversed_text = user_text[::-1]
    return render(request,'reverse.html',{'user':user_text,'reversedtext':reversed_text,'lenn':words})
    
    
    


