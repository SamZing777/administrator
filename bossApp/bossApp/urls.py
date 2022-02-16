from django.contrib import admin
from django.urls import path

from events.admin import event_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event_admin/', event_admin_site.urls)
]


admin.site.site_header = "Boss Admin"
admin.site.site_title = "Boss Admin Portal"
admin.site.index_title = "Welcome to Boss Admin's Portal"
