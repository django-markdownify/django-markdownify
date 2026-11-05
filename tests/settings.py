DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
INSTALLED_APPS = ["markdownify"]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]
