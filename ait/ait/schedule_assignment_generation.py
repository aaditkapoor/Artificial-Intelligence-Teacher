
from .models import DataModel
import random

def gather_data(username):
	assignments_questions = []
	all_data = DataModel.objects.filter(username=username)
	for i in all_data:
		assignments_questions.append(i.question)

	random.shuffle(assignments_questions)

	return assignments_questions




