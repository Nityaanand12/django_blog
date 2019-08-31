from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title','image','slug','content','publish_date']

	# def clean_title(self,*args,**kwargs):
	# 	title = self.cleaned_data.get('title')
	# 	qs = BlogPost.objects.filter(title=title)
	# 	if qs.exists():
	# 		raise forms.ValidationError("this is title exists already")
	# 	return title