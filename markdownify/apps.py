from django.apps import AppConfig
from django.core.checks import register

from markdownify.checks import settings_check


class MarkdownifyConfig(AppConfig):
    name = 'markdownify'

    def ready(self):
        register(settings_check)
