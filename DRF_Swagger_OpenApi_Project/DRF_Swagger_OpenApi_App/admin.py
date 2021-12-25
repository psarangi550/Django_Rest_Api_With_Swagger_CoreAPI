from django.contrib import admin
from .models import WFMTTASKMODEL
# Register your models here.

@admin.register(WFMTTASKMODEL)
class WFMTTASKMODELADMIN(admin.ModelAdmin):
    list_display=['id','cp_number','sne_id','scheme_number','trs','estimate']
    
