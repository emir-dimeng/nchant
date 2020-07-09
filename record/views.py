from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Question, Choice
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'record/index.html'
	context_object_name = 'lastest_question_list'
	
	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]
'''
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'record/detail.html', {'question':question})
	#return HttpResponse("You are looking at question %s." %question_id)
'''
# shortcut
class DetailView(generic.DetailView):
	model = Question
	template_name = 'record/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'record/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question form
		return render(request, 'record/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	else:
		select_choice.votes += 1
		select_choice.save()
	# reverse(), helps avoid having to hardcode a URL.
	return HttpResponseRedirect(reverse('record:results', args=(question.id,)))



