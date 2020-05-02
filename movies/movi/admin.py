from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Test,Metadata,Ratings,Credits

admin.site.register(Test)
admin.site.register(Metadata)
admin.site.register(Ratings)
admin.site.register(Credits)
