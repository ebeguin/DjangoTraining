from django.http import Http404

class Post():
	POSTS=[
		{'id':'1', 'title': 'first post', 'body' : 'my 1st post'},
		{'id':'2', 'title': 'second post', 'body' : 'my 2nd post'},
		{'id':'3', 'title': 'third post', 'body' : 'my 3rd post'},
	]

	@classmethod
	def all(cls):
		return cls.POSTS

	@classmethod
	def find(cls, id):
		try:
			return cls.POSTS[int(id)-1]
		except:
			raise Http404('Erreur 404 - post {} not found'.format(id))
