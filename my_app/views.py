from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

articles = {
    "showbiz": "showbiz page",
    "politics": "politics page",
    "sports": "sports page",
    "crime": "crime page"
}


def articles_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 generic error") #404


def experiment_view(request,num1,num2):
    res = num1+num2
    return HttpResponse("The number is {}".format(str(res)))


# def index(request):
#     return HttpResponse("HELLO THIS IS A VIEW INSIDE MY APP")

def topic_view(request,num_page):
    li = list(articles.keys())
    topic = li[num_page]
    
    return HttpResponseRedirect(reverse("topic-view",args=[topic]))