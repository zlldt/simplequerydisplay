from django.db import models

# Create your models here.


class Person(models.Model):
    sn = models.IntegerField()
    id_num = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    township = models.CharField(max_length=30)
    village = models.CharField(max_length=30)

    def __str__(self):
        return self.id_num

    class Meta:
        db_table = "jzfpgrxx1"
