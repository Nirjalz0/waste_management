from django.contrib import admin
from .models import wasteCategory , CollectionRequest
admin.site.register(wasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


admin.site.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'waste_category', 'quantity', 'status', 'preferred_date', 'collector')
    list_filter = ('status', 'waste_category', 'preferred_date')
    search_fields = ('customer__username', 'address')
# Register your models here.
