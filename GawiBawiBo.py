import random

"""
* Traditional gawi-bawi-bo game

@author Joeng Um Lee
@created 12-10-2016
@modified in 25-10-2016
"""

# 0 : gawi, 1. bawi, 2 : bo

def determine_winner(my_hand, com_hand, won):
	"""
	Determine winner of the game.
	:param my_hand : my hand parameter
	:param com_hand : predefined computer choice
	:return None : None is returned. (void)
	"""

	if com_hand == 0:
		print "Computer was gawi."
	elif com_hand == 1:
		print "Computer was bawi."
	else:
		print "Computer was bo."
		
	a = my_hand - com_hand
	if a > 0 or a == -2:
		print "You win"
		won += 1
		return won
	elif a == 0:
		print "Draw"
		return won
	else:
		print "You lose"
		return won

if __name__ == '__main__':
	""" Comment """
	com_hand = random.randint(0, 2)
	win_count = 0
	count = 0
	while not(count == 5):
		print "Show your hand (0 : gawi, 1 : bawi, 2 : bo)"
		my_hand = int(raw_input())
		win_count = determine_winner(my_hand, com_hand, win_count)
		print "Play More? (O/X) : "
		if(raw_input() == 'X'):
			break
		else:
			count += 1
			continue
	print "you've won for " + str(win_count) + "!";