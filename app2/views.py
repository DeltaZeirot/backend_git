from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vistaDos(request):
    html= """
    
    <h1 style="color:blue">Hola mundo app2</h1>
    
    """

    return HttpResponse(html)
