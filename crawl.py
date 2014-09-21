# crawl.py : This script send the query to Google and save the result as a log file.
from google import search
import datetime
import time


def GoogleAKeyword(queryString, outputFile):
	"Send a string to Google.com and log the result as a file. Default stop=100."
	outputFile.write("==Search keyword: " + queryString + "==\n")
	print("==Search keyword: " + queryString + "==")

	count = 0
	for url in search(queryString, stop=100, pause=5.0):
		print(url)
		outputFile.write(url + '\n')
		count += 1

	print(count)
	outputFile.write(str(count) + '\n')




if __name__ == '__main__':
	logfilename = str(datetime.datetime.now()) + '.log'
	#print(datetime.datetime.now())

	logfile = open('logs/' + logfilename, 'a')

	keywordFile = open('keyword.list', 'r')
	for line in keywordFile:
		GoogleAKeyword(line.rstrip('\n'), logfile)
		time.sleep(60) # delays for 60 seconds -- to circumvent Google's blocking.

