from django.contrib import admin

from .models import anime
from .models import user


# Register your models here.

admin.site.register(anime)
admin.site.register(user)