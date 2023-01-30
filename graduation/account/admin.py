from django.contrib import admin

from .models import Child, Kindergarden, KIDCHOICE


# class KindergardenAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'kindergarden':
#             kwargs["queryset"] = Kindergarden.objects.filter()
# Register your models here.

class ChildInline(admin.TabularInline):
    model = Child

@admin.register(Kindergarden)
class KindergardenAdmin(admin.ModelAdmin):
    inlines = [
        ChildInline
    ]


admin.site.register(Child)
# admin.site.register(Kindergarden)
admin.site.register(KIDCHOICE)


