# encoding: utf-8
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage
from site_deactivation.models import SiteDeactivation

class SiteDeactivationMiddleware(object):
	"""
	Include the SiteDeactivationMiddleware in your settings.py's
	MIDDLEWARE_CLASSES array. Usually it should be the first entry, so it can
	stop any further processing if a site is actually disabled and should be
	redirected.
	"""
	
	def _get_url(self, request):
		"""basically taken from django.contrib.flatpages.views.flatpage"""
		url = request.path_info
		if not url.endswith('/') and settings.APPEND_SLASH:
			return HttpResponseRedirect("%s/" % request.path)
		if not url.startswith('/'):
			url = "/" + url
		return url
	
	
	def process_request(self, request):
		"""
		In case a SiteDeactivation exists for the requested site, redirect
		the user to it's static redirect URL. Otherwise simply do nothing.
		"""
		path = request.path
		try:
			current_site = Site.objects.get(domain__exact=request.META['HTTP_HOST'])
		except:
			return None
		
		if not (path == "/admin" or path.startswith("/admin/")):
			deactivation = SiteDeactivation.objects.filter(site__id__exact=current_site.pk)
			
			# If we found a deactivation, redirect to it's redirect URL.
			if deactivation.count() == 1:
				return HttpResponseRedirect(deactivation.get().redirect_url)
		
		# Default is simply do do nothing.
		return None
	
