from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__	(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'


class Origin(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Entity(models.Model):
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Rather not say', 'Rather not say')
	)

	name = models.CharField(max_length=100)
	alternative_name = models.CharField(max_length=100, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
	gender = models.CharField(max_length=20, choices=GENDER)
	description = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		abstract = True


class Hero(Entity):
	is_immortal = models.BooleanField(default=True)
	benevolence_factor = models.PositiveSmallIntegerField()
	arbitrariness_factor = models.PositiveSmallIntegerField()
	father = models.ForeignKey("self", related_name="+", null=True, blank=True,
					on_delete=models.SET_NULL)
	mother = models.ForeignKey("self", related_name="+", null=True, blank=True,
					on_delete=models.SET_NULL)
	spouse = models.ForeignKey("self", related_name="+", null=True, blank=True,
					on_delete=models.SET_NULL)

	class Meta:
		verbose_name_plural = 'Heroes'


class Villain(Entity):
	is_immortal = models.BooleanField(default=False)
	malevolence_factor = models.PositiveSmallIntegerField()
	power_factor = models.PositiveSmallIntegerField()
	is_unique = models.BooleanField(default=True)
	count = models.PositiveSmallIntegerField(default=1)
