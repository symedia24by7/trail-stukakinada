from django.shortcuts import render

# Create your views here.
def go(request):
    return render(request, 'go.html')