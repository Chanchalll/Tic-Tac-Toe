# Chanchal Gadodia 

#Assignment - TIC TAC TOE game using Python Tkinter

#For detailed explanation please read TicTacToe.txt

#All the images used in this code have been uploaded in images folder

#Importing all necessary libraries
import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial

#Creating empty board
global board
board = [[" " for x in range(3)] for y in range(3)]

#count variable to decide the turn of which player
count = 0  
global single


#Function to check the winner
def iswinner(b, p):

    if ((b[0][0] == p and b[0][1] == p and b[0][2] == p) or     #first row
        (b[1][0] == p and b[1][1] == p and b[1][2] == p) or     #second row
        (b[2][0] == p and b[2][1] == p and b[2][2] == p) or     #third row
        (b[0][0] == p and b[1][0] == p and b[2][0] == p) or     #first column
        (b[0][1] == p and b[1][1] == p and b[2][1] == p) or     #second column
        (b[0][2] == p and b[1][2] == p and b[2][2] == p) or     #third column
        (b[0][0] == p and b[1][1] == p and b[2][2] == p) or     #top left to bottom right diagonal
        (b[2][0] == p and b[1][1] == p and b[0][2] == p)):      #bottom left to top right diaginal
        
        return True

    else:
        return False
                

# To add text on button while playing the game
def add_text(s, i, j, game, p1, p2):

    global count
    #Alternate chances to both the players
    if board[i][j] == ' ':
        if count % 2 == 0:
            p1.config(state=DISABLED)
            p2.config(state=ACTIVE)
            board[i][j] = "O"
        else:
            p2.config(state=DISABLED)
            p1.config(state=ACTIVE)
            board[i][j] = "X"
        count += 1
        button[i][j].config(text=board[i][j])

    x = True
    #Checking winner for single player
    if (s):
        if (9>=count>=3):
            if iswinner(board, "O"):
                box = messagebox.showinfo("Winner", "Player: O won the match!")
                game.destroy()
                x = False

            elif iswinner(board, "X"):
                box = messagebox.showinfo("Winner", "Computer: X won the match!")
                game.destroy()
                x = False

        #if all the boxes are filled then it is a tie
            elif (count>=9):
                box = messagebox.showinfo("Draw","It's a Tie!!")
                game.destroy()
                x = False
        
        if(x):
            if count % 2 != 0:
                move = system()
                button[move[0]][move[1]].config(state=DISABLED)
                add_text(s, move[0], move[1], game, p1, p2)

    #for multiplayer
    else:  
        if (9>=count>=3):
            if iswinner(board, "O"):
                box = messagebox.showinfo("Winner", "Player 1: O won the match!")
                game.destroy()
                
            elif iswinner(board, "X"):
                box = messagebox.showinfo("Winner", "Player 2: X won the match!")
                game.destroy()

        #if all the boxes are filled then it is a tie
            elif (count>=9):
                box = messagebox.showinfo("Draw","It's a Tie!!")
                game.destroy() 


global temp
temp = []
for i in range(3):
    for j in range(3):
        temp.append([i,j])


def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win 
    bCopyy = getBoardCopy(b)
    bCopyy[i[0]][i[1]] = mark
    return iswinner(bCopyy, mark)


def testNextMove(b, mark, i):
    # Determines if a move opens up a win
    bCopy = getBoardCopy(b)
    bCopy[i[0]][i[1]] = mark
    winningMoves = 0
    
    for j in temp:
        if testWinMove(bCopy, mark, j) and bCopy[j[0]][j[1]] == ' ':
            winningMoves += 1
    return winningMoves >= 2


#To decide computer next move
def system():
    moves = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                moves.append([i, j])
    
    
    if (len(moves)==0):
        return

    #find that pointer at which computer or player can win in their next move and return it
    else:
        for j in ['X', 'O']:
            for i in moves:
                dupBoard = getBoardCopy(board)
                dupBoard[i[0]][i[1]] = j
                if (iswinner(dupBoard, j) and board[i[0]][i[1]] ==' '):
  
                    return i
        
        #check for 2 next moves that if computer can win
        for i in temp:
            if (board[i[0]][i[1]] == ' ' and testNextMove(board, 'X', i)):
                return i

        #check for 2 next moves that if player can win
        playerForks = 0
        for i in temp:
            if (board[i[0]][i[1]] == ' ' and testNextMove(board, 'O', i)):
                playerForks += 1
                tempMove = i

        if playerForks == 1:
            return tempMove

        elif playerForks == 2:
            for j in [[1,0], [0,1], [2,1], [1,2]]:
                if board[j[0]][j[1]] == ' ':
                    return j

        #center    
        c = [1, 1]         
        if (c in moves):
                return c

        #corner vacancies    
        corner = [[0,0], [0,2], [2,0], [2,2]]
        for j in corner:
            if (board[j[0]][j[1]] == ' '):
                return j
       
        #edge vacancies
        edge = [[0,1], [1,0], [2,1], [1,2]]
        for j in edge:
            if (board[j[0]][j[1]] == ' '):
                return j


# Make a duplicate of the board
def getBoardCopy(board):
    
    dupeBoard = []
    dupeBoard = [[board[y][x] for x in range(3)] for y in range(3)]
    
    return dupeBoard


#Making GUI of game board by adding 9 buttons
def gameboardGUI(game_board, p1, p2, s):
    global button
    button = []

    for i in range(3):
        m = 3+i
        button.append(i)
        button[i]=[]

        for j in range(3):
            n = j
            button[i].append(j)
        
            text = partial(add_text, s, i, j, game_board, p1, p2)
            #Creating buttons
            button[i][j] = Button(game_board, bd=5, command=text, height=4, width=10, font='arial')
            button[i][j].grid(row=m, column=n)

    game_board.mainloop()


#Initialize game board for multiplayer
def player(game_board):
    
    game_board.destroy()
    game_board = Tk()
    game_board.title("TIC-TAC-TOE")
    game_board.iconbitmap("D:/Internship @Afour/TicTacToe/tic-tac-toe.ico")

    qui = partial(Quit, game_board)
    
    #Player 1 button
    p1 = Button(game_board, text = "Player 1 : O", bg = "pink", fg = "blue", width = 10, font = 'arial')
      
    #Player 2 button
    p2 = Button(game_board, text = "Player 2 : X", bg = "pink", fg = "blue", width = 10, font = 'arial',
                state = DISABLED)
    
    #Quit button
    q = Button(game_board, text="Quit", command=qui, fg = "blue", width = 5, font = 'arial')

    #Adding to grid
    p1.grid(row = 0, column = 1)
    p2.grid(row = 1, column = 1)
    q.grid(row = 2, column = 2)
    single = 0
    gameboardGUI(game_board, p1, p2, single)


#Initialize game board foe single player
def computer(game_board):
    
    game_board.destroy()
    game_board = Tk()
    game_board.title("TIC-TAC-TOE")
    game_board.iconbitmap("D:/Internship @Afour/TicTacToe/tic-tac-toe.ico")

    qui = partial(Quit, game_board)
    
    #Player 1 button
    p1 = Button(game_board, text = "Player : O", bg = "pink", fg = "blue", width = 10, font = 'arial')
      
    #Computer button
    p2 = Button(game_board, text = "Computer : X", bg = "pink", fg = "blue", width = 10, font = 'arial',
                state = DISABLED)
    
    #Quit button
    q = Button(game_board, text="Quit", command=qui, fg = "blue", width = 5, font = 'arial')

    #Adding to grid
    p1.grid(row = 0, column = 1)
    p2.grid(row = 1, column = 1)
    q.grid(row = 2, column = 2)
    single = 1
    gameboardGUI(game_board, p1, p2, single)


#Function for quit button
def Quit(game_board):
    #Confirm message box  
    msg=messagebox.askquestion("Confirm","You still have chances!\nDo you really want to Quit?")
    if msg=='yes':
        game_board.destroy()


# Main function
def TicTacToe():
    global root
    root = Tk()
    
    root.title("TIC-TAC-TOE")
    root.geometry("400x400")
    root.iconbitmap("D:/Internship @Afour/TicTacToe/tic-tac-toe.ico")     #Adding icon
   
    bg = PhotoImage(file = "D:/Internship @Afour/TicTacToe/ttt.gif")       #Adding image
   
    label1 = Label( root, image = bg)        # Show image using label
    label1.place(x = 0, y = 0)
    
    #Adding welcome label
    head = Label(root, text = "Welcome to TIC-TAC-TOE!!",
                  fg = "Darkblue", width = 400, font = 'roboto')

    #Play button
    play = Button(root, text = "Play", command=nextwindow,
                activeforeground = 'blue', activebackground = "pink", bg = "brown", 
                fg = "yellow", width = 400, font = 'arial', bd = 5)
    
    #Exit button
    exit = Button(root, text = "Exit", command = root.destroy, 
                activeforeground = 'blue', activebackground = "pink", bg = "brown", 
                fg = "yellow", width = 400, font = 'arial', bd = 5)

    #Positions of buttons
    exit.pack(side="bottom")
    play.pack(side="bottom")
    head.pack(side="bottom") 
    root.mainloop()    

#adding window to select number of players
def nextwindow():
    root.destroy()
    root1 = Tk()
    root1.title("TIC-TAC-TOE")
    root1.geometry("335x400")

    root1.iconbitmap("D:/Internship @Afour/TicTacToe/tic-tac-toe.ico")     #Adding icon
   
    bg1 = PhotoImage(file = "D:/Internship @Afour/TicTacToe/TicTacToe1.png")       #Adding image
   
    label =Label(root1, image = bg1)        # Show image using label
    label.place(x = 0, y = 0)
    
    #Adding welcome label
    head = Label(root1, text = "Select number of players...",
                  fg = "Darkblue", width = 400, font = 'roboto')

    multi = partial(player, root1)
    comp = partial(computer, root1)

    #Multi player button
    play1 = Button(root1, text = "2 Players", command=multi,
                activeforeground = 'blue', activebackground = "pink", bg = "brown", 
                fg = "yellow", width = 400, font = 'arial', bd = 5)
    
    #Single player button
    play2 = Button(root1, text = "1 Player", command=comp,
                activeforeground = 'blue', activebackground = "pink", bg = "brown", 
                fg = "yellow", width = 400, font = 'arial', bd = 5)

    #Exit button
    exit = Button(root1, text = "Exit", command = root1.destroy, 
                activeforeground = 'blue', activebackground = "pink", bg = "brown", 
                fg = "yellow", width = 400, font = 'arial', bd = 5)

    #Positions of buttons
    exit.pack(side="bottom")
    play2.pack(side="bottom")
    play1.pack(side="bottom")
    head.pack(side="bottom")

    root1.mainloop()

'''  
def playagain():
    #Confirm message box  
    msgg=messagebox.askquestion("Play again?","Do you want to play again?")
    if msgg=='yes':
        nextwindow()'''


#Calling the main function
TicTacToe()