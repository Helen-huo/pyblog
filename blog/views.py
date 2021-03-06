from django.shortcuts import render

def index(req):
    context = {}
    context['title'] = 'Index'
    context['message'] = 'Content from server'
    return render(req, 'index.html', context)

def signin(req):
    context = {}
    context['title'] = 'Sign In/Up'
    return render(req, 'signin.html', context)

def list_blogs(req):
    context = {}
    return render(req, 'list.html', context)