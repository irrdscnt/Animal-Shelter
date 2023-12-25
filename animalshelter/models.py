from django.db import models

class Dog(models.Model):
    dog_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    breed=models.CharField(max_length=255,null=True)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    age = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    temper = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField()
    comments = models.TextField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    news_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    title1=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    photo = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.title

