#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver

URL = 'http://www.acapela-group.com/demo-tts/DemoHTML5Form_V2.php'

class YodaSpeech(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def speak(self, text):
        self.driver.get(URL)
        select = self.driver.find_element_by_name("MySelectedVoice")
        all_options = select.find_elements_by_tag_name("option")

        for option in all_options:
            value =  option.get_attribute("value")
            #print "Value is: %s" % value
            if value == 'WillLittleCreature':
                option.click()

        textfield = self.driver.find_element_by_name("MyTextForTTS")
        textfield.send_keys(text)

        self.driver.find_element_by_id("listen").click()


