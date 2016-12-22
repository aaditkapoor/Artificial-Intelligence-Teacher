from django.db import model


# System generated plsu user generated
class DataModel(models.Model):
	username = models.CharField(max_length=200)
	question = models.CharField(max_length=500)
	answer = models.CharField(max_length=500)

	def __unicode__(self):
		return "Questions of "  + self.username
class AssignmentID(models.Model):
	assignmentId = models.CharField(max_length=20)


	def __unicode__(self):
		return self.assignmentId