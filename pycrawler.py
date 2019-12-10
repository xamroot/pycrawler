import os
import requests
import sys
import queue
import threading
import argparse

# parse command line
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Target url to crawl")
parser.add_argument("wordlist_filename", nargs='?', help="Wordlist file to use, default is wordlist.txt")
parser.add_argument("-t", "--threads", help="Number of threads to spin up, default is 10", type=int)
args = vars(parser.parse_args())

# set up word list from provided file
def create_wordlist(wordlist):
	f = open(wordlist)
	words = queue.Queue()
	for word in f:
		word = word.rstrip('\n')
		words.put(word)
	f.close()
	return words

# brute force driver
def bruteforce_dirs(word_queue, url):
	while not word_queue.empty():
		new_word = word_queue.get()
		attempt_list = []

		'''
		if "." not in new_word:
			attempt_list.append("/{}/".format(new_word))
		else:
			attempt_list.append("/{}".format(new_word))'''
		attempt_list.append("/{}/".format(new_word))


		for attempt in attempt_list:
			target = url + attempt # craft target url
			try:
				res = requests.get(target)

				if res.status_code == 200:
					if "Rejected" not in res.text and "logged" not in res.text:
						print("FOUND: {}".format(target))
			except KeyboardInterrupt:
				print("Exiting...")
				sys.exit()
			except:
				print("{} Error".format(target))
				pass

# driver
def main():
	# get cmd args
	url = args['url']
	threads = args['threads']
	wordlist_file = args['wordlist_filename']
	
	# handle any needed default values
	if (threads == None):
		threads = 10
	if (wordlist_file == None):
		wordlist_file = "svndigger_all.txt"

	wordlist = create_wordlist(wordlist_file)
	for i in range(int(threads)):
		thread = threading.Thread(target=bruteforce_dirs, args=(wordlist, url,))
		thread.start()

main()