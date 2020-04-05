from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'title':'Password Generator'})

def password(request):

    #characters = list('abcdefghijklmnopqrstuvwxyz')
    characters = list('')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list("~!@#$%^&*()_-+={;?><.,}[]/|':'"))

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

