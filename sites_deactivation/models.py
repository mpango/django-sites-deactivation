# encoding: utf-8
"""
With SiteDeactivations you can temporarily disable an entire site via the
admin panel. All requests to that site will then be redirected to a specified
URL. Only requests to the admin and django.contrib.flatpages will work as
usual.

To deactivate the site, create a new SiteDeactivation instance in the admin
for it with an according redirect URL. If this URL points to your own site,
make sure it is a django FlatPage!
"""
from django.db import models
from django.contrib.sites.models import Site

class SiteDeactivation(models.Model):
	"""
	Defines the actual site deactivation. Simply connects a site (that is to
	be disabled) with a redirect URL.
	"""
	site = models.ForeignKey(Site)
	redirect_url = models.URLField(blank=False, null=False, max_length=200, verify_exists=False, help_text="Example: 'http://www.example.com/deactivated/'. Make sure to have trailing slashes.")
	
	class Meta:
		app_label = 'sites'
		verbose_name = 'Site Deactivation / Redirect'
		verbose_name_plural = 'Site Deactivations / Redirects'
	
	
	def __unicode__(self):
		return "%s -> %s"%(self.site.domain, self.redirect_url)
	
