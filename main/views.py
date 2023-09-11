from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'instrument': 'Guitar',
        'brand': 'Fender',
        'type': 'Telecaster',
        'amount': '2',
        'description': 'In good conditions'
    }

    return render(request, "main.html", context)