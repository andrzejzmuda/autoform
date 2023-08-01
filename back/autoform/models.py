from django.db import models

class Actions(models.Model):
    action = models.CharField(max_length=50)

    def __str__(self):
        return self.action


class Operations(models.Model):
    operation = models.CharField(max_length=250)
    details = models.TextField()

    def __str__(self):
        return '%s %s' % (self.operation, self.details)


class Authorisations(models.Model):
    actions = models.ManyToManyField(Actions)
    operation = models.ForeignKey(
        Operations,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return '%s %s' % (self.actions, self.operation)