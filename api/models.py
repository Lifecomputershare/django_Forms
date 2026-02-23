from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200, unique=True)

    class Meta:
        db_table = 'registers'

    def __str__(self):
        return self.name