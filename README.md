#

Install deps:
```
apt-get install nodejs nodejs-legacy npm
pip install djangobower
```

Update django settings file. In settings.py:
```python

INSTALLED_APPS = (
    'djangobower',
    'caboskin'
)

BOWER_INSTALLED_APPS = (
    'jquery#2.1',
    'jquery-ui#1.11',
    'bootstrap#3.3',
    'flat-ui#2.2',
    'html5shiv',
    'respond'
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    )

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
```


