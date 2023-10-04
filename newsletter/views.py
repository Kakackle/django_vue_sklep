from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
# from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)
    
# confirm subscription with conf num - conf num gets included from link in email
def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return redirect("sklep:home")
        # return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return redirect("sklep:home")
        # return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

# delete from subscribers with conf_num, not that necessary, can be done through the API
def unsubscribe(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    print("unscubscribe: ", sub)
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        # return render(request, 'index.html', {'email': sub.email, 'action': 'unsubscribed'})
    # else:
        # return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})
    return redirect("sklep:home")