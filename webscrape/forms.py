from django import forms
from .models import web

class PostForm(forms.ModelForm):
	class Meta:
		model = web
		fields = ('website',)
