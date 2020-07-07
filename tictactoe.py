# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:47:12 2020

@author: neha_
"""
def CheckWin(board):
    if board.get(1) == board.get(2) == board.get(3):
        if board.get(1) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(1)))
    elif board.get(4) == board.get(5) == board.get(6):
        if board.get(4) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(4)))
    elif board.get(7) == board.get(8) == board.get(9):
        if board.get(7) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(7)))
    elif board.get(1) == board.get(4) == board.get(7):
        if board.get(1) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(1)))
    elif board.get(2) == board.get(5) == board.get(8):
        if board.get(2) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(2)))
    elif board.get(3) == board.get(6) == board.get(9):
        if board.get(3) in ('X','O'):
          x = print("Game Over. Player {0} won".format(board.get(3)))
    elif board.get(1) == board.get(5) == board.get(9):
        if board.get(1) in ('X','O'):
         x = print("Game Over. Player {0} won".format(board.get(1)))
    elif board.get(3) == board.get(5) == board.get(7):
        if board.get(3) in ('X','O'):
          x = print("Game Over. Player {0} won".format(board.get(3)))
    else:
       x = print("Game over. It's a tie")
       
    return x       
    

def tictactoe():
 print(" 1 || 2  || 3 ")
 print("-----------")
 print(" 4 || 5  || 6 ")
 print("-----------")
 print(" 7 || 8  || 9 ")

 Board = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
 y = 9

 while y >= 1:
    
  p1 = input("P1 enter position: ")
  p1 = int(p1)
  Board.update({p1:"X"})
  ##print("position at 1 is {0}".format(Board.get(1)))
  print(Board)
  y=y-1
  print(y)
 
  p2 = input("P2 enter position: ")
  p2 = int(p2)
  Board.update({p2:"O"})
  print(Board)
  y=y-1
  print(y) 
  if y == -1:   
   CheckWin(Board)
     



