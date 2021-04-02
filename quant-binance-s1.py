#!/usr/local/bin/env python3
from binance.client import Client
import configparser
import collections
from flask import Flask
import logging
from operator import itemgetter
import pprint
import threading
import time

configFile = configparser.ConfigParser()
configFile.read('config.conf')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
#logging.basicConfig(filename="app.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
app.logger.info('Initialized.')

BINANCE_API_KEY = configFile['BINANCE']['API_KEY']
BINANCE_SECRET_KEY =configFile['BINANCE']['SECRET_KEY']
BINANCE_ENDPOINT = configFile['BINANCE']['ENDPOINT']

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
client.ping()
allPrices = client.get_all_tickers()
symbolList = list()
symbolList = sorted([ i['symbol'] for i in allPrices ])
buySignal = dict()
for i in symbolList:
    buySignal[i] = 0

def queryAllPrices(numbers, sleepTime):
    for i in range(numbers):
        print("Querying all price...")
        oldPrices = sorted(client.get_all_tickers(), key=itemgetter('symbol')) 
        time.sleep(sleepTime)
        newPrices = sorted(client.get_all_tickers(), key=itemgetter('symbol')) 
        for j, k in zip(oldPrices, newPrices):
            if (float(j['price']) - float(k['price'])) < 0:
                buySignal[j['symbol']] += 1
    for i,j in buySignal.items():
        if j>=4:
            print(i)


def printNumber(numbers):
    for i in range(numbers):
        print("Print number: ")
        print('Time: ', i)
        time.sleep(1)

t1 = threading.Thread(target=queryAllPrices, args=(5,1))
t2 = threading.Thread(target=printNumber, args=(5,))
# creating two threads here t1 & t2
t1.start()
t2.start()
# starting threads here parallel by using start function.
t1.join()
# this join() will wait until the cal_square() function is finished.
t2.join()
# this join() will wait unit the cal_cube() function is finished.
print("Successes!")