from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Child, Kindergarden, KIDCHOICE, User


# class KindergardenAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'kindergarden':
#             kwargs["queryset"] = Kindergarden.objects.filter()
# Register your models here.

class ChildInline(admin.TabularInline):
    model = Child

@admin.register(Kindergarden)
class KindergardenAdmin(TranslatableAdmin):
    inlines = [
        ChildInline
    ]


admin.site.register(Child)
# admin.site.register(Kindergarden)
admin.site.register(KIDCHOICE)
# admin.site.register(Kindergarden,TranslatableAdmin)
class UseAdmin(admin.ModelAdmin):
    list_display = ('last_name','address', 'phone', 'email')
admin.site.register(User,UseAdmin)

