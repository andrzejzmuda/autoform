from django.db import models


class Processor(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=250)

    class Meta:
        app_label = 'autoform'
        verbose_name_plural = 'Processors'

    def __str__(self):
        return '%s %s' % (self.name, self.lastname)

class Actions(models.Model):
    action = models.CharField(max_length=50)

    class Meta:
        app_label = 'autoform'
        verbose_name_plural = 'Actions'

    def __str__(self):
        return self.action


class Operations(models.Model):
    operation = models.CharField(max_length=250)
    details = models.TextField()

    class Meta:
        app_label = 'autoform'
        verbose_name_plural = 'Operations'

    def __str__(self):
        return '%s %s' % (self.operation, self.details)


class Authorisations(models.Model):
    actions = models.ManyToManyField(Actions)
    operation = models.ForeignKey(
        Operations,
        on_delete=models.CASCADE
        )
    processor = models.ForeignKey(
        Processor,
        on_delete=models.SET_NULL,
        null=True
        )

    class Meta:
        app_label = 'autoform'
        verbose_name_plural = 'Authorisations'

    def __str__(self):
        return '%s %s %s' % (self.actions, self.operation, self.processor)