# TicTacToe
Assignment - TIC TAC TOE using Python Tkinter

It consists of three windows - 
1) Opening window - tic tac toe image and two buttons namely 'Play' - to go to the next window and 'Exit' to quit the game
2) Next window - To select the number of players as 1 or 2
3) Game board window - consists of player dashboard, quit button, and 9 buttons to play the game
4) Winner window - displays winner or tie

Users can play with another player or with the computer.

1. Playing with another player - Player 1 will take 'O' and player 2 will take 'X'. The turn of players will be displayed on the dashboard. Alternate chances will be given
to each player. The winner will be checked on each move after 3 moves and then the winner window appears to display the winner.

2. Playing with the computer - Player will take 'O' and computer will take 'X' in alternate chances. Computer move will be decided on the basis of the following steps:
				a. Check if computer can win in the next move by placing 'X' on the possible moves and return that move
				b. Check if player can win in the next move by placing 'O' on the possible moves and return that move
				c. Check the next two possible moves of computer if computer can win and return one of that move
				d. Check the next two possible moves of player if he can win return that move on the basis of the number of       winning moves available and blocking the place.
				e. Make center move if it is vacant
				f. Make any vacant corner move
				g. Make any vacant edge move

After following this algorithm, computer will never lose the game i.e. it will only be a tie or computer wins.

Chanchal Gadodia
