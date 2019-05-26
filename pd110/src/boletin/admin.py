from django.contrib import admin

# Register your models here.
from .models import Registrados

class AdminRegistrados(admin.ModelAdmin):
	list_display = ["email", "nombre", "timestamp"]
	list_filter = ["timestamp"]
	# list_display_links = ["nombre"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]
	class Meta:
		model = Registrados


admin.site.register(Registrados, AdminRegistrados)