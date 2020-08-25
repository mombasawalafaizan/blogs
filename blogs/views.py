from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """The home page for Blog Post"""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all blogs."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
	"""Show a single Blog Post"""
	post = BlogPost.objects.get(id=post_id)
	context = {'post': post}
	return render(request, 'blogs/post.html', context)

@login_required
def add_post(request):
	"""Add a new post"""
	if request.method != 'POST':
		#No data submitted; create a blank form.
		form = BlogForm()
	else:
		#POST data submitted; process data.
		form = BlogForm(request.POST)
		if form.is_valid():
			post_user = form.save(commit=False)
			post_user.owner = request.user
			post_user.save()
			return HttpResponseRedirect(reverse('blogs:posts'))

	context = {'form': form}
	return render(request, 'blogs/add_post.html', context)

@login_required
def edit_post(request, post_id):
	"""Edit a post"""
	post = BlogPost.objects.get(id=post_id)

	#Make sure the post belongs to the current user
	if post.owner != request.user:
		raise Http404
	if request.method != 'POST':
		# Initial request; pre-fill the form with the current post.
		form = BlogForm(instance = post)
	else:
		#POST data submitted; process data
		form = BlogForm(instance = post, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))
	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)