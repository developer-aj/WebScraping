from django.shortcuts import render, get_object_or_404, redirect
from .models import web
from .forms import PostForm
from urllib import *
from re import *
from sets import Set
# Create your views here.

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			ul = "http://"+post.website
			post.links, post.email  = crawler(ul)
			post.save()
			return render(request, 'webscrape/post_detail.html', {'post': post})
	else:
		form = PostForm()
	return render(request, 'webscrape/post_new.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(web, pk=pk)
	return render(request, 'webscrape/post_detail.html', {'post': post})
            	
def crawler(addr):
        html = urlopen(addr).read()
        links = Set(findall(r'(http://[a-z0-9A-Z].*?)"',html))
	links = links.union(Set(findall(r'(https://[a-z0-9A-Z].*?)"',html)))
	emails = Set(findall(r'([a-z\._A-Z0-9]+@[a-z\._A-Z0-9]+)',html))
	links_list = links
	links_data = ''
	email_data = ''    
	for link in links:
            	html_child = urlopen(link).read()
            	emails = emails.union(Set(findall(r'([a-z\._A-Z0-9]+@[a-z\._A-Z0-9]+)',html_child)))
            	email_data = '\n'.join(emails)
            	links_list = links_list.union(Set(findall(r'(http://[a-z0-9A-Z].*?)"',html_child)))
		links_list = links_list.union(Set(findall(r'(https://[a-z0-9A-Z].*?)"',html_child)))
		links_data = '\n'.join(links_list)
	return [links_data, email_data]
