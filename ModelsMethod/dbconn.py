from django.db import connection, models

class PersonManger(models.Manager):
    def first_name(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT first_name 
            FROM people_people WHERE 
            last_name=%s""", [last_name])
        return [row[0] for row in cursor.fetchone()]


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    objects = PersonManger()
