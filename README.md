# INSTALLATION

The ´site_deactivation´ app requires that[django's flatpages app](https://docs.djangoproject.com/en/1.3/ref/contrib/flatpages/ "django flatpages")
is also added to your django project.

* copy the ´site_deactivation´ app to your PYTHON_PATH
* add the ´site_deactivation´ app to your INSTALLED_APPS
* add the ´django.contrib.flatpages´ app to your INSTALLED_APPS
* add ´django.contrib.flatpages.middleware.FlatpageFallbackMiddleware´ and
  ´site_deactivation.SiteDeactivationMiddleware.SiteDeactivationMiddleware´
  to your MIDDLEWARE_CLASSES as the topmost entries in that order.
* run ´python manage.py syncdb´

# USAGE

Go to your admin panel and you'll find a new entry ´Site Deactivations / Redirects´
under the ´Sites´ group. In order to temporarily disable an entire site and
let it redirect to a static URL, simply create a new entry there, specifying
the SITE you want to disable and the redirect URL. This redirect URL could be
a reference to a django flatpage.

*Beware* though that deactivating a site in fact deactivates all pages of
that site, except the flatpages linked to the SITE_ID. So the redirect URL
you specify either needs to be directing to a flatpage or it needs to be for
a different SITE_ID in order to work properly!