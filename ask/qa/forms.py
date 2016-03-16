from django import forms
from .models import Question, Answer

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

	def save(self):
		answer = Answer(text = self.cleaned_data['text'],
			question_id = self.cleaned_data['question'])
		answer.save()
		return answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question
