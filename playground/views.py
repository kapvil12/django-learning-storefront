from django.shortcuts import render

# Create your views here.
# request -> response / request handler (action but in django called as view)

from django.http import HttpResponse

def say_hello(request):
    # pull data from db, transform data, send email ..
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Ramailo Tech'})