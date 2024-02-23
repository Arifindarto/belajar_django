from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title': 'Landing Page',
        'subtitle': 'landing'
    }
    return render(request, "landing/index.html", context)