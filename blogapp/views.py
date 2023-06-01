from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')    


def home(request):
    return render(request,'home.html')   

def blogview(request):
    return render(request, 'blogview.html')     

def about(request):
    return render(request,'about.html')    

def contact(request):
    return render(request,'contact.html')    

def newpost(request):
    return render(request,'newpost.html')    

def editpost(request):
    return render(request,'edit.html')        
