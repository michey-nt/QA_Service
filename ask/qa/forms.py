from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=30)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def save(self):
		user = User.objects.create_user(
			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password'])
		user.save()
		return user

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())
	_author = None

	def save(self):
		answer = Answer(text = self.cleaned_data['text'],
			question_id = self.cleaned_data['question'],
			author = self._author,				
			)
		answer.save()
		return answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	_author = None

	def save(self):
		question = Question(title = self.cleaned_data['title'],
			text = self.cleaned_data['text'],
			author = self._author,
			)
		question.save()
		return question
