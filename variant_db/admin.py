from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Family)
admin.site.register(dnaSample)
admin.site.register(Test)
admin.site.register(Variant)
admin.site.register(Gene)
admin.site.register(Classification)
admin.site.register(Evidence)
admin.site.register(acmgCodes)
