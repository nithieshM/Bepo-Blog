from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# For users and Posts we import from the model Users. Now the relationship
# between Users and Posts are 1:M (cause a single user can have many different posts but a post can have
# only one author.)
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Makes django delete the posts of the user if the user is deleted.

    def __str__(self):
        return self.title


