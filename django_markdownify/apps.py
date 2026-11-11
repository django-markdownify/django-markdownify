from django.apps import AppConfig
from django.core.checks import register

from django_markdownify.checks import settings_check


class MarkdownifyConfig(AppConfig):
    name = 'django_markdownify'

    def ready(self):
        register(settings_check)
