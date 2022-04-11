from django.shortcuts import render, redirect, reverse
import requests
import random
from .models import Url, Personalized
# Create your views here.

def short():
    shortened_url=""
    text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(1,6):
        character=text[random.randint(0,61)]
        shortened_url+=character
    return shortened_url

def home(request):
    shortened_url=""
    domain=""
    x=""
    # api_key="e88947af68580455dfab253faa09cbff61dbf"
    if request.method=='POST':
        url=request.POST.get('url')
        if url!="":
            data=Url.objects.filter(long_url=url)
            store=Url()
            l=url.split("/")
            domain="anv3sh/"
            shortened_url=short()
            while Url.objects.filter(shortened_url=shortened_url):
                shortened_url=short()
            print(shortened_url)

            store.shortened_url=shortened_url
            store.long_url=url
            store.save()
    context={
        'domain':domain,
        'url':shortened_url,
        'data':x,

    }
    return render(request,'post/main.html',context)
    
def redirection(request,slug):
    urlss=Url.objects.get(shortened_url=slug)
    long_url=urlss.long_url

    
    return redirect(long_url)