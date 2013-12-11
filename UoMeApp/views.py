from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from UoMeApp.models import UoMePost, Group, Notification
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
def loadDashboard(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', {'user': request.user })
    else:
        return HttpResponseRedirect('/')
 

def profile(request):
    return render_to_response('profile.html',{'user': request.user})


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

def addUoMePost(request, group_id):
    if request.POST:
        form = UoMePostForm(request.POST, user=request.user, group_id=group_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = UoMePostForm(user=request.user, group_id=group_id)
 
    args = {}
    args.update(csrf(request))
    args['group_id'] = group_id
    args['form'] = form
    return render_to_response('create_UoMePost.html',args)

def editUoMePost(request, group_id, uomepost_id):
    if request.POST:
        form = UoMePostForm(request.POST, user=request.user, group_id=group_id)
        if form.is_valid():
            uomepost = UoMePost.objects.get(id=uomepost_id) 
            form = UoMePostForm(request.POST, instance=uomepost, user=request.user, group_id=group_id)
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        uomepost = UoMePost.objects.get(id=uomepost_id) 
        form = UoMePostForm(instance=uomepost, user=request.user, group_id=group_id)
 
    args = {}
    args.update(csrf(request))
    args['group_id'] = group_id
    args['uomepost_id'] = uomepost_id
    args['form'] = form
    return render_to_response('edit_UoMePost.html',args)

def notifyPaid(request, uomepost_id):
    uomepost = UoMePost.objects.get(id=uomepost_id)
    if request.user == uomepost.ower_name:
        receiver = uomepost.receiver_name
        Notification.objects.create(user=receiver,
                                    title=request.user.first_name + ' has paid you back for ' + uomepost.item_name,
                                    message=request.user.first_name + ' ' + request.user.last_name +
                                            ' has stated the he/she has paid you back for ' +
                                             uomepost.item_name + '. Confirm or reject by going to your groups.',
                                    alertNotif=False)
        setattr(uomepost, 'paid', True)
        uomepost.save()
        return HttpResponseRedirect('/groups/')
    else:
        return HttpResponseRedirect('/profile/')
        
def notifyConfirm(request, uomepost_id):
    uomepost = UoMePost.objects.get(id=uomepost_id)    
    uomepost.delete()
    receiver = uomepost.ower_name
    Notification.objects.create(user=receiver,
                                    title='Payment confirmation for ' + uomepost.item_name, 
                                    message=uomepost.receiver_name.first_name + ' ' + uomepost.receiver_name.last_name +
                                            ' has confirmed your payment for ' + uomepost.item_name + ".",
                                    alertNotif=False)
    return HttpResponseRedirect('/groups/')
        
def notifyReject(request, uomepost_id):
    uomepost = UoMePost.objects.get(id=uomepost_id)
    receiver = uomepost.ower_name
    setattr(uomepost, 'paid', False)
    uomepost.save()
    Notification.objects.create(user=receiver,
                                    title='Payment rejected for ' + uomepost.item_name, 
                                    message=uomepost.receiver_name.first_name + ' ' + uomepost.receiver_name.last_name +
                                            ' has rejected your payment for ' + uomepost.item_name + "." +
                                            ' Did you really pay him/her back?',
                                    alertNotif=True)
    return HttpResponseRedirect('/groups/')
    