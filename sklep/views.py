from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Product, ProductImage, Manufacturer, EffectType, Review, \
                    Cart, Order
from .forms import ProductForm, ProductEditForm, ProductImageForm

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

@login_required()
def new_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            if form.cleaned_data.get('type') != 'effect':
                product.bypass = None
                product.effect_type = None
                product.power_type = None
            product.save()
            if form.cleaned_data.get('product_image_1'):
                ProductImage.objects.create(product = product,
                        image=form.cleaned_data.get('product_image_1'))
            if form.cleaned_data.get('product_image_2'):
                ProductImage.objects.create(product = product,
                        image=form.cleaned_data.get('product_image_2'))
            if form.cleaned_data.get('product_image_3'):
                ProductImage.objects.create(product = product,
                        image=form.cleaned_data.get('product_image_3'))
            form.save_m2m()
            return redirect('sklep:home')
    else:
        form = ProductForm()
    return render(request, 'sklep/product_new.django-html', {'form': form})

# TODO: wyglad tego nie gotowy
# TODO: nie rozumiem, nie zwraca w kontekscie za luja danych z instance produktu
@login_required()
def edit_product_view(request, product_slug):
    initial_product = Product.objects.get(slug=product_slug)
    image_forms = []
    for img in initial_product.product_images.all():
        image_form = ProductImageForm(instance=img)
        image_forms.append(image_form)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES,
                                instance=initial_product)    
        if product_form.is_valid():
            product = product_form.save()
            # product.save()
            # product_form.save_m2m()
            # return redirect('sklep:home')
        
        for img in initial_product.product_images.all():
            image_form = ProductImageForm(request.POST, request.FILES, instance=img)
            if image_form.is_valid():
                product_image = image_form.save(commit=False)
                product_image.product = initial_product
                product_image.save()
                image_form.save_m2m()
            else: pass
        
            context = {"product_form": product_form,
                "product": initial_product,
                "ABSOLUTE_URL": 'http://127.0.0.1:8000/',
                'image_forms': image_forms
                }
            return render(request, 'sklep/product_edit.django-html', context)
    else:
        product_form = ProductEditForm(instance=initial_product)
        
    context = {"product_form": product_form,
               "product": initial_product,
               "ABSOLUTE_URL": 'http://127.0.0.1:8000/',
               'image_forms': image_forms
               }
    return render(request, 'sklep/product_edit.django-html', context)