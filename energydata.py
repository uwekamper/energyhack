#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
import urllib
import urllib2
import json

from speak import YodaSpeech
from energyserial import Yoda # you must

def get_json(url):
        """
        Helper function that requests a JSON response from the API and then parses it.
        :return: A dictionary with the values from the JSON response
        """
        response = urllib2.urlopen(url).read()
        json_data = json.loads(response)
        return json_data

def get_consumption():
    url = ''
    data = {}
    try:
        to_time = datetime.now() - timedelta(seconds=1)
        from_time = to_time - timedelta(minutes=5)
        url = 'http://192.168.6.54/middleware.php/data/' \
              '3133df40-d5b5-11e2-83cd-01e8204ee975.json?' \
              'from=%d&' \
              'to=%d' % (time.mktime(from_time.timetuple()) * 1000, time.mktime(to_time.timetuple()) * 1000)
        # print url
        data = get_json(url)
        # print data
        raw_tuples = data[u'data'][u'tuples']
        tuples = raw_tuples[-3:]
        current_watts = sum([x[1] for x in tuples]) / len(tuples)
        print tuples
        return current_watts
    except Exception, e:
        print "ERROR"
        print 'URL:', url
        print 'Data:', data
        raise e


def set_yoda(yoda, watts):
    if watts <= 10:
        yoda.set_bubble(0)
        yoda.set_rgb(0,255,0)
        return

    if watts <= 100:
        yoda.set_bubble(60)
        yoda.set_rgb(0,0,0)
        return

    if watts <= 200:
        yoda.set_bubble(100)
        yoda.set_rgb(200,200,0)
        return

    if watts >= 500:
        yoda.set_bubble(255)
        yoda.set_rgb(255,0,0)
        return

    if watts >= 999:
        yoda.set_bubble(255)
        yoda.set_rgb(255,255,255)
        return

def main():
    yoda = Yoda(serial_port='/dev/tty.usbmodem411')
    speech = YodaSpeech()
    old_watts = 0
    while True:
        watts = get_consumption()
        text = '%d Watts you consume.' % watts
        print "Text: %s" % text
        if watts >= 900 and watts <= 1200:
            text += ' Save energy you must, young padawan.'
        elif watts > 1200:
            text += ' Consuming this much energy the path to the dark side is.'
        set_yoda(yoda, watts)

        diff = abs(old_watts - watts)
        if diff > 20:
            print "diff is %s, speaking" % diff
            speech.speak(text)

        old_watts = watts
        time.sleep(15)



if __name__ == '__main__':
    main()
