import moira
import requests
import json
import sys
import time
import getpass
import datetime
import pickle

class clr:
    black = '\033[30m'
    red = '\033[31m'
    dullgreen = '\033[32m'
    dullyellow = '\033[33m'
    brown = '\033[34m'
    peach = '\033[35m'
    pink = '\033[36m'
    peach2 = '\033[37m'
    dullred = '\033[1;31m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'
    blue = '\033[1;34m'
    fuchsia = '\033[1;35m'
    goldenrod = '\033[1;36m'
    white = '\033[1;37m'
    end = '\033[0m'
    def disable(self):
		self.black = ''
		self.red = ''
		self.dullgreen = ''
		self.dullyellow = ''
		self.brown = ''
		self.peach = ''
		self.pink = ''
		self.peach2 = ''
		self.dullred = ''
		self.green = ''
		self.yellow = ''
		self.blue = ''
		self.fucshia = ''
		self.goldenrod = ''
		self.white = ''
		self.end = ''

username = '________'
password = '________'
game = 'intro-to-business-spring-2015'
ticker = 'UWTI'
stock = 'EXCHANGETRADEDNOTE-XASQ-UWTI'
amount = 300000
outputfmt = clr.pink + '%(time)s' + clr.peach + ' $%(price)s' + clr.end
timefmt = '{:%Y-%m-%d %H:%M:' + clr.dullyellow + '%S}'
token = moira.get_token(username, password)

def get_google():
    r2 = requests.get('http://finance.google.com/finance/info', params={'q': ticker})
    
    #r['time'] = clr.pink + timefmt.format(r['time'])
    j = json.loads(r2.text.replace('\n','').replace('/','').replace('[','').replace(']',''))
    #print r2.headers['date'], float(j['l_cur']), outputfmt % r
    #time.sleep(.05)
    
    return float(j['l_cur'])

def get_mw():
    r = moira.stock_search(token, game, ticker)
    return float('%(price)f' % r)

while 1:
    mw = get_mw()
    google = get_google()
    if google > 4: google = google/100
    print mw, google
    
    if (google - mw) >= 0.006:
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        moira.order(token, game, 'Buy', stock, amount)
        while 1:
            mw2 = get_mw()
            print mw2
            if (mw2 - mw)*amount*10 >= 5000: break
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
        moira.order(token, game, 'Sell', stock, amount)
    if (mw - google) >= 0.006:
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        moira.order(token, game, 'Short', stock, amount)
        while 1:
            mw2 = get_mw()
            print mw2
            if (mw - mw2)*amount*10 >= 5000: break
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
        moira.order(token, game, 'Cover', stock, amount)
