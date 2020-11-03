from django.db import models


class Programme(models.Model):
    title = models.CharField(max_length=50)
    release = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(null=True,blank=True)
    banner = models.ImageField(upload_to='images/',)
    service = models

    def __str__(self):
        return f'{self.name}'

    def create_programme(self):
        self.save()

    def delete_programme(self):
        self.delete()

    @classmethod
    def find_programme(cls, programme_id):
        return cls.objects.filter(id=programme_id)




class Service(models.Model):
    name = models.CharField(max_length=120)
    Equipments = models.ManyToManyField(Equipment)



class Equipment(models.Model):
    name = models.CharField(max_length=120)
    Services = models.ManyToManyField(Service)
    


