from django.db import models

# Create your models here.
class msg_Post(models.Model):
    text = models.TextField()

    # def __str__(self):
    #     return self.text[:50]
    def __str__(self):
        return f"{self.text}"

