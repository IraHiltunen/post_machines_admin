from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine

# Create your models here.


class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField("date published")
    open_datetime = models.DateTimeField("date published")
    update_datetime = models.DateTimeField("date published", default=datetime.now)
    status = models.BooleanField(default=False)

# один з цих треба для відображення адекватного
    def __str__(self):
        return f"{self.address} {self.city}"

    def __repr__(self):
        return f"{self.address} {self.city}"