from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    params={
        "title":"アンケート",
        "msg":"あなたはなぜこのホテルに来ようと思ったのですか?",
        "goto":"next"
    }
    return render(request,"hello/index.html",params)
def next(request):
    params={
        "title":"hello/next",
        "msg":"このホテルのよかったことは?",
        "goto":"index",
    }
    return render(request,"hello/index.html",params)