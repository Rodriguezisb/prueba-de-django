from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Post


# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
    model = Post
