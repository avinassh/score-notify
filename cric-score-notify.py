#!/usr/bin/env python

import os
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup
from pync import Notifier

# This script relies on Cricinfo RSS Live Feed (http://static.cricinfo.com/rss/livescores.xml)

cric_info_api = "http://static.cricinfo.com/rss/livescores.xml"

while True:
	score_data_raw = requests.get(cric_info_api)
	score_data_soup = BeautifulSoup(score_data_raw.text)

	data = score_data_soup.find_all("description")

	if len(data) < 2:
		print("Looks like no matches are live. Script is exiting!")
		sys.exit()

	print("Following live scores are available now")
	# the first element is always 
	# <description>Latest scores from Cricinfo</description>
	for i, match in enumerate(data[1:]): 
		print(match)
	break
