from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from bbs.models import UserProfile
from .forms import personalProfileSettingForm
from .forms import personalprofileSettingModelForm

class personalProfileDetail(DetailView):
    #model = get_object_or_404(UserProfile, pk = )
    #model = UserProfile
    template_name = 'personalProfile/personalProfile.html'
    context_object_name = 'userObject'

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super(personalProfileDetail, self).get_context_data(**kwargs)
        context['user'] = UserProfile
        return context


def personalProfileSetting(request, pk):
    userObject = get_object_or_404(UserProfile, pk = pk)
    if request.method == 'POST':
        form = personalProfileSettingForm(request.POST)
        if form.is_valid():
            userObject.name = form.cleaned_data['name']
            userObject.save()
            return HttpResponseRedirect(userObject.get_absolute_url())
    else:
        form = personalProfileSettingForm(initial={'name':userObject.name})
    return render(request, 'personalProfile/personalProfileSetting.html',
                  {'form':form, 'userObejct':userObject})

def personalProfileSettingMF(request, pk):
    userObject = get_object_or_404(UserProfile, pk = pk)
    baseUser = get_object_or_404(User,pk = userObject.user.pk)
    template_name = 'personalProfile/personalProfileSetting.html'
    if request.method == 'POST':
        #band the form with post data
        form = personalprofileSettingModelForm(request.POST, request.FILES)
        if form.is_valid():
            userObject.name = form.cleaned_data['name']
            baseUser.username = form.cleaned_data['name']
            userObject.signature = form.cleaned_data['signature']
            #userObject.photo = form.cleaned_data['photo']
            userObject.photo = request.FILES['photo']
            userObject.save()
            baseUser.save()
            #form.save()
            return HttpResponseRedirect(userObject.get_absolute_url())
    else:
        form = personalprofileSettingModelForm(initial={'name':userObject.name})
    return render(request, 'personalProfile/personalProfileSetting.html',
                  {'form':form, 'userObejct':userObject})