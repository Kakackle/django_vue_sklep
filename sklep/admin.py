from django.contrib import admin
from sklep.models import *
from users.models import *
from newsletter.models import *

from django.apps import apps

# custom registration
# admin.register()

# automatic registration

# get all model fields

# custom registration with an extra "send newsletter" action
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"

class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)

# custom registration to choose fields
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_created', 'price', 'owner', 'main_product_image', 'rating_average', 'manufacturer', 'quantity', 'discount', 'bought_count')

admin.site.register(Product, ProductAdmin)

# all other models

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        # self.fields = sorted([field.name for field in model._meta.fields if field.editable])
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

models = apps.get_models()

for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass