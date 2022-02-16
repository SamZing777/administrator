from django.contrib import admin

from .models import (
	Epic,
	Event,
	EventHero,
	EventVillain
	)


class EventAdminSite(admin.AdminSite):
	site_header = 'Event Admin Site'
	site_header = 'Event Admin Site Portal'
	index_title = "Welcome to Event Admin Site Panel"

event_admin_site = EventAdminSite(name='event_admin')


event_admin_site.register(Epic)
event_admin_site.register(Event)
event_admin_site.register(EventHero)
event_admin_site.register(EventVillain)
