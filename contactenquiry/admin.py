from django.contrib import admin
from contactenquiry.models import contactEnquiry
# Register your models here.
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name',  'email', 'message')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to search within the admin interface
    list_filter = ('name', 'email')  

admin.site.register(contactEnquiry, ContactEnquiryAdmin)