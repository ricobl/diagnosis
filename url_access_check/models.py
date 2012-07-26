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
        return self.address

    class Meta:
            ordering = ["address", "access_type"]


class Fail(models.Model):
    url = models.ForeignKey('URL')

    TEST_TYPE_CHOICES = (('S', 'Server'), ('B', 'Browser'))
    test_type = models.CharField(max_length=1, choices=TEST_TYPE_CHOICES)

    when = models.DateTimeField(auto_now_add = True)

    #access data
    user = models.CharField(max_length=255, blank=True, null=True)
    group_list = models.TextField(blank=True, null=True)

    http_x_forwarded_for = models.CharField(max_length=255, blank=True, null=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "%s [%s]" % (self.url.address, self.test_type)

