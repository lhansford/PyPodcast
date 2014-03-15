class Subscription(object):

	def __init__(self):
		self.refresh()

	def refresh(self):
		""" Refresh subscription """
		pass

	def mark_listened(self, name):
		""" Mark given episode as read. Confimr if string matches more than 1 """
		pass

	def mark_unlistened(self, name):
		""" Mark given episode as unread. Confimr if string matches more than 1 """
		pass

	def mark_all_listened(self):
		""" Mark all episodes as read"""
		pass

	def mark_all_unlistened(self):
		""" Mark all episodes as unread."""
		pass

	def fetch(self,name):
		""" Fetch given episode. """
		pass

	def fetch_all(self):
		""" Fetch all episodes. """
		pass

	def get_episodes(self):
		""" List all episodes. """
		pass

	def get_info(self):
		""" Get description of podcast. """
		pass
