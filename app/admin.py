from django.contrib import admin
from .models import Report, Profile

admin.site.site_header = 'Administracion de Reportes CAAE'

class ReportAdmin(admin.ModelAdmin):
	list_filter = ('ano_reporte','tipo_reporte','reporte_Departamento',)
	list_display = ('tipo_reporte','nombre','reporte_Departamento',)
		

class ProfileAdmin(admin.ModelAdmin):
	list_filter = ('facultad','tipo_Usuario',)
	list_display = ('user','facultad','tipo_Usuario',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Report, ReportAdmin)


