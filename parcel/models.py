import logging
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from post_machine.models import PostMachine, Locker
from django.db.models.signals import post_save
from django.dispatch import receiver
logger = logging.getLogger(__name__)


# Create your models here.


class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    order_datetime = models.DateTimeField("date published")
    open_datetime = models.DateTimeField("date published", null=True, blank=True)
    update_datetime = models.DateTimeField("date published", default=datetime.now)
    status = models.BooleanField(default=False)
    # True-Delivered, false-not delivered(on delivery fill "open_datetime")

# один з цих треба для адекватного відображення
#     def __str__(self):
#         return (f"{self.recipient} {self.sender} {self.size} {self.post_machine_recipient}"
#                 f"{self.order_datetime} {self.open_datetime} {self.update_datetime}"
#                 f"{self.status}")
#
#     def __repr__(self):
#         return (f"{self.recipient} {self.sender} {self.size} {self.post_machine_recipient}"
#                 f"{self.order_datetime} {self.open_datetime} {self.update_datetime}"
#                 f"{self.status}")

    def __str__(self):
        return f"{self.pk} {self.sender} - {self.recipient}"

    def __repr__(self):
        return f"{self.pk} {self.sender} - {self.recipient}"


@receiver(post_save, sender=Parcel)  # Connect to the built-in post_save signal
def update_status_on_parcel_put_to_locker(sender, instance, created, **kwargs):
    # This function will be called automatically after Order model instance is saved

    print(instance)
    if instance.status == False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = False
            parcel_locker.save()
            logger.info(f"updated locker status for parcel {instance}")
