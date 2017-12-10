# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Test(models.Model):

	class Meta(object):
		verbose_name = u'Тест'
		verbose_name_plural = u'Тести'

	name = models.CharField(
      max_length=256,
      blank=False)

	def __str__(self):
		return u'%s' % (self.name)


class Question(models.Model):

	class Meta(object):
		verbose_name = u'Питання тесту'
		verbose_name_plural = u'Питання тестів'

	test = models.ForeignKey(Test,	
		blank=True,
		null=True,
		default=None)
	description = models.CharField(
      max_length=400,
      blank=False)
	version_a = models.CharField(
		max_length=400,
		blank=False,
		null=False)
	version_b = models.CharField(
		max_length=400,
		blank=False,
		null=False)
	version_c = models.CharField(
		max_length=400,
		blank=True,
		null=True)
	version_d = models.CharField(
		max_length=400,
		blank=True,
		null=True)
	true = models.CharField(
		max_length=400,
		blank=False,
		null=False)
	
	def __str__(self):
		return u'%s' % (self.description)



class Result(models.Model):

	class Meta(object):
		verbose_name = u'Результат'
		verbose_name_plural = u'Результати'

	name = models.CharField(
      max_length=20,
      blank=False)
	surname = models.CharField(
      max_length=20,
      blank=False)
	rating = models.CharField(
      max_length=3,
      blank=False)
	choices = models.CharField(
      max_length=50,
      blank=False)

	def __str__(self):
		return u'%s' % (self.surname)	
