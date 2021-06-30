from django.db import models

# Create your models here.

class Logger(models.Model):

    primary      = models.AutoField(primary_key=True)
    message      = models.TextField(default='No Log Message')
    date         = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.primary

    class Meta:
        ordering = ('primary',)
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return str('{0} : {1} : {2}'.format(self.primary, self.message, self.date))

