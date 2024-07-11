from django.contrib import admin

# Register your models here.
from post_machine.models import PostMachine, Locker

admin.site.register(PostMachine)
admin.site.register(Locker)



