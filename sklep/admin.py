from django.contrib import admin
from sklep.models import *
from users.models import *

from django.apps import apps

# custom registration
# admin.register()

# automatic registration
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass