from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'waiting$', 'quiz.views.waiting',name='waiting'),
	url(r'getquestion$', 'quiz.views.getquestion'),
	url(r'checkanswer$', 'quiz.views.checkanswer'),
	url(r'$', 'quiz.views.quiz',name='quiz'),
)
