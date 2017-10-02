# django-revisited

## migrations
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

## shell it
`python manage.py shell`

## create a superuser
`python` manage.py createsuperuser`
