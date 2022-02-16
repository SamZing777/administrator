from django.db import models

from entities.models import (
	Hero,
	Villain
	)


class Epic(models.Model):
	name = models.CharField(max_length=250)
	participating_heroes = models.ManyToManyField(Hero)
	participating_villains = models.ManyToManyField(Villain)

	def __str__(self):
		return self.name


class Event(models.Model):
	epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
	details = models.TextField()
	years_ago = models.PositiveSmallIntegerField()


class EventHero(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
	is_primary = models.BooleanField()


class EventVillain(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
	is_primary = models.BooleanField()
