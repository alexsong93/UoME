from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from UoMeApp.models import UoMePost, Event, Group
from forms import UoMePostForm, CreateGroupForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.views.generic import ListView

# load homepage
def homepage(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html',c)

# load dashboard if user has logged in
def createDashboard(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', {'first_name': request.user.first_name})
    else:
        return HttpResponseRedirect('/')
 

def profile(request):
    return render_to_response('profile.html',{'user': request.user})

def getEvent(request, eventSlug, selected_page=1):
    posts = UoMePost.objects.all().order_by('pub_date')
    event_posts = []
    for post in posts:
        if post.event.filter(slug=eventSlug):
            event_posts.append(post)
 
    pages = Paginator(event_posts, 5)
    event = Event.objects.filter(slug=eventSlug)[0]
     
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
 
    # Display all the posts
    return render_to_response('events.html', { 'posts': returned_page.object_list, 'page': returned_page, 'event': event})


def createGroup(request):
    if request.POST:
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = CreateGroupForm()
 
    args = {}
    args.update(csrf(request))
     
    args['form'] = form
    return render_to_response('create_Group.html',args)


class myGroupsView(ListView):
    
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Group.objects.filter(members=request.user)
        return super(myGroupsView, self).dispatch(request, *args, **kwargs)

def create(request):
    if request.POST:
        form = UoMePostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = UoMePostForm()
 
    args = {}
    args.update(csrf(request))
     
    args['form'] = form
    return render_to_response('create_UoMePost.html',args)
        
        
        
        