from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title': 'Go Blog',
        'subtitle': 'Blog'
    }
    return render(request, "blog/index.html", context)