import praw
from jinja2 import Environment, PackageLoader

class RedditScraper(object):
	def __init__(self, redditObj, fav_subs):
		self.r = redditObj
		self.fav_subs = fav_subs
	def create_object(self):
		data = {}
		for fav_sub in self.fav_subs:
			sub = self.get_subreddit_submissions(fav_sub)
			data[fav_sub] = [self.extract_data(s) for s in sub]
		return data
	def get_subreddit_submissions(self, name, limit=10):
		""" Returns a generator of the top submissions in a subreddit """
		return r.get_subreddit(name).get_top(limit=limit)
	def extract_data(self, sub):
		""" Given a submission, this method returns the title, url, and some comments associated with that submission """
		return (sub.title, sub.url)  # need to figure out a way to process comments


class EmailSubmissions(object):
	def __init__(self, data, email):
		self.data = data
		self.email = email
	def render():
		""" Renders a jinja2 html template, so it can be emailed to the user """

r = praw.Reddit(user_agent='subreddit-email')
fav_subs = ['python', 'javascript', 'cscareerquestions', 'node']

reddit = RedditScraper(r, fav_subs)
print(reddit.create_object())
