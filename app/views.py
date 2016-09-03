from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from app.models import Gym, Image, CustomUser
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from app.forms import CustomUserLoginForm, CustomUserCreationForm
from app.forms import  CreateGym, EditGym
from django.contrib.auth.decorators import login_required

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

def video_of_the_day(request):
    context = {}
    return render(request, 'video_page.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def login_view(request):
    context = {}
    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        context['form']=form

        if form.is_valid():
            email = form.cleaned_data.get('email',None)
            password = form.cleaned_data.get('password',None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                message= """
                username or password incorrect, try again
                <a href='/login/'>login</a>
                """
                return HttpResponse(message)
            return redirect('/homepage/')
    return render(request,'login_view.html',context)

def logout_view(request):
    logout(request)

    return redirect('/homepage/')

def sign_up(request):
    context = {}
    context['form']= CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        context['form']=form

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email',None)
            password = form.cleaned_data.get('password1',None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                message= """
                username or password incorrect, try again
                <a href='/login/'>login</a>
                """
                return HttpResponse(message)

            return redirect('/homepage/')
    return render(request,'signup_view.html',context)

def delete_gym(request, pk):
    context= {}

    Gym.objects.get(pk=pk).delete()

    return redirect('/homepage/')

def edit_gym(request, pk):
    context= {}

    gym = Gym.objects.get(pk=pk)

    context ['gym']= gym

    form = EditGym(request.POST or None, request.FILES,instance=gym)

    context ['form']= form

    if form.is_valid():
        killme=form.save(commit=False)
        killme.owner = CustomUser.objects.get(id=request.user.id)
        killme = form.save()

        return redirect('/homepage/')
    else:
        print form.errors

    return render (request, 'edit_gym.html', context)


def create_gym(request):
    context = {}
    form = CreateGym(request.POST,request.FILES)
    context['form']=form

    if form.is_valid():
        killme=form.save(commit=False)
        killme.owner = CustomUser.objects.get(id=request.user.id)
        killme = form.save()

        return redirect('/homepage/')
    else:
        print form.errors
    return render(request, 'create_gym.html', context)


def list_all_gyms(request):
    context = {}
    gyms = Gym.objects.all()
    context['gyms'] = gyms

    return render(request, 'list_all_gyms.html', context)
def list_users_for_gym(request, pk):
    context = {}
    gym = Gym.objects.get(pk=pk)
    # context['users'] = gym.members_set.all()
    context['users'] = gym.members.all()

    return render(request, 'list_users_for_gym.html', context)
def gym_details(request, pk):
    context = {}
    gym= Gym.objects.get(pk=pk)
    context['gym'] = gym
    return render(request, 'gym_details.html', context)


def gym_register(request,pk):
    context = {}
    gym = Gym.objects.get(pk=pk)
    gym.members.add(CustomUser.objects.get(pk=request.user.id))

    return redirect('/list_all_gyms/')

def male_gyms(request):
    context = {}
    gyms = Gym.objects.filter(gender='M')
    context['gyms']= gyms

    return render(request, 'list_all_gyms.html', context)

def female_gyms(request):
    context = {}
    gyms = Gym.objects.filter(gender='F')
    context['gyms']= gyms

    return render(request, 'list_all_gyms.html', context)

def mixed_gyms(request):
    context = {}
    gyms = Gym.objects.filter(gender='Z')
    context['gyms']= gyms

    return render(request, 'list_all_gyms.html', context)


# def create_gym(request):
#     context = {}
#     form = CreateGym(request.POST, request.FILES)
#     context['form']=form

#     print "view retreived"
    
#     if request.method == 'POST':
#         if form.is_valid():
#             print "is valid"
#             data = form.save(commit=False)

#             data.owner = CustomUser.objects.get(id=request.user.id)
        
#             data.save()

#             images = request.POST.getlist('images')

#             images2 = request.POST.get('images')
#             # images = form.cleaned_data.get('images')

#             print "this is the list of images!! %s" % images
#             print "this is the second way to grab images %s" % images2 

#             for image in images:

#                 print type(image)

#                 new_image = Image.objects.create(file=images)

#                 print 'after image create'

#                 data.images.add(new_image)
            
#             print "data saved"

#             return redirect('/homepage/')
#         else:
#             print form.errors
#             return HttpResponse(form.errors)
#     return render(request, 'create_gym.html', context)