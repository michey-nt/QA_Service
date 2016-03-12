from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def main(request):
	page = request.GET.get('page', 1)

	questions = Question.objects.order_by('-added_at')
	
	paginator = Paginator(questions, 10)
	paginator.baseurl = '?page='

	page = paginator.page(page)

	return render (request, 'main.html', {
		questions:	page.object_list,
		paginator:	paginator, page: page,
	})
