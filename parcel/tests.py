from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from parcel import models as parcel_models
from post_machine import models as post_machine_models


class MyTestCase(TestCase):
    fixtures = ["data5"]  # maybe can ["data.json"]

    def setUp(self):
        test_pmachine = post_machine_models.PostMachine.objects.get(pk=1)
        test_locker = post_machine_models.Locker.objects.filter(post_machine=test_pmachine).all()[0]
        self.locker_id = test_locker.pk
        self.test_parcel = parcel_models.Parcel()
        self.test_parcel.recipient = User.objects.create_user(username='test_user',
                                                              password='test_password')
        self.test_parcel.sender = 'Ann'
        self.test_parcel.size = 1
        self.test_parcel.post_machine_recipient = test_pmachine
        self.test_parcel.locker = test_locker  # посилка чекає в поштоматі
        self.test_parcel.order_datetime = '2021-01-01 10:00:00'
        self.test_parcel.open_datetime = '2021-01-02 10:00:00'
        self.test_parcel.status = False
        self.test_parcel.save()
        self.test_parcel.locker.status = False
        self.test_parcel.locker.save()

    def test_something(self):
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.locker.pk)
        self.assertEqual(actual_locker.status, False)
        c = Client()  # хочемо забрати посилку, тому клаєнт залогінений повинен бути
        c.login(username='test-user', password='test_password')
        response = c.post(f'/parcel/get_parcel/', {'parcel_id': self.test_parcel.pk})  # доробити!!!!
        self.assertEqual(response.status_code, 302)
        actual_parcel = parcel_models.Parcel.objects.get(pk=self.test_parcel.pk)
        self.assertEqual(actual_parcel.status, True)
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.locker.pk)
        self.assertEqual(actual_locker.status, True)
