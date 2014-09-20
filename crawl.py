# crawl.py : This script send the query to Google and save the result as a log file.
from google import search
import datetime

if __name__ == '__main__':
	filename = str(datetime.datetime.now()) + '.log'
	#print(datetime.datetime.now())

	logfile = open('logs/' + filename, 'a')

	count = 0
	for url in search('북조선', stop=100):
		#print(url)
		logfile.write(url + '\n')
		count += 1

	#print(count)
	logfile.write(str(count) + '\n')

