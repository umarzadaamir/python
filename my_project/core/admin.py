from django.contrib import admin
from .models import Person, people

# Register your models here.
admin.site.register(Person)
admin.site.register(people)
