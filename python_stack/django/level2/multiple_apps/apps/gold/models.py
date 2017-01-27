from __future__ import unicode_literals

from django.db import models

from ..user_management.models import User

# Create your models here.
class LeaderboardManager(models.Manager):
	def save_game(self, data):
		score = int(data['score'])
		user_id = int(data['user_id'])
		#try pulling a user
		try:
			cur_user = User.objects.get(id=user_id)
			#try pulling their board
			try:
				board = self.get(user=cur_user)
				print "got board"
				if board.top_score < score:
					board.top_score = score
				board.games_played += 1
				board.total_gold_earned += score
				board.save()
			#if there is no board
			except:
				print "making new board"
				board = self.create(
					user = cur_user,
					top_score = score,
					games_played = 1,
					total_gold_earned = score,
				)
				print "New Board!!!"
			return "Your top score is {}!".format(board.top_score)
		except:
			return "Oops, it looks like there's no user by your name!"

class Leaderboard(models.Model):
	user = models.OneToOneField(User)
	top_score = models.IntegerField()
	games_played = models.IntegerField()
	total_gold_earned = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = LeaderboardManager()