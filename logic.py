from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.player = 1
        self.xWins = 0
        self.oWins = 0
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.setupUi(self)

        self.square1.clicked.connect(lambda: self.turn(self.board, self.player, 0, 0, self.square1))
        self.square2.clicked.connect(lambda: self.turn(self.board, self.player, 0, 1, self.square2))
        self.square3.clicked.connect(lambda: self.turn(self.board, self.player, 0, 2, self.square3))
        self.square4.clicked.connect(lambda: self.turn(self.board, self.player, 1, 0, self.square4))
        self.square5.clicked.connect(lambda: self.turn(self.board, self.player, 1, 1, self.square5))
        self.square6.clicked.connect(lambda: self.turn(self.board, self.player, 1, 2, self.square6))
        self.square7.clicked.connect(lambda: self.turn(self.board, self.player, 2, 0, self.square7))
        self.square8.clicked.connect(lambda: self.turn(self.board, self.player, 2, 1, self.square8))
        self.square9.clicked.connect(lambda: self.turn(self.board, self.player, 2, 2, self.square9))
        self.saveButton.clicked.connect(lambda: self.saveGame())
        self.loadButton.clicked.connect(lambda: self.loadGame())
        self.reset_Button.clicked.connect(lambda: self.reset())

    def checkWin(self):
        """
        Checks if the game is in a winning or drawed state

        :param self.board: The current state of the board
        :return: True if a player has won
        """
        if self.board[0][0] == 1 and self.board[0][1] == 1 and self.board[0][2] == 1:
            return True
        if self.board[1][0] == 1 and self.board[1][1] == 1 and self.board[1][2] == 1:
            return True
        if self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 1:
            return True
        if self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1:
            return True
        if self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1:
            return True
        if self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1:
            return True
        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            return True
        if self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[0][2] == 1:
            return True
        if self.board[0][0] == 2 and self.board[0][1] == 2 and self.board[0][2] == 2:
            return True
        if self.board[1][0] == 2 and self.board[1][1] == 2 and self.board[1][2] == 2:
            return True
        if self.board[2][0] == 2 and self.board[2][1] == 2 and self.board[2][2] == 2:
            return True
        if self.board[0][0] == 2 and self.board[1][0] == 2 and self.board[2][0] == 2:
            return True
        if self.board[0][1] == 2 and self.board[1][1] == 2 and self.board[2][1] == 2:
            return True
        if self.board[0][2] == 2 and self.board[1][2] == 2 and self.board[2][2] == 2:
            return True
        if self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2:
            return True
        if self.board[2][0] == 2 and self.board[2][1] == 2 and self.board[0][2] == 2:
            return True



    def turn(self, player: int, x: int, y: int, button: QPushButton):
        """
        Checks if the square is availble, and if so, claims it for that player
        :param board: The current state of the board
        :param player: Whose turn it is
        :param x: the x coordinate of the square
        :param y: the y coordinate of the square
        :param button: the button that called this function
        """

        # Is this square claimed?
        if self.board[x][y] == 0:
            if player == 1:
                button.setText('X')
                self.board[x][y] = 1
                self.player = 2
                self.turnLabel.setText("O's Turn")
            if player == 2:
                button.setText('O')
                self.board[x][y] = 2
                self.player = 1
                self.turnLabel.setText("X's Turn")

        # Check for a win
        print('Checking for win...')
        print(self.board)
        if player == 1 and self.checkWin() == True:
            self.turnLabel.setText("X wins!")
        if player == 2 and self.checkWin() == True:
            self.turnLabel.setText('O wins!')

    def reset(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        print(self.board)
        self.square1.setText('')
        self.square2.setText('')
        self.square3.setText('')
        self.square4.setText('')
        self.square5.setText('')
        self.square6.setText('')
        self.square7.setText('')
        self.square8.setText('')
        self.square9.setText('')
        self.player = 1
        self.turnLabel.setText("X's Turn")

    def saveGame(self):
        file = open('game.txt')























