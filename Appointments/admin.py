from django.contrib import admin
from django.apps import apps
from .models import *
class AppsAdmin(admin.ModelAdmin):
    list_display = ('startTime', 'endTime', 'workingTime', 'priceListPosition', 'client')

admin.site.register(Appointment, AppsAdmin)

admin.site.register(Job)
admin.site.register(Employee)
admin.site.register(Table)
admin.site.register(WorkingTime)
admin.site.register(PriceList)
admin.site.register(PriceListPosition)
admin.site.register(Service)

#from .models import Вот тут
#Register your models here.
#app_config = apps.get_app_config('apps')

#Те модели которые не нужно регистрировать!!! Их нужно импортнуть отдельно
#NOT_REGISTERED_MODELS = []
#for model in app_config.get_models():
#    if not (model in NOT_REGISTERED_MODELS):
#       admin.site.register(model)
