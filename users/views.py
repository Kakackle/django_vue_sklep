from django.shortcuts import render
from django.urls import reverse_lazy
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, CreateView

# def user_view(request, username):
#     user = UserProfile.objects.get(user__username=username)
#     context = {
#         'user': user 
#     }
#     return render(request, "users/user.django-html", context)

@method_decorator(login_required, name='dispatch')
class profile_update(UpdateView):
    model = UserProfile
    fields = ['type', 'bio', 'profile_image', 'favourite_products']
    success_url = reverse_lazy('sklep:home')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)