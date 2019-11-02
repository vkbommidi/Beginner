#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    '''Doc String: Printing the board'''
    clear_output()
    #printing out the board:
    print(board[7],board[10],board[8],board[10],board[9])
    print(board[11])
    print(board[4],board[10],board[5],board[10],board[6])
    print(board[11])
    print(board[1],board[10],board[2],board[10],board[3])


# In[2]:


game_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',10:'|',11:'--|---|--'}


# In[3]:


display_board(game_board)


# In[ ]:





# In[50]:


test_board = {1:'x',2:'o',3:'x',4:'o',5:'x',6:'o',7:'x',8:'o',9:'x',10:'|',11:'--|---|--'}


# In[51]:


display_board(test_board)


# In[52]:


#display_board() check ok.


# In[53]:


def player_input():
    '''Doc String: Funtion to choose players marker'''
    marker = ''
    while marker!='x' and marker!='o':
        marker=input('Player1 Choose eighter x or o',).lower()
    if marker=='x':
        return ('x','o')
    else:
        return ('o','x')


# In[54]:


player_input()


# In[9]:


player_input()


# In[10]:


player1_marker,player2_marker=player_input()


# In[11]:


player1_marker


# In[12]:


player2_marker


# In[13]:


#player_input check ok


# In[14]:


def place_marker(board,position,marker):
    board[position]=marker


# In[15]:


place_marker(test_board,4,player2_marker)


# In[16]:


display_board(test_board)


# In[17]:


#place_marker() check ok.


# In[55]:


def win_check(board,marker):
    return ((board[1]==board[2]==board[3]==marker) or (board[4]==board[5]==board[6]==marker) 
    or (board[7]==board[8]==board[9]==marker) or (board[1]==board[4]==board[7]==marker)
    or (board[2]==board[5]==board[8]==marker) or (board[3]==board[6]==board[9]==marker) 
    or (board[1]==board[5]==board[9]==marker) or (board[7]==board[5]==board[3]==marker))


# In[56]:


test_board[1]==test_board[5]==test_board[9]=='x'


# In[58]:


win_check(test_board,player2_marker)


# In[21]:


#win_check() check ok.


# In[22]:


from random import randint
def choose_first():
    '''Doc String: Randomly selects which player goes first'''
    if randint(0,1)==0:
        return "Player 2"
    else:
        return "Player 1"


# In[23]:


choose_first()


# In[24]:


choose_first()


# In[25]:


#choose_first() check ok.


# In[26]:


def space_check(board, position):
    return board[position]==' '


# In[27]:


test_board[5]=' '


# In[28]:


display_board(test_board)


# In[29]:


space_check(test_board,5)


# In[30]:


def full_board_check(board):
    for x in range(1,10):
        if space_check(board,x):
            return False
    return True


# In[31]:


full_board_check(test_board)


# In[32]:


#full_board_check() check ok.


# In[33]:


def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position(1-9)',))
    return position


# In[34]:


player_choice(test_board)


# In[35]:


#player_choice() check ok.


# In[36]:


def replay():
    return input('Do you want to play again:Enter yes or no',).lower().startswith('y')


# In[37]:


replay()


# In[38]:


replay()


# In[39]:


#reply() check ok.


# In[60]:


print('Welcome to Tic Tac Toe!')

while True:
    
    #Defined an empty board to start game
    game_on_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',10:'|',11:'--|---|--'}

    #Displaying the empty board to players
    display_board(game_on_board)

    #Player 1 is asked to choose a marker
    player_1_marker,player_2_marker=player_input()

    #Ramdomly selects which player goes first
    player=choose_first()

    print(f'{player} goes first')

    #Ask player "Are you ready"
    game_on = input('Are you ready to play: yes or no',)

    #Game Start

    while game_on.lower()[0] == 'y':
            if player == "Player 1":
                print(f'{player} turn')
                place = player_choice(game_on_board)
                place_marker(game_on_board,place,player_1_marker)
                display_board(game_on_board)
                if win_check(game_on_board,player_1_marker):
                    print('Player 1 won the game')
                    game_on='n'
                elif full_board_check(game_on_board):
                    print('The game is a tie')
                    game_on='n'
                player='Player 2'
            else:
                print(f'{player} turn')
                place = player_choice(game_on_board)
                place_marker(game_on_board,place,player_2_marker)
                display_board(game_on_board)
                if win_check(game_on_board,player_2_marker):
                    print(f'{player} won the game')
                    game_on='n'
                elif full_board_check(game_on_board):
                    print('The game is a tie')
                    game_on='n'
                player='Player 1'
    if not replay():
        break
    


# In[ ]:





# In[ ]:




