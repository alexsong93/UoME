from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    user = auth.authenticate(username=username, password=password,first_name=first_name,last_name=last_name)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/')
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render_to_response('register.html', args)
        
        
        
        
