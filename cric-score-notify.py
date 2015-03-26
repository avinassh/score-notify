#!/usr/bin/env python

import os
import sys
import argparse
from time import sleep

import requests
from bs4 import BeautifulSoup
from pync import Notifier

from settings import cric_info_api
from settings import cric_info_api_with_proxy

# This script relies on Cricinfo RSS Live Feed (http://static.cricinfo.com/rss/livescores.xml)

parser = argparse.ArgumentParser(description="This script fetches score from Cric Info (using RSS feed) and displays as notification. This script currently works for OS X only.")
parser.add_argument('-f','--frequency', type=int, default=15, help='This setting specifies how often script should check for score. Provide fetch frequency in seconds.', 
                    required=False)
parser.add_argument('-p','--proxy', type=bool, default=False, help='This setting specifies whether to use proxy server to fetch data or not. ', 
                    required=False)
options = vars(parser.parse_args())

fetch_frequency = options['frequency']
use_proxy = options['proxy']


def notify(text):
	Notifier.notify(text)


def fetch_score_data():
	if use_proxy:
		url = cric_info_api_with_proxy
	else:
		url = cric_info_api

	score_data_raw = requests.get(url)
	score_data_soup = BeautifulSoup(score_data_raw.text)
	score_data = score_data_soup.find_all('description')

	if len(score_data) < 2:
		print('\n\nLooks like no matches are live. Script is exiting!\n\n')
		sys.exit()

	return score_data	


def main():
	old_score = None
	score_data = fetch_score_data()
	print('\nFollowing live scores are available now:\n')
	# the first element is always 
	# <description>Latest scores from Cricinfo</description>
	for i, game in enumerate(score_data[1:], 1): 
		print(i, game.text)

	game_indentifier = int(input('\n\nEnter your choice: '))

	if game_indentifier >= len(score_data) or game_indentifier < 1:
		print('\nErr, wrong choice. I am exiting')
		sys.exit()

	print ('\n\nGreat! I will keep displaying the scores now for every %s seconds. And proxy set is to %s.\n\n' % (fetch_frequency, use_proxy))

	while True:
		score_data = fetch_score_data()
		score = score_data[game_indentifier].text
		if score != old_score:
			old_score = score
			notify(score)
		sleep(fetch_frequency)
		#break


if __name__ == '__main__':
	main()