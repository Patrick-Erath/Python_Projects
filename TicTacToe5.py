import itertools

def win(current_game):
	# Horizontal Victories
	for row in game:
		# Is occurence of element at x[0] the same as the length of the list?
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} is the winner horizontally (-)!")
			return True

	# Column Victories
	check = []
	for col in range(len(game)):
		for row in game:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] != 0:
			print(f"Player {check[0]} is the winner diagonally (|) !")
			return True

	# Diagonal Victories
	diags = []
	for index in range(len(game)):
		diags.append(game[index][index])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player {diags[0]} is the winner diagonally  (\\) !")
		return True

	# Vertical Victories
	diags = []
	rows = range(len(game))
	cols = reversed(range(len(game)))
	for col, row in zip(cols, rows):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player {diags[0]} is the winner vertically (/) !")
		return True

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This poisition has already been taken!")
			return game_map, False
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("Error Message", e)
		return game_map, False
	except Exception as e:
		print("Did you input the row/column as 0, 1 or 2?")
		return game_map, False


play = True
players = [1, 2] 
while play:
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]

	game_won = False
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player=next(player_choice)
		print(f"Current Player: {current_player}")
		played = False

		while not played and game_won == False:
			column_choice = int(input("What column do you want to play? (0, 1, 2) "))
			row_choice = int(input("What row do you want to play? (0, 1, 2) "))
			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n)")
			if again.lower() == "y":
				print("Restarting ... ")
			else:
				print("See you next time! :)")
				play = False


