#!/usr/bin/python3

# Use Python 3.5.2
import requests
import json

API_KEY = '293c18a028b72c4204b8d73d384c9a96f84a515ca8a6a44b582da963ecbd42fa'
API_URL = 'https://min-api.cryptocompare.com/data'
CRYPTOS = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'MANA', 'GNT', 'BAT']
USD = 'USD'

class CryptoProject():
	def __init__(self):
		self.btc_data  = ''
		self.eth_data  = ''
		self.xrp_data  = ''
		self.ltc_data  = ''
		self.bch_data  = ''
		self.mana_data = ''
		self.gnt_data  = ''
		self.bat_data  = ''

	def main(self):
		btc = self.get_price_hourly(CRYPTOS[0], 2000, 1558917827)
		self.btc_data = btc['Data']
		eth = self.get_price_hourly(CRYPTOS[1], 2000, 1558917827)
		self.eth_data = eth['Data']
		xrp = self.get_price_hourly(CRYPTOS[2], 2000, 1558917827)
		self.xrp_data = xrp['Data']
		ltc = self.get_price_hourly(CRYPTOS[3], 2000, 1558917827)
		self.ltc_data = ltc['Data']
		bch = self.get_price_hourly(CRYPTOS[4], 2000, 1558917827)
		self.bch_data = bch['Data']
		mana = self.get_price_hourly(CRYPTOS[5], 2000, 1558917827)
		self.mana_data = mana['Data']
		gnt = self.get_price_hourly(CRYPTOS[6], 2000, 1558917827)
		self.gnt_data = gnt['Data']
		bat = self.get_price_hourly(CRYPTOS[7], 2000, 1558917827)
		self.bat_data = bat['Data']
		self.file_writer('test')

	def file_writer(self, filename):
		fo = open("{}.txt".format(filename), "w")
		header = 'time,'
		for crypto in CRYPTOS:
			t = '{0},'.format(crypto.lower())
			header += t
		header = header[:-1] + '\n'
		# fo.write( header )
		for i in list(range(2000)):
			fo.write("{},".format(self.btc_data[i]['time']))
			fo.write("{},".format(self.btc_data[i]['close']))
			fo.write("{},".format(self.eth_data[i]['close']))
			fo.write("{},".format(self.xrp_data[i]['close']))
			fo.write("{},".format(self.ltc_data[i]['close']))
			fo.write("{},".format(self.bch_data[i]['close']))
			fo.write("{},".format(self.mana_data[i]['close']))
			fo.write("{},".format(self.gnt_data[i]['close']))
			fo.write("{}\n".format(self.bat_data[i]['close']))
		fo.close()

	def get_price_hourly(self, fsym, limit, toTs):
		r = requests.get('{}/histohour?fsym={}&tsym={}&limit={}&toTs={}&api_key={}'.format(API_URL, fsym, USD, limit, toTs, API_KEY))
		return r.json()

if __name__ == '__main__':
	cp = CryptoProject()
	cp.main()
