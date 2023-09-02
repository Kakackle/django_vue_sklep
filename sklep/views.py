from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Index response")

# # @method_decorator(login_required, name='dispatch')
# class VueView(TemplateView):
#     template_name = 'index.django-html'

#     def get_context_data(self, **kwargs):
#         # przekazywanie danych do vue przez context
#         # if self.request.user.is_authenticated:
#         #     name = self.request.user.first_name
#         # else:
#         #     name = 'no user'
#         URLS = {
#             'api_product_list': reverse("api:api_product_list"),
#             'other': reverse("sklep:other")
#         }
#         return {
#             'user': self.request.user,
#             'URLS': URLS
#         }

def vue_view(request, path=''):
    URLS = {
            'base_path': 'http://127.0.0.1:8000',
            'login': reverse("accounts:login"),
            'logout': reverse("accounts:logout"),
            'signup': reverse("accounts:signup"),
            'user_edit': reverse("accounts:edit"),
            'api_product_list': reverse("api:api_product_list"),
            'other': reverse("sklep:other")
        }
    if request.user.is_authenticated:
        user = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'bio': request.user.profile.bio,
            'date_created': request.user.profile.date_created,
            'profile_image': request.user.profile.profile_image.url,
            'favourite_products': list(request.user.profile.favourite_products.all()),
        }
    else:
        user ={
            'is_authenticated': request.user.is_authenticated,
            'username': 'not logged in',
            'first_name': None,
            'last_name': None,
            'bio': None,
            'date_created': None,
            'profile_image': None,
            'favourite_products': None,
        }
    context={
        'user': user,
        'URLS': URLS       
    }
    return render(request, 'index.django-html', context)

@login_required()
def other_django_view(request):
    context = {
        "test": "yes it's me context",
        "user": request.user
    }
    return render(request, 'sklep/other.django-html', context)