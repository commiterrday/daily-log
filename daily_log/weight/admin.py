from django.contrib import admin
from weight.models import Weight

class WeightAdmin(admin.ModelAdmin):
    list_display = ('time', 'kg', 'body_fat')

# Register your models here.
admin.site.register(Weight, WeightAdmin)
