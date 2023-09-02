from django.contrib import admin
from sklep.models import *
from users.models import *

from django.apps import apps

# custom registration
# admin.register()

# automatic registration

# get all model fields
class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        # self.fields = sorted([field.name for field in model._meta.fields if field.editable])
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

models = apps.get_models()

for model in models:
    # apply display of all fields
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass