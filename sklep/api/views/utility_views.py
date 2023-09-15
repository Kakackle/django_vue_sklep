# from django.shortcuts import get_object_or_404
# from sklep.api.permissions import IsOwnerOrReadOnly
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token})