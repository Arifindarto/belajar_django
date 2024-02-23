from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        'title':'Auuuuuuuth',
        'subtitle': 'Auuu'
    }
    return render(request, "auth/index.html", context)