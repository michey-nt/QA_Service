from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
from django.contrib import auth
from django.contrib.auth.models import User

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def login (request, *args, **kwargs):
	if request.method == "GET":
		form = LoginForm()
		return render(request, 'login.html', {'form' : form})
	else:
		username = request.POST.get('username')
    		password = request.POST.get('password')
    		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			form = LoginForm()
			return render(request, 'login.html', {'form' : form})

def signup (request, *args, **kwargs):
	if request.method == "GET":
		form = SignUpForm()
		return render(request, 'signup.html', {'form' : form})
	else:
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			user = auth.authenticate(username = request.POST['username'],
				password = request.POST['password'])
			auth.login(request, user)
			return HttpResponseRedirect('/')

def answer(request, *args, **kwargs):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._author = request.user
			answer = form.save()
			return HttpResponseRedirect('/question/' + str(answer.question_id))

def ask(request, *args, **kwargs):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			form._author = request.user
			question = form.save()
			return HttpResponseRedirect('/question/' + str(question.id))
	else:
		form = AskForm()
	return render(request, 'ask.html', {'form' : form})

def question(request, *args, **kwargs):
	question = get_object_or_404(Question, id=args[0])
	answers = Answer.objects.filter(question = question)
	form = AnswerForm(initial={'question' : question.id})
	return render(request, 'question.html',
		{'question' : question, 'answers' : answers, 'form' : form})

def main(request):
	question_list = Question.objects.all().order_by('-id')
	paginator = Paginator(question_list, 10)
	
	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	return render(request, 'main.html', { 'questions' : questions })
	
def popular(request):
	question_list = Question.objects.all().order_by('-rating')
	paginator = Paginator(question_list, 10)

	page = request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)
	
	return render(request, 'main.html', { 'questions' : questions })
