from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title':'Auuuuuuuth',
        'subtitle': 'Auuu',
        'nav': [
            ['/','Home'],
            ['/blog', 'Blog'],
            ['/auth', 'Auth']
        ]
    }
    return render(request, "auth/index.html", context)