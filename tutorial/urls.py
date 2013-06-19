from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns( '' ,
                        url(r '^hello_world/' , include( 'tutorial.hello_world.urls' )),
                        url(r '^$' ,  'tutorial.hello_world.views.welcome' ,name= 'hello_world-welcome' ),
						#url(r'^(?P<name>.[^/]+)/(?P<age>\d+)/$', 'welcome', name='hello_world-welcome-name-age'),

						    # Examples:
						    # url(r'^$', 'tutorial.views.home', name='home'),
						    # url(r'^tutorial/', include('tutorial.foo.urls')),

						    # Uncomment the admin/doc line below to enable admin documentation:
						    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

						    # Uncomment the next line to enable the admin:
						    # url(r'^admin/', include(admin.site.urls)),
						)