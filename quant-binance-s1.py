#!/usr/local/bin/env python3
import configparser
import logging
from flask import Flask
from binanceApiWrapper.binanceApiWrapper import binanceApi

configFile = configparser.ConfigParser()
configFile.read('config.conf')

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.logger.info('Initialized.')

BINANCE_API_KEY = configFile['BINANCE']['API_KEY']
BINANCE_SECRET_KEY =configFile['BINANCE']['SECRET_KEY']
BINANCE_ENDPOINT = configFile['BINANCE']['ENDPOINT']

quantBinance = binanceApi(api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY, endpoint=BINANCE_ENDPOINT)
if quantBinance.systemStatus() == 0:
    app.logger.info('Binance API endpoint %s is alive with latency %s' % (str(BINANCE_ENDPOINT), str(quantBinance.endpointLatency())))