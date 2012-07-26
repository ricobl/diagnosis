import logging
import httplib2

class Ping(object):
    def isReachable(self, address, http_client=None):
        if not http_client:
            http_client = self.__create_http_client()
         
        try:   
            resp, content = http_client.request(address, "GET")
            logging.debug("%s [%s]" % (address, resp['status']))
            return True
        except httplib2.ServerNotFoundError:
            logging.debug("%s [ServerNotFoundError]" % address)
            return False
        
    def __create_http_client(self):
        logging.debug("will create a new httplib2.Http")
        return httplib2.Http(cache=False, timeout=10)