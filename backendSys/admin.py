from django.contrib import admin
from .models import Administrator
from .models import Choices
# Register your models here.
admin.site.register(Administrator)
admin.site.register(Choices)