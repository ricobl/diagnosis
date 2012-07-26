#!/usr/bin/env python                                                                                                                                                                
#-*- coding:utf-8 -*-

from django.template.response import TemplateResponse
from django.views.generic.base import View


from models import URL

from ping import Ping

class ManualURLCheck(View):

    def get(self, request):

        print "USER [%s]" % request.user
        print "HTTP_X_FORWARDED_FOR [%s]" % request.META.get('HTTP_X_FORWARDED_FOR')
        print "REMOTE_ADDR [%s]" % request.META.get('REMOTE_ADDR')
        print "GRUPS:"
        for group in request.user.groups.all():
            print "\tGROUP [%s]" % group.name


        urls_browser = URL.objects.filter(access_type__in=["*","B"])
        urls_server  = URL.objects.filter(access_type__in=["*","S"])

        tested_addresses = []

        ping = Ping()
        for url in urls_server:
            tested_addresses.append({
                                     'address': url.address,
                                     'reachable': ping.isReachable(url.address)
                                    })

        context = {
                    'tested_addresses': tested_addresses,
                    'urls_browser': urls_browser
                  }

        return TemplateResponse(request, 'check/manual_check.html', context=context)


class ServerURLCheck(View):

    def get(self, request):

        print "HTTP_X_FORWARDED_FOR [%s]" % request.META.get('HTTP_X_FORWARDED_FOR')
        print "REMOTE_ADDR [%s]" % request.META.get('REMOTE_ADDR')

        urls_server  = URL.objects.filter(access_type__in=["*","S"])

        tested_addresses = []

        ping = Ping()
        for url in urls_server:
            tested_addresses.append({
                'address': url.address,
                'reachable': ping.isReachable(url.address)
            })

        context = {
            'tested_addresses': tested_addresses
        }

        return TemplateResponse(request, 'check/server_check.html', context=context)