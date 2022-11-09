from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model): #Creating a 1-1 relationship with users and profiles.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    bio = models.TextField()    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): # resizing profile pictures to save space.
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path) 


