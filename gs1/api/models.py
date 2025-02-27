from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


# after creating a model, you can run makemigrations, generates migration files based on changes in your models.
# then run python manage.py migrate to apply the migration files to the database

#then we created a superuser using python manage.py createsuperuser to access the admin panel.
