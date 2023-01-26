from django.contrib import admin

# Register your models here.
from core.models import *


@admin.register(URLs)
class URLsAdmin(admin.ModelAdmin):
    pass


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    pass
