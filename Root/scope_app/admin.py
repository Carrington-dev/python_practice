from django.contrib import admin

from scope_app.models import Dino, Park, Zone

# Register your models here.
@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    '''Admin View for Park'''

    list_display = ('name','is_safe',)
    ordering = ('name',)

    def is_safe(self, obj):
        return obj.is_safe()

    is_safe.boolean = True

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    '''Admin View for Park'''

    list_display = ('location',)
    
    
    search_fields = ('location',)
    # date_hierarchy = 'created'
    ordering = ('-pk',)

    


@admin.register(Dino)
class DinoAdmin(admin.ModelAdmin):
    '''Admin View for Dino'''

    list_display = ('name', 'park', 'species', 'gender', 'digestion_period_in_hours', 'herbivore',  'created_at', 'updated_at')
    
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('name',)


    