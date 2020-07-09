from django.urls import path

from . import views

app_name = 'record'
urlpatterns = [
	# ex: /record/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /record/5/
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /record/5/results/
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# ex: /record/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
]