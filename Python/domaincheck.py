#
# Domain Availability Checker
#
# By Elver Loho <elver.loho@gmail.com>
# Released either under the BSD or the MIT license. Whatever. You decide.
#
# This code uses undocumented Gandi.net AJAX APIs, because their official
# XML-RPC APIs are broken. Hopefully this code will get their attention and
# motivate them to repair their official API.
#
# Use at your own risk.

import json
import httplib
import urllib

from time import sleep

def is_domain_available(domain, attempts = 10, sleep_between_checks = 0.1):
    for x in range(attempts):
        data = urllib.urlencode({"domains[]" : domain})
        
        headers = {"Referer" : "https://www.gandi.net/domain/buy/result/",
                   "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10",
                   "Accept-Language" : "en-us,en;q=0.5",
                   "Accept-Charset" : "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                   "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "X-Requested-With" : "XMLHttpRequest",
                   "Accept" : "application/json, text/javascript, */*"}
        
        connection = httplib.HTTPSConnection("www.gandi.net", timeout=60)
        connection.request("POST", "/ajax/domain_search", data, headers)
        response = connection.getresponse()
        json_obj = json.loads(response.read())
        if json_obj[domain] == "available":
            return True
        if json_obj[domain].startswith("unavailable"):
            return False
        if json_obj[domain] == "pending":
            if(sleep_between_checks):
                sleep(sleep_between_checks)
            continue
        else:
            raise Exception("Unknown status: %s" % json_obj)
    raise Exception("Ran out of attempts!")

def test():
    domains = ["whatever.com", "asdafafkjl.com", "google.com", "asffjksd.com"]
    for domain in domains:
        print domain, is_domain_available(domain)

if __name__ == "__main__":
    test()