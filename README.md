# INSTALLATION

* copy the ´site_deactivation´ app to your PYTHON_PATH
* add the ´site_deactivation´ app to your INSTALLED_APPS
* add ´site_deactivation.SiteDeactivationMiddleware.SiteDeactivationMiddleware´
  to your MIDDLEWARE_CLASSES as the topmost entry (unless you are using
  django flatpages, in that case put it just underneath their middleware)
* run ´python manage.py syncdb´

A good addition to the ´site_deactivation´ app is [django's flatpages app](https://docs.djangoproject.com/en/1.3/ref/contrib/flatpages/ "django flatpages").

# USAGE

Go to your admin panel and you'll find a new entry ´Site Deactivations / Redirects´
under the ´Sites´ group. In order to temporarily disable an entire site and
let it redirect to a static URL, simply create a new entry there, specifying
the SITE you want to disable and the redirect URL. This redirect URL could be
a reference to a django flatpage.