from django.db import models

class URL(models.Model):
    address = models.CharField(max_length=500)
    ACCESS_TYPE_CHOICES = (
                            ('S', 'Server'),
                            ('B', 'Browser'),
                            ('*', 'Both'),
                          )
    access_type = models.CharField(max_length=1, choices=ACCESS_TYPE_CHOICES, default='S')

    created_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return "%s [%s]" % (self.address, self.access_type)

    class Meta:
            ordering = ["address", "access_type"]

