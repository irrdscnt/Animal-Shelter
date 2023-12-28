from django.db import models

class Animal(models.Model):
    animal_id = models.AutoField(primary_key=True)
    type_of_animal=models.CharField(max_length=20,null=True,choices=[('Dog', 'Dog'), ('Cat', 'Cat')])
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

class Review(models.Model):
    name = models.TextField()
    review = models.TextField()
    email = models.CharField(max_length=100)
    photo = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return self.name

class AdoptionForm(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=40, null=True)
    email=models.CharField(max_length=255)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name