from django.contrib import admin
from .models import UserModel
from ait.models import DataModel

admin.site.register(UserModel)
admin.site.register(DataModel)