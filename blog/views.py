from django.shortcuts import render,redirect

from .models import Blog

from .forms import BlogCreationForm

# Create your views here.
def home(request):

    if 'user_email' in request.session: 
        blog_posts = Blog.objects.all()

        context = {"blog_posts": blog_posts}
        return render(request,"home.html",context)
    else:
        return redirect("login")
    


def add_new_blog_post(request):
    if request.method == "POST":
        blog_creation_form = BlogCreationForm(request.POST)
        
        if blog_creation_form.is_valid():
            blog_creation_form.save()
            return redirect('home')  
        else:
            print("Please fill required fields")
    else:    
        return render(request,"blog/create.html",{})
 