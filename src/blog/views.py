from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title': 'Go Blog',
        'subtitle': 'Blog',
        'nav': [
            ['/','Home'],
            ['/blog', 'Blog'],
            ['/auth', 'Auth']
        ]
    }
    return render(request, "blog/index.html", context)