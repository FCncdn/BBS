from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.urls import reverse
from bbs.models import UserProfile
from bbs.models import Article
from .forms import personalProfileSettingForm
from .forms import detailSettingModelForm
from .forms import basicSettingModelForm
from .forms import MySearchForm
from .models import FollowShip
from .models import BlackList
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

class personalProfileDetail(DetailView):
    #model = get_object_or_404(UserProfile, pk = )
    #model = UserProfile
    template_name = 'personalProfile/personalProfile.html'
    context_object_name = 'userFront'

    def get_queryset(self):
        #return UserProfile.objects.filter(pk=self.kwargs['pk'])
        return User.objects.filter(pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super(personalProfileDetail, self).get_context_data(**kwargs)
        is_follow = FollowShip.objects.filter(follower__user__pk=self.request.user.pk)
        is_follow = is_follow.filter(followed__user__pk=self.kwargs['pk'])
        is_black = BlackList.objects.filter(currentUser__user__pk=self.request.user.pk)
        is_black = is_black.filter(blacker__user__pk=self.kwargs['pk'])
        context['numFollower'] = FollowShip.objects.filter(follower__user__pk=self.kwargs['pk']).count()
        context['numFollowed'] = FollowShip.objects.filter(followed__user__pk=self.kwargs['pk']).count()
        context['numPost'] = Article.objects.filter(author__pk=self.kwargs['pk']).count()
        context['articles'] = Article.objects.filter(author__pk=self.kwargs['pk'])
        context['is_follow'] = is_follow
        context['is_black'] = is_black
        return context

def personalProfileDynamic(request, pk):
    return render(request, 'personalProfile/personalProfileDynamic.html',{})

def personalProfileFavourite(request, pk):
    return render(request, 'personalProfile/personalProfileFavourite.html',{})


class MySearchView(SearchView):
    template_name = 'personalProfile/test.html'
    form_class = MySearchForm

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset

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
    #baseUser = get_object_or_404(User,pk = userObject.user.pk)
    template_name = 'personalProfile/personalProfileSetting.html'
    if request.method == 'POST':
        #band the form with post data
        form = detailSettingModelForm(request.POST, request.FILES)
        if form.is_valid():
            #userObject.name = form.cleaned_data['username']
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            #baseUser.username = form.cleaned_data['username']
            #userObject.signature = form.cleaned_data['signature']
            userObject.phoneNum = form.cleaned_data['phoneNum']
            userObject.receive_dynamic = form.cleaned_data['receive_dynamic']
            userObject.receive_email = form.cleaned_data['receive_email']
            if request.FILES.get('headImage',''):
                userObject.headImage = request.FILES['headImage']
            userObject.save()
            #baseUser.save()
            request.user.save()
            print("***personalProfileSettingMF::form valid done")
            return HttpResponseRedirect(userObject.get_absolute_url())
    else:
        form = detailSettingModelForm(initial={
            'username':request.user.username,
            'email':request.user.email,
            'phoneNum':userObject.phoneNum,
            'receive_dynamic':userObject.receive_dynamic,
            'receive_email':userObject.receive_email,
            })
    return render(request, 'personalProfile/personalProfileSetting.html',
                  {'form':form, 'userObejct':userObject})


def personalProfileBasicSetting(request, pk):
    userObject = get_object_or_404(UserProfile, pk = request.user.profile.pk)
    template_name = 'personalProfile/personalProfileBasicSetting.html'
    if request.method == 'POST':
        #band the form with post data
        form = basicSettingModelForm(request.POST, request.FILES)
        if form.is_valid():
            userObject.gender = form.cleaned_data['gender']
            userObject.resume = form.cleaned_data['resume']
            userObject.website = form.cleaned_data['website']
            userObject.save()
            print("***personalProfileBasicSetting::form valid done")
            return HttpResponseRedirect(userObject.get_absolute_url())
    else:
        form = basicSettingModelForm(initial={
            'gender':userObject.gender,
            'resume':userObject.resume,
            'website':userObject.website,
            })
    return render(request, 'personalProfile/personalProfileBasicSetting.html',
                  {'form':form, 'userObejct':userObject})

def personalProfileDetailSetting(request, pk):
    userObject = get_object_or_404(UserProfile, pk = request.user.profile.pk)
    #baseUser = get_object_or_404(User,pk = userObject.user.pk)
    template_name = 'personalProfile/personalProfileDetailSetting.html'
    if request.method == 'POST':
        #band the form with post data
        form = detailSettingModelForm(request.POST, request.FILES)
        if form.is_valid():
            #userObject.name = form.cleaned_data['username']
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            #baseUser.username = form.cleaned_data['username']
            #userObject.signature = form.cleaned_data['signature']
            userObject.phoneNum = form.cleaned_data['phoneNum']
            userObject.receive_dynamic = form.cleaned_data['receive_dynamic']
            userObject.receive_email = form.cleaned_data['receive_email']
            if request.FILES.get('headImage',''):
                userObject.headImage = request.FILES['headImage']
            userObject.save()
            #baseUser.save()
            request.user.save()
            print("***personalProfileDetailSetting::form valid done")
            return HttpResponseRedirect(userObject.get_absolute_url())
    else:
        form = detailSettingModelForm(initial={
            'username':request.user.username,
            'email':request.user.email,
            'phoneNum':userObject.phoneNum,
            'receive_dynamic':userObject.receive_dynamic,
            'receive_email':userObject.receive_email,
            })
    return render(request, 'personalProfile/personalProfileDetailSetting.html',
                  {'form':form, 'userObejct':userObject})

def personalProfileBackList(request, pk):
    return render(request, 'personalProfile/personalProfileBackListSetting.html',{})

def personalProfileReward(request, pk):
    return render(request, 'personalProfile/personalProfileRewardSetting.html',{})

def personalProfileRedirectFollow(request, pk):
    is_follow = FollowShip.objects.filter(follower__user__pk=request.user.pk)
    is_follow = is_follow.filter(followed__user__pk=pk)
    currentUser = UserProfile.objects.get(user__pk=pk)
    if is_follow:
        is_follow.delete()
        print('***personalProfileRdfirectFollow')
        print('delete model success')
    else:
        m_follow = FollowShip(follower=request.user.profile, followed=currentUser)
        m_follow.save()
        print('***personalProfileRdfirectFollow')
        print('create model success')
    return HttpResponseRedirect(reverse('personalProfile:personalProfileMain', kwargs={'pk':pk}))

def personalProfileRedirectBlackList(request, pk):
    is_black = BlackList.objects.filter(currentUser__user__pk=request.user.pk)
    is_black = is_black.filter(blacker__user__pk=pk)
    currentUser = UserProfile.objects.get(user__pk=pk)
    if is_black:
        is_black.delete()
    else:
        m_balckList = BlackList(currentUser=request.user.profile, blacker=currentUser)
    return HttpResponseRedirect(reverse('personalProfile:personalProfileMain', kwargs={'pk':pk}))