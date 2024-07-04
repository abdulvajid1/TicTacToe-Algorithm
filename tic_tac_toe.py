class Tictactoe:
    def __init__(self):

        # initialize a variable for looping through the until the game is over
        self.game_over = False

        # Initialize variable for checking win or tie
        self.win=False

        # Initialize the board of values
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
        
        # initialize variable for switching player while on game
        self.player_turn = True

    # Draw the board
    def draw_board(self):
        # We can create each row that separate by | and then we use formate for telling the value in each gap
        self.row0 = "| {} | {} | {} |".format(self.board[0][0], self.board[0][1], self.board[0][2])
        self.row1 = "| {} | {} | {} |".format(self.board[1][0], self.board[1][1], self.board[1][2])
        self.row2 = "| {} | {} | {} |".format(self.board[2][0], self.board[2][1], self.board[2][2])
        print(self.row0)
        print(self.row1)
        print(self.row2)

    # Firts player turn
    def first_player_turn(self):
        self.entry_to_board('X')

    # Second player turn
    def second_player_turn(self):
        self.entry_to_board('0')

    # Checking any type of game of overs
    def check_win(self,item):
        if self.check_tie():
            self.game_over=True

        elif self.check_rows(item):
            print(self.check_rows(item))
            self.game_over=True
            self.win = True

        elif self.check_cols(item):
            print(self.check_cols(item))
            self.game_over=True
            self.win = True

        elif self.check_diagonals(item):
            print(self.check_cols(item))
            self.game_over=True
            self.win = True

    # Checking rows
    def check_rows(self,item):
        if self.board[0][0]==item and self.board[0][1]==item and self.board[0][2]==item:
            return 'Player {} is the winner'.format(item)
        elif self.board[1][0]==item and self.board[1][1]==item and self.board[1][2]==item:
            return 'Player {} is the winner'.format(item)
        elif self.board[2][0]==item and self.board[2][1]==item and self.board[2][2]==item:
            return 'Player {} is the winner'.format(item)
        else:
            return False
            


    # Checking cols
    def check_cols(self,item):
        if self.board[0][0] == item and self.board[1][0] == item and self.board[2][0] == item:
            return 'Player {} is the winner'.format(item)
        elif self.board[0][1] == item and self.board[1][1] == item and self.board[2][1] == item:
            return 'Player {} is the winner'.format(item)
        elif self.board[0][2] == item and self.board[1][2] == item and self.board[2][2] == item:
           return 'Player {} is the winner'.format(item)
        else:
           return False
    # Checking diagnoals
    def check_diagonals(self,item):
        if self.board[0][0] == item and self.board[1][1] == item and self.board[2][2] == item:
           return 'Player {} is the winner'.format(item)
        elif self.board[0][2] == item and self.board[1][1] == item and self.board[2][0] == item:
            return 'Player {} is the winner'.format(item)
        else:
            return False

    # Entry X or 0 to the board
    def entry_to_board(self,item):
        user_input = input('Enter {} person move in "row,column":'.format(item))
        # Check any error in user input
        error_check = self.check_user_input(user_input)
        # if error_check is 1 then all is ok
        if error_check == 1:
            # format the user input to get both row and column number separately
            row,col = self.user_input_formatting(user_input)
            if self.check_already_in_board(row,col):
                # if the player is first person then he will send X as input into board
                # else the second player which will be 0 as input
                self.change_player_turn()
                if item == 'X':
                    self.board[row][col] = item
                else:
                    self.board[row][col] = item

            else:
                print('the space is already occupied')
        # If the error_check is not 1 then there is some error that will print here
        else:
            print(error_check)

    def change_player_turn(self):
        if self.player_turn:
            self.player_turn=False
        else:
            self.player_turn=True
        return 1

    def check_already_in_board(self,row,col):
        # Check the space is empty
        if self.board[row][col] ==' ':
            return True
        else:
            return False

    def check_tie(self):
        if self.win:
            return
        else:
            self.board_full = True
            for row in range(0, 3):
                for col in range(0, 3):
                    if self.board[row][col] == ' ':
                        self.board_full = False
            if self.board_full:
                print('The Game Tied')
                self.game_over=True
            

    def user_input_formatting(self,user_input):
        # check the length of the list
        user_input = user_input.strip().split(',')
        if len(user_input) == 2:
            # convert both item in the list in integer format
            row_col_list = self.convert_integer(user_input)
            # If there is no errors then we will return the formatted row and column
            return row_col_list
        # if length user input after splitting the string in ',' then there is some other mistake
        else:
            return 'Please provide the input in the format "row,column" '


    def check_user_input(self,user_input):
        # check the user input is in list format
        if type(user_input) == str:
            user_input = self.user_input_formatting(user_input)
            # Now we check weather the user input is a list which contain the [row and col]
            # all other format that returning are string that tells some error
            if type(user_input) == list:
                if user_input[0] > 2 or user_input[0] < 0 or user_input[1] > 2 or user_input[1] < 0:
                    return 'use the row and the column number between 0 to 3'
                else:
                    return 1  # indicate all is ok
            else:
                print(user_input)
        else:
            return 'Please provide 2 values that separated by ",", one for selecting the rows and other for column'



    def convert_integer(self,user_input):
        try:
            row = int(user_input[0])
            col = int(user_input[1])
        # if there is any error in the conversion then the user input will contain some mistake
        except Exception:
            return "provide both variable in number"
        return list([row,col])


    def play(self):
        self.draw_board()
        while not self.game_over:
            # we will call the board when we create the object of the class tic-tac-toe
            if self.player_turn:
                self.first_player_turn()
                self.draw_board()
                self.check_win('X')
            else:
                self.second_player_turn()
                self.draw_board()
                self.check_win('O')
game = Tictactoe()
game.play()

