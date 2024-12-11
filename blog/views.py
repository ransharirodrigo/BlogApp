from django.shortcuts import render,redirect

from .models import Blog

from .forms import BlogCreationForm

from users.models import CustomUser

# Create your views here.
def home(request):

    if 'user_email' in request.session: 
        user_email = request.session.get('user_email') 
        blog_posts = Blog.objects.filter(user__email=user_email)

        context = {"blog_posts": blog_posts}
        return render(request,"home.html",context)
    else:
        return redirect("login")
    


def add_new_blog_post(request):
    if request.method == "POST":
        blog_creation_form = BlogCreationForm(request.POST)
        
        if blog_creation_form.is_valid():
            user_email = request.session.get('user_email')
            user = CustomUser.objects.filter(email=user_email).first()

            blog =  blog_creation_form.save(commit=False)
            blog.user = user
            blog.save()

            return redirect('home')  
        else:
            print("Please fill required fields")
    else:    
        return render(request,"blog/create.html",{})
 