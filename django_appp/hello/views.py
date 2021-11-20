from typing_extensions import ParamSpec
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    params={
        "title":"アンケート",
        "msg":"あなたはなぜこのホテルに来ようと思ったのですか?"
    }
    return render(request, "hello/index.html",params)
def next(request):
    params={
        "title":"hello/next",
        "msg":"このホテルのよかったことは?"
    }