from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^$', 'qa.views.main'),
	url(r'^login/', 'qa.views.login'),
	url(r'^signup/', 'qa.views.signup'),
	url(r'^question/(\d+)/$', 'qa.views.question'),
	url(r'^ask/', 'qa.views.ask'),
	url(r'^answer/', 'qa.views.answer'),
	url(r'^popular/', 'qa.views.popular'),
	url(r'^new/', 'qa.views.test'),
]
