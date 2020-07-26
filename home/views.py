from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize




class HomePageView(TemplateView):
     template_name='home/home.html'

class ContactPageView(TemplateView):
     template_name='home/contact.html'

