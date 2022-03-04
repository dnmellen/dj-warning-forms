from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.question
