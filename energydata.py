#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
import urllib
import urllib2
import json

def get_json(url):
        """
        Helper function that requests a JSON response from the API and then parses it.
        :return: A dictionary with the values from the JSON response
        """
        response = urllib2.urlopen(url).read()
        json_data = json.loads(response)
        return json_data

def get_consumption():
    to_time = datetime.now()
    from_time = to_time - timedelta(seconds=10)
    url = 'http://192.168.6.54/middleware.php/data/' \
          '3133df40-d5b5-11e2-83cd-01e8204ee975.json?' \
          'from=%d&' \
          'to=%d' % (time.mktime(from_time.timetuple()) * 1000, time.mktime(to_time.timetuple()) * 1000)
    # print url
    data = get_json(url)
    # print data
    tuples = data[u'data'][u'tuples']
    current_watts = tuples[0][1]
    return current_watts


def main():
    while True:
        print('Current consumption: %s' % get_consumption())
        time.sleep(5)

if __name__ == '__main__':
    main()