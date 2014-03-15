import sqlite3
import os.path
import urllib.request

from config import PODCAST_DIR, SUBS_DIR
from podcast import Podcast

class Library(object):

	def __init__(self, subs_dir=SUBS_DIR):
		self.subs_dir = subs_dir
		self._init_subs()
		self.podcasts = self._get_podcasts()

	def _init_subs(self):
		""" Create subscriptions file if it doesn't exist."""
		if not os.path.exists(self.subs_dir):
			os.makedirs(self.subs_dir)
		path = os.path.join(self.subs_dir, "subscriptions.txt")
		if not os.path.isfile(path):
			with open(path,'w') as subs:
				subs.write("")

	def _get_podcasts(self):
		""" Create a dict containing all information on the podcasts subscribed
		to.
		"""
		urls = self._get_urls()
		podcasts = {}
		for url in urls:
			if url in podcasts.keys():
				print(url + " exists more than once in your subscriptions list.")
			else:
				feed = self._get_feed(url)
				podcasts[url] = Podcast(feed)
		return podcasts


	def _get_urls(self):
		""" Get the user's subscriptions from the subscriptions file.
		Returns them as a list (of feed URLs).
		"""
		with open(os.path.join(self.subs_dir, "subscriptions.txt"),'r') as subs:
			return [ sub for sub in subs.readlines() ]

	def _get_feed(self, url):
		response = urllib.request.urlopen(url)
		return response.read()

	def list_subscriptions(self):
		""" List all subscriptions """
		for podcast in self.podcasts:
			print(podcast)
	
	# def add_subscription(self, url):
	# 	""" Add subscription from given url """
	# 	pass

	# def remove_subscription(self, podcast):
	# 	""" Remove subscription from given podcast"""
	# 	pass

	def refresh(self):
		""" Refresh all subscriptions """
		pass

	def fetch(self, podcast):
		""" Fetch all new episodes of given podcast. """
		pass

	def fetch_all(self):
		""" fetch all new episodes. """
		pass

