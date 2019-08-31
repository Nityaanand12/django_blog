from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
	my_title = "Hello There...."
	qs = BlogPost.objects.all()[:5]
	context = {'title':"Welcome to try django","blog_list":qs}
	# template_name = "title.txt"
	# template_obj = get_template(template_name)
	# rendered_string = template_obj.render(context)
	#django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
	return render(request,"home.html",context)

def about_page(request):
	#return HttpResponse("<h1>About Us</h1>")
	return render(request,"about.html",{'title':'About Us'})

def contact_page(request):
	#return HttpResponse("<h1>Contact Us</h1>")
    form = ContactForm(request.POST or None)
    if form.is_valid():
    	print(form.cleaned_data)
    	form = ContactForm()
    context = {
    'title':"Contact Us",
    "form":form
    }
    return render(request,"form.html",context)

def example_page(request):
	context = {'title':'Example'}
	template_name = "helloworld.html"
	template_obj = get_template(template_name)
	rendered_obj = template_obj.render(context)
	return HttpResponse(rendered_obj)
	#return render(request,"contact.html",{'title':'Contact Us'})