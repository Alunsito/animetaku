from django.contrib import admin

from .models import anime, user, anime_review

class AnimeAdmin(admin.ModelAdmin):
    fields = ['name_anime','release_date','genres']

class userInline(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['name_user']}),
        ('Date information', {'fields': ['email', 'classes': ['collapse']]})
    ]
    inline = [userInline]
# Register your models here.

admin.site.register(anime, AnimeAdmin)
admin.site.register(user,userInline)