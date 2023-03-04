from django.contrib import admin
# import models here
from .models import Finch, Siting, Food

# Register your models here.
admin.site.register(Finch)
# Register our sitings model
admin.site.register(Siting)
# Register our food model
admin.site.register(Food)