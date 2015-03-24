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
			post.data, post.email  = crawler(ul).split('starkpatel')
			post.save()
			return render(request, 'webscrape/post_detail.html', {'post': post})
	else:
		form = PostForm()
	return render(request, 'webscrape/post_new.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(web, pk=pk)
	return render(request, 'webscrape/post_detail.html', {'post': post})
            	
def crawler(addr):
        a = urlopen(addr)
        html = a.read()
        links = Set(findall(r'(http:.*?)"',html))
	html_data = " "
	email_data = " "
	linqs = ""        
	for link in links:
            	a_child = urlopen(link)
		linqs+= "".join(link)
            	html_child = a_child.read()
		email = findall(r'([a-z\._A-Z0-9]+@[a-z\._A-Z0-9]+)',html_child)
            	email_set = Set(email)
            	email_data = " ".join(email_set)
            	title = "".join(findall(r'<title.*?>[\n]?(.*?)</title>',html_child))
		content = "".join(findall(r'<meta name="[Dd][Ee][Ss].*?" content="(.*?)"',html_child))
            #print "\n"+link
            	html_data = '<a href="'+link+'"><h2>'+title+'</h2></a>'
            	html_data = html_data + content
            	html_data = html_data + '<h4 style="color:blue">'+link+'</h4><br/>'          
	html_data += 'starkpatel'+email_data+linqs	
	return html_data
