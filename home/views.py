from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    peoples = [
        {"name": "shahriar", "age": 23},
        {"name": "arif", "age": 17},
        {"name": "soruv", "age": 27},
        {"name": "fahim", "age": 14},
        {"name": "akib", "age": 30},
    ]
    vagetables=['Pumpkin','Tomato','Potato']
    return render(request, "home/index.html", context={"peoples": peoples, 'vagetables': vagetables})

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html")

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a succes page</h1>")
