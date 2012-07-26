"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import mox
import httplib2
from ping import Ping


class PingTest(TestCase):
    def test_address_reachable(self):
        mx = mox.Mox()
        http_client = mx.CreateMock(httplib2.Http)
        http_client.request('http://globo.com', 'GET').AndReturn(({'status':'200'},'Mock Response'))
        mx.ReplayAll()

        ping = Ping()
        self.assertTrue(ping.isReachable("http://globo.com", http_client))

        mx.UnsetStubs()
        mx.VerifyAll()

    def test_address_unreachable(self):
        mx = mox.Mox()
        http_client = mx.CreateMock(httplib2.Http)
        http_client.request('http://www.enderecoquenaoexiste.com', 'GET').AndRaise(httplib2.ServerNotFoundError)
        mx.ReplayAll()

        ping = Ping()
        self.assertFalse(ping.isReachable("http://www.enderecoquenaoexiste.com", http_client))

        mx.UnsetStubs()
        mx.VerifyAll()