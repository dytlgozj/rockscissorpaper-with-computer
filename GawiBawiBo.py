import random

"""
* Traditional gawi-bawi-bo game

@author Joeng Um Lee
@created 12-10-2016
"""

# 0 : gawi, 1. bawi, 2 : bo

def determine_winner(my_hand, com_hand):
	"""
	Determine winner of the game.
	:param my_hand : my hand parameter
	:param com_hand : predefined computer choice
	:return None : None is returned. (void)
	"""
	a = my_hand - com_hand
	if a > 0 or a == -2:
		print "You win"
	elif a == 0:
		print "Draw"
	else:
		print "You lose"

if __name__ == '__main__':
	""" Comment """
	com_hand = random.randint(0, 2)

	print "Show your hand (0 : gawi, 1 : bawi, 2 : bo)"
	my_hand = int(raw_input())
	determine_winner(my_hand, com_hand)