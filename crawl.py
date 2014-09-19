# crawl.py : This script send the query to Google.
from google import search
import datetime

if __name__ == '__main__':
	# print datetime
	print(datetime.datetime.now())

	count = 0
	for url in search('북조선', stop=100):
		print(url)
		count += 1

	print(count)
