from django.db import models
from accounts.models import UserProfile


class Pet(models.Model):
    type = models.CharField(max_length=6)
    name = models.CharField(max_length=6)
    age = models.SmallIntegerField()
    description = models.TextField()
    image_field = models.ImageField(upload_to='images/pet-avatars')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -> {self.pet}'
