#!/usr/bin/env python                                                                                                                                                                
#-*- coding:utf-8 -*-

from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.http import HttpResponse

from url_access_check.models import URL, Fail
from url_access_check.fail_handler import FailHandler

from url_access_check.ping import Ping

class ManualURLCheck(View):

    def get(self, request):
        urls_browser = URL.objects.filter(access_type__in=["*","B"])
        urls_server  = URL.objects.filter(access_type__in=["*","S"])

        tested_addresses = []

        ping = Ping()
        for url in urls_server:
            reachable = ping.isReachable(url.address)

            tested_addresses.append({
                                     'address': url.address,
                                     'reachable': reachable
                                    })

            if not reachable:
                FailHandler().failed('S', request, url)

        context = {
                    'tested_addresses': tested_addresses,
                    'urls_browser': urls_browser
                  }

        return TemplateResponse(request, 'url_access_check/manual_check.html', context=context)

class RandomClientURLCheck(View):

    def get(self, request):
        urls_browser = URL.objects.filter(access_type__in=["*","B"]).order_by('?')[:3]

        context = {
            'urls_browser': urls_browser
        }

        return TemplateResponse(request, 'url_access_check/random_check.js', context=context)


class ServerURLCheck(View):

    def get(self, request):

        urls_server  = URL.objects.filter(access_type__in=["*","S"])

        tested_addresses = []

        ping = Ping()
        for url in urls_server:
            reachable = ping.isReachable(url.address)
            tested_addresses.append({
                'address': url.address,
                'reachable': reachable
            })

            if not reachable:
                FailHandler().failed('S', request, url)


        context = {
            'tested_addresses': tested_addresses
        }

        return TemplateResponse(request, 'url_access_check/server_check.html', context=context)


class Failed(View):
    def post(self, request):


        try:
            url = URL.objects.get(pk=request.POST.get("url_id"))

            FailHandler().failed('B', request, url)

            return HttpResponse(u'DONE', mimetype='text/plain', status=200)
        except URL.DoesNotExist:
            return HttpResponse(u'ERROR URL not registered at diagnosis', mimetype='text/plain', status=404)

        except Exception, err:
            return HttpResponse(u'ERROR %s' % err.message, mimetype='text/plain', status=500)

    def get(self, request):

        fails = Fail.objects.count()

        if not fails:
            return HttpResponse(u'NONE', mimetype='text/plain', status=200)
        else:
            return HttpResponse(u'%d FAILS' % fails, mimetype='text/plain', status=500)
