import lxml.html

import urllib
import urllib2

def get_html(url):
    return unicode(urllib.urlopen(url).read(),'shift-jis')

def get_trade_data():
    url = 'http://www.jsgoal.jp/special/2013move/?c=j1'
    dom = lxml.html.fromstring(get_html(url))
    for e in dom.xpath('//div[@class="field"]'):
        for i in e.xpath('//img'):
            print i.attrib['alt']
            break


if __name__ == '__main__':
    get_trade_data()

