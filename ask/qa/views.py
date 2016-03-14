from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer
from .forms import AskForm

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def ask(request, *args, **kwargs):
	form = AskForm()
	if request.method == "GET":
		return render(request, 'ask.html', {'form' : form})
	else:
		if form.is_valid():
			question = form.save()
			id = question.id
			return HttpResponseRedirect("/question/" + id)

def question(request, *args, **kwargs):
	one_question = get_object_or_404(Question, id = args[0])
	answers = Answer.objects.filter(question=one_question)
	return render(request, 'question.html',  {
		'question' : one_question,
		'answers' : answers,
	})

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
