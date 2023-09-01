from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Index response")

#TODO: only make viewa accessible on login ale nie mamy login view gdzie moglibysy tego dokonac
# @method_decorator(login_required, name='dispatch')
class VueView(TemplateView):
    template_name = 'index.django-html'

    def get_context_data(self, **kwargs):
        # product_1 = Product.objects.get(pk=1)
        # przekazywanie danych do vue przez context
        if self.request.user.is_authenticated:
            name = self.request.user.first_name
        else:
            name = 'no user'
        return {
            'test': 'test content',
            # 'user': self.request.user,
            'user': name,
            # 'product': product_1
        }

# FIXME: okej, dziala, tylko ze url z ?next=.. daje 404 - do rozwiazania
@login_required()
def other_django_view(request):
    context = {
        "test": "yes it's me context",
        "user": request.user
    }
    return render(request, 'sklep/other.django-html', context)