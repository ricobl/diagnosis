
from models import Fail

class FailHandler(object):
    def failed(self, test_type, request, url):

        fail = Fail()

        fail.test_type = test_type
        fail.url = url
        fail.user = request.user

        group_list = []
        for group in request.user.groups.all():
            group_list.append(group.name)

        fail.group_list = str(" ,".join(group_list))

        fail.http_x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        fail.remote_addr = request.META.get('REMOTE_ADDR')
        fail.user_agent = request.META.get('HTTP_USER_AGENT')
        fail.save()