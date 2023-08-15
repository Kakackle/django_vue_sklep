from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Profile

# Create your views here.

def index(request):
    return HttpResponse("Index response")

#only make viewa accessible on login
@method_decorator(login_required, name='dispatch')
class VueView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        #context
        # tutaj context_variable przekazywane jest jako cokolwiek
        # celem bylo przekazanie **kwargs, w ktorym zawarte jest path ze sciezki po vue/
        # zgodnie z konfiguracja w urls
        return {
            'context_variable': 'value'
        }
        # return {
        #     'user_types': [{
        #         'id': c[0],
        #         'name': c[1]
        #     } for c in Profile.USER_TYPE],
        # }