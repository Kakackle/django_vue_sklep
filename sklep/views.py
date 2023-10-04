from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Product, ProductImage, Manufacturer, EffectType, Review, \
                    Cart, Order, Shipping
from .forms import ProductForm, ProductEditForm, ProductImageForm

from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# for stripe
from django.views import View
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY

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
            # 'checkout': reverse("backend:checkout"),
            # 'product_create': reverse()            
        }
    if request.user.is_authenticated:
        URLS['profile_edit'] = reverse("users:user", kwargs={'slug':request.user.username})
        user = {
            'is_authenticated': request.user.is_authenticated,
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'bio': request.user.profile.bio,
            'date_created': request.user.profile.date_created,
            'profile_image': request.user.profile.profile_image.url,
            'favourite_products': list(request.user.profile.favourite_products.values_list('name', flat=True)),
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

@login_required()
def edit_product_view(request, product_slug):
    initial_product = Product.objects.get(slug=product_slug)
    image_forms = []
    
    if request.user != initial_product.owner:
        raise PermissionDenied
        return redirect('sklep:home')

    # jesli POST, uzupelnij formy danymi
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
            image_forms.append(image_form)
            if image_form.is_valid():
                product_image = image_form.save(commit=False)
                product_image.product = initial_product
                product_image.save()
                image_form.save_m2m()
            else: continue

    else:
        product_form = ProductEditForm(instance=initial_product)
        # dla zwracania - formy na obrazki - GET
        for img in initial_product.product_images.all():
            image_form = ProductImageForm(instance=img)
            image_forms.append(image_form)

    context = {"product_form": product_form,
               "product": initial_product,
               "ABSOLUTE_URL": 'http://127.0.0.1:8000/',
               'image_forms': image_forms
               }
    return render(request, 'sklep/product_edit.django-html', context)

@login_required()
def delete_image_view(request, product_slug, image_slug):
    print(image_slug)
    initial_product = Product.objects.get(slug=product_slug)
    image_forms = []

    if request.user != initial_product.owner:
        raise PermissionDenied

    if request.POST:
        image = ProductImage.objects.get(slug=image_slug)
        image.delete()

        for img in initial_product.product_images.all():
            image_form = ProductImageForm(request.POST, request.FILES, instance=img)
            image_forms.append(image_form)

        product_form = ProductEditForm(request.POST, request.FILES, instance=initial_product)

    else:
        for img in initial_product.product_images.all():
            image_form = ProductImageForm(instance=img)
            image_forms.append(image_form)
        product_form = ProductEditForm(instance=initial_product)

    context = {
        "product_form": product_form,
        "product": initial_product,
        "ABSOLUTE_URL": 'http://127.0.0.1:8000/',
        'image_forms': image_forms
        }
    return render(request, 'sklep/product_edit.django-html', context)

@login_required()
def delete_product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.user != product.owner:
        raise PermissionDenied
    if request.POST:
        # FIXME: usuwanie produktow
        print('tried to delete: ', product_slug)
    else:
        pass
    return redirect("sklep:home")

# @method_decorator(login_required, name='dispatch')
class manufacturer_create(LoginRequiredMixin, CreateView):
    model = Manufacturer
    fields = [ 'name', 'logo_image', 'description', 'country']
    success_url = reverse_lazy('sklep:home')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class manufacturer_update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Manufacturer
    fields = [ 'name', 'logo_image', 'description', 'country']
    success_url = reverse_lazy('sklep:home')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)
    # sprawdzanie czy uzytkownik jest autorem
    def test_func(self):
        manufacturer = self.get_object()
        return self.request.user == manufacturer.owner

@method_decorator(login_required, name='dispatch')
class effect_type_create(CreateView):
    model = EffectType
    fields = ['name', 'desc']
    success_url = reverse_lazy('sklep:home')

@method_decorator(login_required, name='dispatch')
class effect_type_update(UpdateView):
    model = EffectType
    fields = ['name', 'desc']
    success_url = reverse_lazy('sklep:home')

@method_decorator(login_required, name='dispatch')
class shipping_create(CreateView):
    model = Shipping
    fields = ['name', 'price', 'days_minimum']
    success_url = reverse_lazy('sklep:home')

@method_decorator(login_required, name='dispatch')
class shipping_update(UpdateView):
    model = Shipping
    fields = ['name', 'price', 'days_minimum']
    success_url = reverse_lazy('sklep:home')

@method_decorator(login_required, name='dispatch')
class cart_create(CreateView):
    model = Cart
    fields = ['user', 'products', 'shipping_method']
    success_url = reverse_lazy('sklep:home')


# @method_decorator(login_required, name='dispatch')
@login_required()
def checkout(request, pk):
    order = Order.objects.get(id=pk)
    context ={
        'order': order
    }
    return render(request, 'sklep/checkout.django-html', context)

BASE_DOMAIN = '127.0.0.1:8000'
@method_decorator(login_required, name='dispatch')
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs.get("pk"))

        order_items = []

        for item in order.items.all():
            order_items.append({
                    'price_data': {
                        'currency': 'pln',
                        'unit_amount': int(item.product.price_discounted * 100),
                        'product_data':{
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
            })

        print(order_items)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items = order_items,
            metadata={"order_id": order.id},
            mode='payment',
            # success_url=BASE_DOMAIN + '/success.html',
            # cancel_url=BASE_DOMAIN + '/cancel.html',
            # success_url = reverse('backend:checkout-success'),
            # cancel_url = reverse('backend:checkout-cancel'),
            # success_url=request.build_absolute_uri(reverse('backend:checkout-success',
            #                                                 args=(order.pk, )))
            success_url=request.build_absolute_uri(reverse('backend:checkout-success')),
            cancel_url=request.build_absolute_uri(reverse('backend:checkout-cancel')),
        )
        return redirect(checkout_session.url)
        # return JsonResponse({
        #     'id': checkout_session.id
        # })

class SuccessView(TemplateView):
    template_name = "sklep/success.django-html"

class CancelView(TemplateView):
    template_name = "sklep/cancel.django-html"

# @method_decorator(csrf_exempt, name="dispatch")
# class StripeWebhookView(View):
#     """
#     Stripe webhook view to handle checkout session completed event.
#     """
    
#     def post(self, request, format=None):
#         payload = request.body
#         endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
#         sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#         event = None

#         try:
#             event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#         except ValueError as e:
#             # Invalid payload
#             return HttpResponse(status=400)
#         except stripe.error.SignatureVerificationError as e:
#             # Invalid signature
#             return HttpResponse(status=400)

#         if event["type"] == "checkout.session.completed":
#             print("Payment successful")

#             # Add this
#             session = event["data"]["object"]
#             customer_email = session["customer_details"]["email"]
#             order_id = session["metadata"]["order_id"]
#             order = get_object_or_404(Order, id=order_id)

#             send_mail(
#                 subject="Here is your product",
#                 message=f"Thanks for your purchase. The URL is: {order.slug}",
#                 recipient_list=[customer_email],
#                 from_email="your@email.com",
#             )

#         # Can handle other events here.

#         return HttpResponse(status=200)

        # basic -------------------

        # payload = request.body

        # # For now, you only need to print out the webhook payload so you can see
        # # the structure.
        # print(payload)

        # return HttpResponse(status=200)
    
        # -----------------------
@csrf_exempt
def stripe_webhook_view(self, request, format=None):
    payload = request.body
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        print("Payment successful")

        # Add this
        session = event["data"]["object"]
        customer_email = session["customer_details"]["email"]
        order_id = session["metadata"]["order_id"]
        order = get_object_or_404(Order, id=order_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. The URL is: {order.slug}",
            recipient_list=[customer_email],
            from_email="your@email.com",
        )

    # Can handle other events here.

    return HttpResponse(status=200)