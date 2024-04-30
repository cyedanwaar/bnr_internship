from django.contrib import admin
from .models import Job, Applicant, Organization, Resource, Reference, BiderSupplier


admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Organization)
admin.site.register(Resource)
admin.site.register(Reference)
admin.site.register(BiderSupplier)
