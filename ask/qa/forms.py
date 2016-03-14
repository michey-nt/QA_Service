from django import forms
from .models import Question

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		if (len(self.cleaned_data['title'])==0 or len(self.cleaned_data['text'])==0):
			raise forms.ValidationError(
				u'One of the fields blank',
				code='blank'
			)

	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question
