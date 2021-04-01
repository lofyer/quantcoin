#!/usr/local/bin/env python3
import configparser
import logging
from flask import Flask
from binanceApiWrapper.binanceApiWrapper import binanceApi

configFile = configparser.ConfigParser()
configFile.read('config.conf')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
#logging.basicConfig(filename="app.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
app.logger.info('Initialized.')

BINANCE_API_KEY = configFile['BINANCE']['API_KEY']
BINANCE_SECRET_KEY =configFile['BINANCE']['SECRET_KEY']
BINANCE_ENDPOINT = configFile['BINANCE']['ENDPOINT']

quantBinance = binanceApi(api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY, endpoint=BINANCE_ENDPOINT)
quantBinanceStatus, quantBinanceLatency = quantBinance.systemStatus()
if quantBinanceStatus == 0:
    app.logger.info('Binance API endpoint %s is alive with latency %.3f seconds' % (BINANCE_ENDPOINT, quantBinanceLatency))
else:
    app.logger.error('Binance API endpoint %s connection failed.' % (BINANCE_ENDPOINT))