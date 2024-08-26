from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def qulification(request):
    return render(request, 'qulification.html')
def experince(request):
    return render(request, 'experince.html')