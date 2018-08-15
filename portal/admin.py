from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Documentinstance)
class DocumentinstanceAdmin(admin.ModelAdmin):
    pass

class Documentinstance(admin.TabularInline):
    model = Documentinstance
    extra = 1
    pass

@admin.register(templateinstance)
class templateinstanceAdmin(admin.ModelAdmin):
    pass
    
class templateinstance(admin.TabularInline):
    model = templateinstance
    extra = 1
    pass

@admin.register(templateset)
class templateset(admin.ModelAdmin):
    inlines = [templateinstance]
    pass