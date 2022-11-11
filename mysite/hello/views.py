from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def myview(request):
    num_session = request.session.get('num_session', 0) + 1
    request.session['num_session'] = num_session
    if num_session > 4:
        del(request.session['num_session'])
    resp =  HttpResponse("view count" +'='+ str(num_session))
    resp.set_cookie('dj4e_cookie', 'dfa61ee5', max_age=1000)
    return resp