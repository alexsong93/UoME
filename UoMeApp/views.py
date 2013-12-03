from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from UoMeApp.models import UoMePost, Event
from forms import UoMePostForm, CreateGroupForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse

 
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


def create(request):
    if request.POST:
        form = UoMePostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/UoMePosts/')
    else:
        form = UoMePostForm()
 
    args = {}
    args.update(csrf(request))
     
    args['form'] = form
    return render_to_response('create_UoMePost.html',args)
        
        
        
        