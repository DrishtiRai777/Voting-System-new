from django.contrib import admin
from backapp.models import OrganizationDetails, AdministrativeDetails, Usersdetail


# Register your models here.
admin.site.register(OrganizationDetails)
admin.site.register(AdministrativeDetails)
admin.site.register(Usersdetail)
