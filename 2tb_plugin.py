# -*- coding: utf-8 -*-

import irc3
from irc3.plugins.command import command
import re
import requests
import time

@irc3.event(irc3.rfc.JOIN)
def lookup_2tb(bot, mask, channel, **kwargs):
    reg = re.compile(r'<span>.*?\$(.*?)<\/span>', re.M)

    while 1:
        text = requests.get('http://stores.ebay.com/newegg/_i.html?_nkw=hitachi+2tb').text
        found = reg.findall(text)

        for price in found:
            if float(price) < 45:
                bot.privmsg(channel, "HEY pew get that hdd u fuk; it\'s {}".format(price))

        time.sleep(5 * 60)
