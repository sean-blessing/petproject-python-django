from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    breed_id = models.IntegerField(db_column="BreedId")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    birth_year = models.IntegerField(db_column="BirthYear")
    birth_month = models.IntegerField(db_column="BirthMonth")
    available = models.BooleanField(default=False)
    class Meta:
        db_table = "pet"
    