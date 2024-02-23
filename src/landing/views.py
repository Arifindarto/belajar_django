from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title': 'Landing Page',
        'subtitle': 'landing',
        'nav': [
            ['/','Home'],
            ['/blog', 'Blog'],
            ['/auth', 'Auth'],
        ],
        'banner': 'img/landing.png'
    }
    return render(request, "landing/index.html", context)