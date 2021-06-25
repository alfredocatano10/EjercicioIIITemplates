from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Puesto, Producto, Reserva

# Create your views here.
#---------------------------------------------------------------
#---------------------------------------------------------------

class HomePageView(ListView):
	model = Puesto
	template_name = 'home.html'

class PostPageView(ListView):
	model = Puesto
	template_name = 'post.html'
	context_object_name = 'post_list'

