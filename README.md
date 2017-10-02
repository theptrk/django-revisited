# django-revisited

## config
### migrations
[ ] change you models (in models.py)
[ ] `python manage.py makemigrations`
[ ] `python manage.py migrate`

```python
# example creating migrations only for the polls app

# create a migration file called migrations/0001_initial.py
python manage.py makemigreations polls

# check what sql commands that file would run
python manage.py sqlmigrate polls 0001

# check that for any problems
python manage.py check
```

### shell it
`python manage.py shell`

### create a superuser
`python` manage.py createsuperuser`

## urls
```python
# <project_name>/urls.py
# basic plumbing
urlpatterns = [
    url(r'^someregex/', path.to.view.method)
]

# mount urls by using `include` where the view method would be
# <project_name>/urls.py
from django.conf.urls import include
urlpatterns = [
    url(r'^someregex/', include('<app_name>.urls')
]

# <app_name>/urls.py
urlpattens = [
    url(r'^$', views.index, name='index')
]

# <app_name>/views.py
def index(request):
    return "Hello Django"
```

## templates
- when settin `APP_DIRS` is set to true, you're templates directory needs to be
  namespaced inside of the app_name directory *inside* the templates directory. 
- say your app is polls, then your directory should be in:
`<app_name>/templates/<app_name>/index.html`

### context passing
```python
# <app_name>/views.py
# assume Question is a model, polls is my app name
def index(request):
    list = Question.objects.order_by('pub_date')[:5]
    return redner(request, 'polls/index.html', {list: list})

```
```jinja
# polls/templates/polls/index.html
{% for q in list %}
  {{q.attribute1}}
  {{q.attribute2}}
{% endfor %}
```
