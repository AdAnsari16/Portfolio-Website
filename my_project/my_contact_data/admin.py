#------Django Internal Packages-----
from django.contrib import admin
#/------Django Internal Packages-----
 
#------Django Importing Models-----
from my_contact_data.models import ContactForm
#/------Django Importing Models-----
 
#Register your models here.
 
#-----Django Admin View for ----
 
#Django Admin View for Contact Form Model
class ContactFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name","email_id"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "message"
    ]
admin.site.register(ContactForm,ContactFormkAdmin)
