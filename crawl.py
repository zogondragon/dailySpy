# crawl.py : This script send the query to Google.
from google import search

if __name__ == '__main__':
	print("Hello World!")
	for url in search('testing the test', stop=10):
		print(url)
