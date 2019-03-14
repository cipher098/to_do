from django.db import models
import datetime

class Work(models.Model):
	priority_list = (
	    ('!', 'Low'),
	    ('!!', 'Medium'),
	    ('!!!', 'High'),
	)
	priority = models.CharField(max_length=3, choices=priority_list, default='!')
	work = models.CharField(max_length=100, null=True, blank=True)
	# created_time = models.DateField(default=datetime.date.today)
	created_time = models.DateTimeField(default=datetime.datetime.now)
	due_time = models.DateTimeField(null=True, blank=True)
	# description = models.TextField(null=True, default='', blank=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.work + '|' + str(self.completed)