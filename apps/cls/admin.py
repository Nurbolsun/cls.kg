from django.contrib import admin
from .models import *


# Register your models here.
class BranchImageInline(admin.TabularInline):
    model = BranchImage
    extra = 2
    verbose_name = "Фотография"
    verbose_name_plural = "Фотографии"


class BranchAdmin(admin.ModelAdmin):
    inlines = [BranchImageInline]
    list_display = ('name', 'region', 'is_active', 'created_at')
    search_fields = ('name', 'region__name')
    list_filter = ('region', 'is_active')


admin.site.register(Branch, BranchAdmin)
admin.site.register(BranchImage)
admin.site.register(Region)
