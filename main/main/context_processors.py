from django.conf import settings # import the settings file

def template_settins(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'SITE_NAME': settings.SITE_NAME,
        'BLOG_ENABLED': settings.BLOG_ENABLED,
        'TRAINING_ENABLED': settings.TRAINING_ENABLED
    }