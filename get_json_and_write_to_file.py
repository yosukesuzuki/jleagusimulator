# -*- coding: utf-8 -*-
import logging
import datetime
import base64
import urllib
import urllib2

def get_json_and_write_file():
    url = 'http://jleaguefoot.appspot.com/v/trade/data/' 
    opener = urllib2.build_opener()
    fetch_result = opener.open(url).read()
    out_file = open('./media/trade_data.json','w')
    out_file.write(fetch_result)
    out_file.close()

if __name__ == '__main__':
    get_json_and_write_file() 
