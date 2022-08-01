from django.db import models


class Hour(models.Model):
    hour = models.CharField(max_length=50)

    def __str__(self):
        return self.hour


class Phone(models.Model):
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class User(models.Model):
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    key_phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='key_phone')
    key_hour = models.ForeignKey(Hour, on_delete=models.CASCADE, related_name='key_hour')

    def __str__(self):
        return f'{self.phone} - {self.name}'


class Mailing(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    user = models.ManyToManyField(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.description[:20]}'


class Message(models.Model):
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} message - {self.date}'

