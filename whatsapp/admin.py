from django.contrib import admin
from .models import Mobile

class WhatsappAdmin1(admin.ModelAdmin):
  list_display = ("brand", "cost")
  search_fields=Mobile.searchablefields
  
urlpatterns1 = [
    admin.site.register(Mobile, WhatsappAdmin1)
]
