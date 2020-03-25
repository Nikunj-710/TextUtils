# I have create this file - nikunj
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    info = {'name': 'Nikunj', 'place': 'INDIA'}
    return render(request, 'index.html', info)

def about(request):
    button = '''<a href="http://127.0.0.1:8000"> <button type="button">HOME</button> </a>
            <a href="http://127.0.0.1:8000"> <button type="button">Back</button> </a> <br/>'''
    return HttpResponse(button + "ABOUT NIKUNJ")

def file(request):
    b = r"C:\Users\Lenovo\PycharmProjects\DjangoCoursee\textutils\textutils\info.txt"
    f = open(b, "r")
    z = f.read()
    return HttpResponse(z)


def navigation(request):
    links = '''<a href="http://127.0.0.1:8000"> <button type="button">HOME</button> </a>
    <a href="http://127.0.0.1:8000"> <button type="button">Back</button> </a> <br/>
    <br/><a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> DJANGO PLAYLIST with Harry </a>
    <br/><a href="https://www.facebook.com"> <h3>FACEBOOK</h3></a>
    <br/><a href="https://www.hindustantimes.com/india-news/"> <h2>NEWS</h2> </a>
    <br/><a href="https://www.who.int"> <h1>WHO {GO CORONA}</h1> </a>
    '''
    return HttpResponse(links)


def analyser(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # list action on text
    puncremove = request.POST.get('puncremove', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    params = {}

    if (puncremove == "on"):
        punctuation_symbol = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation_symbol:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analysed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyser.html', params)

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLine', 'analysed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyser.html', params)

    if (uppercase == "on"):
        analyzed = ""
        analyzed = analyzed + djtext.upper()
        params = {'purpose': 'Convert UPPERCASE', 'analysed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyser.html', params)

    if (extraspace == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remove', 'analysed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyser.html', params)

    if (charcount == "on"):
        count = 0
        for char in djtext:
            if (char==" " or char=="\n" or char=="\r"):
                count = count + 1
        analyzed = djtext
        params = {'purpose': 'Count Character', 'analysed_text': analyzed, 'count_char': (len(djtext)-count)}
        #return render(request, 'analyser.html', params)

    if(puncremove!="on" and newlineremove!="on" and uppercase!="on" and extraspace!="on" and charcount!="on"):
        return HttpResponse("<h1>ERROR! Please Select Any Operation</h1>")

    return render(request,'analyser.html', params)

def contactus(requst):
    return HttpResponse("<h1>Contact US - 999999999</h1>")

def extraspaceremover(request):
    button = '''<a href="http://127.0.0.1:8000"> <button type="button">HOME</button> </a>
        <a href="http://127.0.0.1:8000"> <button type="button">Back</button> </a> <br/>'''
    return HttpResponse(button + "space Remover")

def puncremover(request):
    button = '''<a href="http://127.0.0.1:8000"> <button type="button">HOME</button> </a>
        <a href="http://127.0.0.1:8000"> <button type="button">Back</button> </a> <br/>'''
    return HttpResponse(button + "punc Remover")

def captfirst(request):
    button = '''<a href="http://127.0.0.1:8000"> <button type="button">HOME</button> </a>
        <a href="http://127.0.0.1:8000"> <button type="button">Back</button> </a> <br/>'''
    return HttpResponse(button + "Capital First")
