from django.shortcuts import render,redirect,get_object_or_404
from .forms import registerForm,update_profile
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import post_form
from .models import blog_post,Category
# Create your views here
# registration_function
def register(request):
    if request.method=="POST":
        form=registerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('profile')
        else:
            messages.warning(request,'Something Went Wrong , Please Try Again')
            return redirect('register')
    form=registerForm()
    return render(request,'./author/registrationForm.html',{'form':form, 'type':"Registration"})

# login_function
def loginForm(request):
    if request.method=="POST":
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                messages.success(request,'Logged in Successfully')
                auth.login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Information Is Incorrect')
                return redirect('register')
            
        messages.warning(request,'Enter Your correct Username And Password')   
   
    form=AuthenticationForm()
    return render(request,'./author/registrationForm.html',{'form':form, 'type':'Login'})

# logOut function
def logout(request):
    auth.logout(request)
    messages.warning(request,'Logged Out Successfully')
    return redirect('home')

# profile_setUp
@login_required(login_url='/login/')
def profile(request):
    blog=blog_post.objects.filter(author=request.user)
    user=request.user
  
    return render(request,'author/profile.html',{'user':user,'blog':blog})

# profile_Update
@login_required(login_url='/login/')
def profileUpdate(request):
    
    if request.method=="POST":
        form=update_profile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect('profile')
        else:
            messages.warning(request," Please Try Again")
            return redirect('profile_update')
    form=update_profile(instance=request.user)
    return render(request,'author/registrationForm.html',{'form': form, 'type':'Profile Update'})

#change password
@login_required(login_url='/login/')
def change_password(request):
    if request.method=="POST":
         form=PasswordChangeForm(request.user,request.POST)
         if form.is_valid():
             form.save()
             auth.update_session_auth_hash(request,form.user)
             messages.success(request,"Password Updated Successfully")
             return redirect('profile')
         else:
             messages.warning(request," Please Try Again")
             return redirect('login')
    
    form=PasswordChangeForm(request.user)
    return render(request,'author/registrationForm.html',{'form': form, 'type':'Password Change'})

#add blog post
@login_required(login_url='/login/')
def new_blog(request):
    if request.method=="POST":
        form=post_form(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            messages.success(request,'New Post Added Successfully')
            return redirect('profile')
        else:
            messages.warning(request," Please Try Again")
            return redirect('new_blog')
    form=post_form()
    return render(request,'./author/blog_form.html',{'form':form,'type':'Create New'})

#delete Post
@login_required(login_url='/login/')
def delete_post(request,pk):
    post=get_object_or_404(blog_post,pk=pk)
    post.delete()
    return redirect('profile')

#edit post
@login_required(login_url='/login/')
def edit_post(request,pk):
    post=get_object_or_404(blog_post,pk=pk)
    edit_post=post_form(instance=post)
    if request.method=="POST":
        edit_post=post_form(request.POST,instance=post)
        if edit_post.is_valid():
            edit_post.save()
            messages.success(request,'New Post Added Successfully')
            return redirect('profile')
        else:
            messages.warning(request," Please Try Again")
            return redirect('edit_post')
    
    return render(request,'./author/blog_form.html',{'form':edit_post, 'type':'Edit'})

def all_blog(request):
    blog=blog_post.objects.all()
    category=Category.objects.all()
    return render(request,'./author/blog_page.html',{'posts':blog,'cat':category})