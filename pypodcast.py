import sqlite3
import os.path

from config import PODCAST_DIR, SUBS_DIR

class Library(object):

	def __init__(self):
		self._init_subs()
		self.subscriptions = self._get_subscriptions()

	def _init_subs(self):
		""" Create subscriptions file if it doesn't exist."""
		if not os.path.exists(SUBS_DIR):
			os.makedirs(SUBS_DIR)
		path = os.path.join(SUBS_DIR, "subscriptions.txt")
		if not os.path.isfile(path):
			with open(path,'w') as subs:
				subs.write("")

	def _get_subscriptions(self):
		""" Get the user's subscriptions from the subscriptions file.
		Returns them as a list (of feed URLs).
		"""
		with open(os.path.join(SUBS_DIR, "subscriptions.txt"),'r') as subs:
			return [ sub for sub in subs.readlines() ]

	def list_subscriptions(self):
		""" List all subscriptions """
		pass
	
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

