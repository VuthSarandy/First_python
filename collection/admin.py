from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'dob', 'contact', 'active']
    # list_editable = ['last_name', 'gender', 'dob', 'contact', 'active']
    list_display_links = ['first_name', 'last_name', 'gender', 'dob', 'contact', 'active']
    # list_per_page = 1

admin.site.register(Person, PersonAdmin)