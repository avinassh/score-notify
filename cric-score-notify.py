#!/usr/bin/env python

import os
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup
from pync import Notifier

# This script relies on Cricinfo RSS Live Feed (http://static.cricinfo.com/rss/livescores.xml)

cric_info_api = 'http://static.cricinfo.com/rss/livescores.xml'

def notify(text):
	Notifier.notify(text)


def fetch_score_data():
	score_data_raw = requests.get(cric_info_api)
	score_data_soup = BeautifulSoup(score_data_raw.text)
	score_data = score_data_soup.find_all('description')

	if len(score_data) < 2:
		print('Looks like no matches are live. Script is exiting!')
		sys.exit()

	return score_data	

def main():
	old_score = None
	score_data = fetch_score_data()
	print('Following live scores are available now')
	# the first element is always 
	# <description>Latest scores from Cricinfo</description>
	for i, game in enumerate(score_data[1:], 1): 
		print(i, game.text)

	game_indentifier = int(input('Enter your choice: '))

	if game_indentifier >= len(score_data) or game_indentifier < 1:
		print('Err, wrong choice. I am exiting')
		sys.exit()

	while True:
		score_data = fetch_score_data()
		score = score_data[game_indentifier].text
		if score != old_score:
			old_score = score
			notify(score)
		sleep(5)
		#break

if __name__ == '__main__':
	main()