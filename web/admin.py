from django.contrib import admin

from .models import Receipt, Person, UploadedFile

admin.site.register(Receipt)
admin.site.register(Person)
admin.site.register(UploadedFile)
