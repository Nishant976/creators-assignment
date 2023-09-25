from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from .models import Image
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class CreatePostView(CreateView):
   template_name="accounts/post.html"
   model=Image
   fields="__all__"
   success_url=reverse_lazy("login")


    
