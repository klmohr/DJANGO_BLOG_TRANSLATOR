from django.contrib import admin
from .models import Post


class PosAdmin(admin.ModelAdmin):
    list_display = ('title','date_created','author')

# Register your models here.
admin.site.register(Post,PosAdmin)