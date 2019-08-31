from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm

# def blog_post_detail_page(request,slug):
# 	# print(post_id.__class__)
# 	# try:
# 	# 	obj = BlogPost.objects.get(slug=slug)
# 	# except BlogPost.DoesNotExist:
# 	# 	raise Http404
# 	# except ValueError:
# 	# 	raise Http404
# 	# QuerySet = BlogPost.objects.filter(slug=slug)
# 	# if QuerySet.count() == 0:
# 	# 	raise Http404
# 	# obj = QuerySet.first()
# 	print("Django says",request.method,request.path,request.user)
# 	obj = get_object_or_404(BlogPost,slug=slug)
# 	template_name = "blog_post_detail.html"
# 	context = {"object":obj}
# 	return render(request,template_name,context)


#CRUD

# GET --> retrieval / List
# POST --> Create / Update / Delete 

def blog_post_list_view(request):
	# list out objects
	# could be search
	qs = BlogPost.objects.published() # queryset --> list of python objects
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct()

	template_name = "blog/list.html"
	context ={'object_list':qs}
	return render(request,template_name,context) 

@staff_member_required
def blog_post_create_view(request):
    # create objects
    # use a form 	
    form = BlogPostModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():
    	#obj = BlogPost.objects.create(**form.cleaned_data)
    	obj = form.save(commit=False)
    	obj.title = form.cleaned_data.get('title')
    	obj.user = request.user
    	obj.save()
    	# print(form.cleaned_data)
    	form = BlogPostModelForm()
    template_name = "form.html"
    context ={'form': form}
    return render(request,template_name,context) 

def blog_post_detail_view(request,slug):
	# 1 object --> detail view
    obj = get_object_or_404(BlogPost,slug=slug)
    template_name = "blog/detail.html"
    context = {"object":obj}
    return render(request,template_name,context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost,slug=slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
    	form.save()
    template_name = "form.html"
    context = {'form':form,"title":f"Update {obj.title}"}
    return render(request,template_name,context) 

@staff_member_required
def blog_post_delete_view(request,slug):
	
	obj = get_object_or_404(BlogPost,slug=slug)
	if request.method == 'POST':
		obj.delete()
		return redirect('/blog')
	template_name = "blog/delete.html"
	context = {"object":obj}
	return render(request,template_name,context) 


