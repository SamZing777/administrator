from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
		Category,		
		Origin,
		Hero,
		Villain
	)


class ExportCSVMixin:
	def export_as_csv(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment: filename = {}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)

		for obj in queryset:
			row = writer.writerow([getattr(obj, field) for field in field_names])
			return response

		export_as_csv.short_description = "Export Selected"


class OriginAdmin(admin.ModelAdmin):

	def hero_count(self):
		return self.hero_set.count()

	def villain_count(self):
		return self.villain_set.count()

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		queryset = queryset.annotate(
			herocount = Count("hero", distinct=True),
			villaincount = Count("villain", distinct=True)
		)
		return queryset

	list_display = ['name', hero_count, villain_count]
	actions = ["export_as_csv"]


class IsVeryBenevolentFilter(admin.SimpleListFilter):
	title = 'is_very_benevolent'
	parameter_name = 'is_very_benevolent'

	def lookups(self, request, model_admin):
		return(
			('Yes', 'Yes'),
			('No', 'No')
		)

	def get_queryset(self, request, queryset):
		value = self.value()
		if value == 'Yes':
			return queryset.filter(benevolence_factor__gt=75)
		elif  value == 'No':
			return queryset.exclude(benevolence_factor__gt=75)
		return queryset


class HeroAdmin(admin.ModelAdmin):
	actions = ["mark_immortal"]

	def mark_immortal(self, request, queryset):
		queryset.update(is_immortal=True)

	list_display = ['name', 'is_immortal', 'category', 'origin', IsVeryBenevolentFilter]
	actions = ["export_as_csv"]


"""
	def is_very_benevolent(self, obj):
		return obj.benevolence_factor > 75
"""


admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Origin, OriginAdmin)
admin.site.register(Hero)
admin.site.register(Villain)
