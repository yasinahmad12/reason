from django.shortcuts import render

# Create your views here.
def index (req):
    return render (req,"base.html")

def home (request):
    return render( request= 'home.html')
