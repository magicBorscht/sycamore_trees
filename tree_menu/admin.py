from django.contrib import admin
from .models import MenuNode


class NodeAdmin(admin.ModelAdmin):
    exclude = ['level']


admin.site.register(MenuNode, NodeAdmin)
