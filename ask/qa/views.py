from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question

def test(request, *args, **kwargs):
	return HttpResponse('OK')

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
	
