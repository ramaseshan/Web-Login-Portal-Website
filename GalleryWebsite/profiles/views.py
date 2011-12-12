from GalleryWebsite.profiles.forms import *
from GalleryWebsite.profiles.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import list_detail

@login_required
def profile_list(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(login(request))
    else:
        return list_detail.object_list(
        request,
        queryset = Profile.objects.all(),
        paginate_by = 20,)
    
profile_list.__doc__ = list_detail.object_list.__doc__

@login_required
def profile_create(request):
    
     if request.user.is_authenticated():   
        profile=Profile(user_id=request.user.id)
        profile.save()
        return HttpResponseRedirect('/profile/edit/')


@login_required         
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/profile/create/')
          
    if profile:
        context = { 'object':profile }
        return render_to_response('profiles/profile_detail.html', context, context_instance=RequestContext(request))
  
        


@login_required
def profile_edit(request, template_name='profiles/profile_form.html'):
    
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/profile/')

    if request.POST:
        
        profile = Profile.objects.get(user=request.user)
                
        if profile:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            user_form = UserForm(request.POST, instance=request.user)
               

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return HttpResponseRedirect('/profile/') 
       
        
        else:
            context = {
                'profile_form': profile_form, 
                'user_form': user_form,
            }
    else:
        profile = Profile.objects.get(user=request.user)
        context = {
            'profile_form': ProfileForm(instance=profile), 
            'user_form': UserForm(instance=request.user),
        
        }
    return render_to_response(template_name, context, context_instance=RequestContext(request))
